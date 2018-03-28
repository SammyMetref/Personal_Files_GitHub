##########################################
# Experimental parameters                #
##########################################


from Exp1_params import *


##########################################
# Static parameters (not to be modified) #
##########################################
 
# General libraries
import sys,os,shutil
sys.path.insert(0,'/Users/sammymetref/Documents/Boost-Swot/Notebooks/GitHub/Personal_Files/2018/Scripts/2018-03-15-sm-qgsw-DI-master-modified/2018-03-27-sm-SWOT_DA/') 
import numpy as np
import matplotlib.pylab as plt
import time
import netCDF4 as nc  
from datetime import datetime
from datetime import timedelta
import time  


# Boost-SWOT specific libraries
from initialization_functions import Initialization
from Model import EnsembleModel
from Observations import ObservationCheck
from Observations import ObsOperator
from Saveoutputs import Save_present_time_outputs 

# SWOT cycle time
cycle_time=timedelta(days=20,hours=20,minutes=45,seconds=1)    

# SWOT pass names
pass_names=['p003', 'p031', 'p059', 'p087', 'p098', 'p115', 'p126', 'p154', 'p182', 'p210', 'p225', 'p238', 'p253', 'p266', 'p281', 'p309', 'p337', 'p365', 'p376', 'p393', 'p404', 'p432', 'p460', 'p488', 'p516', 'p531', 'p544', 'p559']

# observation initial timestamp set by SWOT simulator
init_obs_date=datetime(2012,6,14,0)  #(yyyy,mm,dd,hh)         

# path and names of the state vectors
state_vectors_names='/Users/sammymetref/Documents/Boost-Swot/Notebooks/GitHub/Personal_Files/2018/Scripts/2018-03-15-sm-qgsw-DI-master-modified/notebooks/2018-03-27-sm-SWOT_DA/TMP_DA/state_vectors.nc'
 
 
# temporary data assimilation directory path 
tmp_DA_path="/Users/sammymetref/Documents/Boost-Swot/Notebooks/GitHub/Personal_Files/2018/Scripts/2018-03-15-sm-qgsw-DI-master-modified/notebooks/2018-03-27-sm-SWOT_DA/TMP_DA/"

# SOSIE path
sosie_path="/Users/sammymetref/Documents/Boost-Swot/Notebooks/GitHub/Personal_Files/2018/Scripts/2018-03-15-sm-qgsw-DI-master-modified/notebooks/2018-03-27-sm-sosie-modified/bin/" 

# name of SOSIE output
name_sosie_output="ssh_QG-OSMOSIS-SWOT-SWATH_bilin.nc"

# name of SOSIE map
name_sosie_map="../sosie_mapping_QG-OSMOSIS-SWOT-SWATH.nc"
