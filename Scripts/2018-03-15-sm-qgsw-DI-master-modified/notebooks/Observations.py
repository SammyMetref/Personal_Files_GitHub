################################
# SSH initialization functions #
################################
import netCDF4 as nc
import numpy as np


def ObservationCheck(time1,deltat,observationpath):
    """
    NAME 
        ObservationCheck 

    DESCRIPTION
        ObservationCheck verifies if observations are available in [time1-deltat,time1+deltat]

        Args:
            time1 (datetime object): current time 
            deltat (datetime.timedelta object): data assimilation cycle time  
            observationpath (string): path to observations

        Returns:
            observations_available (boolean): Informs if observations are available between time1 and time2  
    """          
    
    observations_available=True
            
    return observations_available

 