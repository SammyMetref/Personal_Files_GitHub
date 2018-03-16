################################
# SSH initialization functions #
################################ 
import numpy as np
import qgsw

def EnsembleModel(function,field0,n_ens,lon2d,lat2d,time0,*args):
    field=np.zeros([n_ens,np.shape(lon2d)[0],np.shape(lat2d)[1]],)
    print(np.shape(field0[:,:,:]))
    print(np.shape(lon2d))
    print(np.shape(lat2d))
    print(time0)
    for i_ens in range(n_ens):
        tmp_field=field0[i_ens,:,:]
        field[i_ens,:,:]=function(tmp_field,lon2d,lat2d,time0,*args)
        
    return field
        


def QG_SW(field0,lon2d,lat2d,time0): 
    c=field0*0. + 2.5 # in m/s 
    dtmodel=600 # propagator time step
    deltat=time0
    
    return qgsw.qgsw(Hi=field0, c=c, lon=lon2d, lat=lat2d, tint=time0, dtout=deltat, dt=dtmodel,rappel=None,snu=0.)