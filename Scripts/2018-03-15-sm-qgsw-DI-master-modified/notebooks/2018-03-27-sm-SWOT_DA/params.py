#############
# Libraries #
############# 

# General libraries
import sys,os,shutil
sys.path.insert(0,'/Users/sammymetref/Documents/Boost-Swot/Notebooks/GitHub/Personal_Files/2018/Scripts/2018-03-15-sm-qgsw-DI-master-modified/2018-03-27-sm-SWOT_DA/') 
import numpy as np
import matplotlib.pylab as plt
import time
import netCDF4 as nc 
#import modgrid
from datetime import datetime
from datetime import timedelta
from datetime import datetime
from datetime import timedelta
import time 

# Model specific libraries
from importlib.machinery import SourceFileLoader 
modgrid = SourceFileLoader("modgrid", "/Users/sammymetref/Documents/Boost-Swot/Notebooks/GitHub/Personal_Files/2018/Scripts/2018-03-15-sm-qgsw-DI-master-modified/notebooks/Models/modgrid.py").load_module() 

# DA specific libraries
from initialization_functions import Initialization
from Model import EnsembleModel
from Observations import ObservationCheck
from Saveoutputs import Save_present_time_outputs 

##############
# Parameters #
############## 

# Initialization parameters
n_ensemble=1                                 # ensemble size

# Initialization function  
from initialization_functions import NATL60state as initialization  
 
    
# Time parameters
init_date=datetime(2012,6,14,0)              # initial date(yyyy,mm,dd,hh)
present_date=init_date                       # present date(yyyy,mm,dd,hh)
final_date=datetime(2012,6,16,0)             # final date (yyyy,mm,dd,hh)
assimilation_time_step=timedelta(days=1)     # assimilation time step   

# Model function 
from Model import QG_SW as model 

# Observation parameters 
obs_path="/Users/sammymetref/Documents/Boost-Swot/Notebooks/GitHub/Personal_Files/2018/SwotSimulator/example/swot_output/"
                                                   # observation path
obs_prefixe="swot292-OSMOSIS"                # observation prefixe 
    
# Outputs parameters
plotoutputs=False                            # plot final outputs
saveoutputs=True                             # save all outputs


##########################################
# Static parameters (not to be modified) #
##########################################


cycle_time=timedelta(days=20,hours=20,minutes=45,seconds=1)    # SWOT cycle time
 
pass_names=['p003', 'p031', 'p059', 'p087', 'p098', 'p115', 'p126', 'p154', 'p182', 'p210', 'p225', 'p238', 'p253', 'p266', 'p281', 'p309', 'p337', 'p365', 'p376', 'p393', 'p404', 'p432', 'p460', 'p488', 'p516', 'p531', 'p544', 'p559']
                                                   # SWOT pass names
init_obs_date=datetime(2012,6,14,0)          # observation initial timestamp (yyyy,mm,dd,hh) 