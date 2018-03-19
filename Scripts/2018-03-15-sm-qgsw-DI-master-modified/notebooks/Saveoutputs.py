################################
# SSH save function            #
################################ 
import numpy as np 
import netCDF4 as nc
from datetime import datetime
from datetime import timedelta

def Save_present_time_outputs(field0,n_ens,lon2d,lat2d,date0):
    """
    NAME 
        Saveoutputs 

    DESCRIPTION
        Save a netcdf file of an ensemble of SSH fields

        Args:  
            field0 (3D array of dimensions [n_ens,n_lon,n_lat]): ensemble of SSH fields  
            n_ens (integer): number of ensemble member
            lon (2D array of dimensions [n_lon,n_lat]): longitud field
            lat (2D array of dimensions [n_lon,n_lat]): latitud field 
            date0 (datetime object): current date
            
        Internal args: 
            name_exp (string): name of the experiment

        Returns:  
            None 

    """
    #date0=datetime(2012,6,14)
    name_exp='QGSWOSMO_IniNATL60_Ensforecast'
    path='/Users/sammymetref/Documents/Boost-Swot/Notebooks/GitHub/Personal_Files/2018/Data/DA_OSMOSIS/'+name_exp+'/' 
    ncout = nc.Dataset(path+name_exp+'_y'+str(date0.year)+'m'+str(date0.month)+'d'+str(date0.day)+'h'+str(date0.hour)+'_SSHdegrad.nc', 'w', format='NETCDF3_CLASSIC')
    ncout.createDimension('x', lon2d.shape[0])
    ncout.createDimension('y', lat2d.shape[1])
    ncout.createDimension('member', n_ens)
    nclon = ncout.createVariable('lon', 'f', ('x','y',))
    nclat = ncout.createVariable('lat', 'f', ('x','y',)) 
    ncens = ncout.createVariable('ens', 'f', ('member',)) 
    nchei = ncout.createVariable('SSH', 'f', ('member','x','y',)) 
    nclat[:,:] = lat2d 
    nclon[:,:] = lon2d  
    ncens[:] = range(n_ens) 
    nchei[:,:,:] = field0 
    ncout.close()
    
    return 
        
