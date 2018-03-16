################################
# SSH initialization functions #
################################
import netCDF4 as nc
import numpy as np


def Initialization(function,*args):
    return function(*args)


def NATL60state(n_ens=1,path='../'):
    if n_ens>1:
        print('Error: reststate only works for one-member-ensemble')
        return
    fid = nc.Dataset(path)
    lon=np.array(fid.variables["nav_lon"][:])
    lat=np.array(fid.variables["nav_lat"][:]) 
    multiplefields=np.array(fid.variables["degraded_sossheig"][:,:]) 
    
    field=np.zeros([n_ens,np.shape(lon)[0],np.shape(lat)[1]],)
    field[0,:,:]=multiplefields[0,:,:]
    
    return [field, lon, lat]