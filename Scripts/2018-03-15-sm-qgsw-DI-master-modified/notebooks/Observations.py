################################
# SSH initialization functions #
################################
import netCDF4 as nc
import numpy as np


def ObservationCheck(time1,time2):
    """
    NAME 
        ObservationCheck 

    DESCRIPTION
        ObservationCheck verifies if observations are available between time1 and time2

        Args:
            time1 (datetime object): first time 
            time2 (datetime object): second time 

        Returns:
            observations_available (boolean): Informs if observations are available between time1 and time2  
    """          
    
    observations_available=True
            
    return observations_available

 