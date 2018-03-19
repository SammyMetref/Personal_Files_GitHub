################################
# SSH initialization functions #
################################ 
import numpy as np
import qgsw

def EnsembleModel(function,field0,n_ens,lon2d,lat2d,time0,*args):
    """
    NAME 
        EnsembleModel 

    DESCRIPTION
        Global model function

        Args: 
            function (function): model function
            field0 (3D array of dimensions [n_ens,n_lon,n_lat]): ensemble of SSH fields  
            n_ens (integer): number of ensemble member
            lon (2D array of dimensions [n_lon,n_lat]): longitud field
            lat (2D array of dimensions [n_lon,n_lat]): latitud field 
            time0 (integer [in seconds]): time of propagation

        Returns: 
            SSH_fields (3D array of dimensions [n_ensemble,n_lon,n_lat]): ensemble of SSH fields propagated from *field0* and during *time0* time

    """
    field=np.zeros([n_ens,np.shape(lon2d)[0],np.shape(lat2d)[1]],) 
    for i_ens in range(n_ens):
        tmp_field0=field0[i_ens,:,:]
        tmp_field=function(tmp_field0,lon2d,lat2d,time0,*args) 
        field[i_ens,:,:]=tmp_field
        
    return field
        


def QG_SW(field0,lon2d,lat2d,time0): 
    """
    NAME 
        QG_SW

    DESCRIPTION 
        Function calling the quasi-geostrophic shallow water model (C. Ubelmann)

        Args: 
            field0 (2D array of dimensions [n_lon,n_lat]): SSH field
            lon2d (2D array of dimensions [n_lon,n_lat]): longitud field
            lat2d (2D array of dimensions [n_lon,n_lat]): latitud field 
            time0 (integer [in seconds]): time of propagation

        Internal args:
            c (2D array of dimensions [n_lon,n_lat]): Rossby first baroclinic phase speed  
            dtmodel (integer [in seconds]): model time step 
            deltat (integer [in seconds]): output time step 

        Returns: 
            field[-1,:,:] (2D array of dimensions [n_lon,n_lat]): SSH field after propagation

    """     
    c=field0*0. + 2.5 # in m/s 
    dtmodel=600 # propagator time step
    deltat=time0
    
    field, trash = qgsw.qgsw(Hi=field0, c=c, lon=lon2d, lat=lat2d, tint=time0, dtout=deltat, dt=dtmodel,rappel=None,snu=0.)
     
    
    return field[-1,:,:]