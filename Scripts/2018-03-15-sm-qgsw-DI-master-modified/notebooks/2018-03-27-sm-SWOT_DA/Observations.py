################################
# SSH initialization functions #
################################
import netCDF4 as nc
import numpy as np
import os.path


def ObservationCheck(time1,deltat,observationpath,observationprefixe,ncycle,pass_names,initobsdate):
    """
    NAME 
        ObservationCheck 

    DESCRIPTION
        ObservationCheck verifies if observations are available in [time1-deltat,time1+deltat]

        Args:
            time1 (datetime object): current time 
            deltat (datetime.timedelta object): data assimilation cycle time  
            observationpath (string): path to observations
            observationprefixe (string): prefixe of observations
            ncycle (int): cycle number
            initobsdate (datetime object): initial observation time (yyyy,mm,dd,01,01,01 of the NATL60 input of SWOT simulator)

        Returns:
            observations_available (boolean): Informs if observations are available in [time1-deltat,time1+deltat]
            file_obs (1D string array): the list of file names where observations where encountered
             
    """          
    obspathpref=observationpath+observationprefixe+'_c'+str(ncycle).zfill(2) 
    
    time1mdeltat_seconds_fromfirstobs=(time1-deltat/2-initobsdate).total_seconds()
    time1pdeltat_seconds_fromfirstobs=(time1+deltat/2-initobsdate).total_seconds()
    
    #print(time1mdeltat_seconds_fromfirstobs)
    #print(time1pdeltat_seconds_fromfirstobs)
    
    obs_encountered=0 
    file_obs=np.array([])
    for pass_name in pass_names:
        file=obspathpref+'_'+pass_name+'.nc'  
        if os.path.isfile(file): 
            fid = nc.Dataset(file)
            obstimes=np.array(fid.variables["time_sec"][:]) 
            check_obs_in_pass=(time1mdeltat_seconds_fromfirstobs < obstimes[0]) and (obstimes[0] < time1pdeltat_seconds_fromfirstobs) or (time1mdeltat_seconds_fromfirstobs < obstimes[-1]) and (obstimes[-1] < time1pdeltat_seconds_fromfirstobs)  
            
            if check_obs_in_pass: 
                file_obs=np.append(file_obs,file)
                obs_encountered=obs_encountered + 1    


    if obs_encountered!=0: 
        return [True,file_obs]   
         
    return [False,None]

def GetObsTime(observation_path,observation_name):
    """
    NAME 
        GetObsTime 

    DESCRIPTION
        GetObsTime retrive the time of *observation_name* at *observation_path*

        Args: 
            observation_path (string): path to observation
            observation_name (string): name of observation

        Returns:
            obs_time (float, in seconds): observation time 
    """    
    
    file=observation_path+observation_name 
    fid = nc.Dataset(file)
    obstimes=np.array(fid.variables["time_sec"][:])
    obstime=obstimes[0]
    
    return obstime