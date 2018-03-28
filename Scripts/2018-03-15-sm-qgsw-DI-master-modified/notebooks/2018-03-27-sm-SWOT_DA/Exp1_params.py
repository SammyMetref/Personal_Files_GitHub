##########################################
##########################################
##     Experiment 1 - Parameters        ##
########################################## 
##########################################
from datetime import datetime
from datetime import timedelta 

 
################################
#   Initialization parameters  #
################################
n_ensemble=1                                                            # ensemble size 
from initialization_functions import NATL60state as initialization      # initialization function
  
################################
#       Time parameters        #
################################
init_date=datetime(2012,6,14,0)                                         # initial date(yyyy,mm,dd,hh)
present_date=init_date                                                  # present date(yyyy,mm,dd,hh)
final_date=datetime(2012,6,16,0)                                        # final date (yyyy,mm,dd,hh)
assimilation_time_step=timedelta(days=1)                                # assimilation time step   

################################
#       Model parameters       #
################################ 
from Model import QG_SW as model                                        # Model function 

################################
#    Observation parameters    #
################################
obs_path="/Users/sammymetref/Documents/Boost-Swot/Notebooks/GitHub/Personal_Files/2018/SwotSimulator/example/swot_output/"
                                                                        # observation path
obs_prefixe="swot292-OSMOSIS"                                           # observation prefixe 
from Observations import ObsOperator_SOSIE_SWOT as obsop                # observation operator
    
################################
#      Outputs parameters      #
################################
saveoutputs=True                                                        # save all outputs
 