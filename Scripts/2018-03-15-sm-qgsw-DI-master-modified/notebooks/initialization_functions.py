################################
# SSH initialization functions #
################################
import netCDF4 as nc
import numpy as np


def Initialization(function,n_ens,*args):
    """
    NAME 
        Initialization 

    DESCRIPTION
        Global initialization function

        Args:
            function (function): initialization function 
            n_ensemble (integer): number of ensemble members

        Returns:
            SSH_fields0 (3D array of dimensions [n_ensemble,n_lon,n_lat]): ensemble of initial SSH fields produced by function
            lon (2D array of dimensions [n_lon,n_lat]): longitud field produced by function
            lat (2D array of dimensions [n_lon,n_lat]): latitud field produced by function 
    """            
            
    return function(n_ens,*args)


def NATL60state(n_ens=1):
    """
    NAME 
        NATL60state

    DESCRIPTION 

        Args: 
            n_ens (integer): number of ensemble members

        Internal args:
            file_name_init_SSH_field (string): name of the initialization file needed to create the inital SSH field(s) 
            path_init_SSH_field (string): path of the initialization file needed to create the inital SSH field(s)

        Returns: 
            field (2D array of dimensions [n_lon,n_lat]): initial SSH field in file *path_init_SSH_field*
            lon (2D array of dimensions [n_lon,n_lat]): longitud field in file *path_init_SSH_field*
            lat (2D array of dimensions [n_lon,n_lat]): latitud field in file *path_init_SSH_field*

    """

    # Initial SSH field file name
    file_name_init_SSH_field='NATL60OSMO-CJM165_y2012m06d14-y2013m10d01.1d_SSHdegrad.nc'
    # Initial SSH field path
    path_init_SSH_field='/Users/sammymetref/Documents/Boost-Swot/Notebooks/GitHub/Personal_Files/2018/Data/OSMOSIS/'+file_name_init_SSH_field


    if n_ens>1:
        print('Warning: NATL60state only works for one-member-ensemble') 
    fid = nc.Dataset(path_init_SSH_field)
    lon=np.array(fid.variables["nav_lon"][:])
    lat=np.array(fid.variables["nav_lat"][:]) 
    multiplefields=np.array(fid.variables["degraded_sossheig"][:,:]) 
    
    field=np.zeros([n_ens,np.shape(lon)[0],np.shape(lat)[1]],)
    for i_ens in range(n_ens):
        field[i_ens,:,:]=multiplefields[0,:,:]
    
    return [field, lon, lat]