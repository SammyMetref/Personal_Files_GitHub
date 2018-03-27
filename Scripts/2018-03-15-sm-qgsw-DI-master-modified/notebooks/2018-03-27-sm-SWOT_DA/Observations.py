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


def ObsOperator(function,state_vectors_names,observation_name,n_ens,*args):
    """
    NAME 
        ObsOperator 

    DESCRIPTION
        Global observation operator function

        Args:
            function (function): observation operator function 
            state_vectors_names (array of strings): path and names of state_vectors
            observation_name (array of strings): path and name of observation
            n_ensemble (integer): number of ensemble members

        Returns:
            function(state_vectors_names,n_ens,*args): output of *function*  
    """            
            
    return function(state_vectors_names,observation_name,n_ens,*args)


def ObsOperator_SOSIE_SWOT(state_vectors_names,observation_name,n_ens=1):
    """
    NAME 
        ObsOperator_SOSIE_SWOT

    DESCRIPTION 
        Call SOSIE to create the SWOT observation projection of the model states (from *state_vectors_names* files)
        
        Args: 
            state_vectors_names (array of strings): path and names of state_vectors
            observation_name (array of strings): path and name of observation
            n_ens (integer): number of ensemble members 

        Returns: 
            state_projections_names (array of strings): path and names of model state projection onto the SWOT observation plane 

    """
    
    sosie_path="/Users/sammymetref/Documents/Boost-Swot/Notebooks/GitHub/Personal_Files/2018/Scripts/2018-03-15-sm-qgsw-DI-master-modified/notebooks/2018-03-27-sm-sosie-modified/bin/"
    tmp_path="/Users/sammymetref/Documents/Boost-Swot/Notebooks/GitHub/Personal_Files/2018/Scripts/2018-03-15-sm-qgsw-DI-master-modified/notebooks/2018-03-27-sm-SWOT_DA/TMP_DA/"
    str_observation_name="'"+observation_name+"'"
    
    state_projection_names=[]
    for i_ens in range(n_ens):
        
        # Seperating state_vectors by ensemble member
        stringiens=str(i_ens).zfill(2)
        state_projection_name=state_vectors_names[:-4]+"_"+stringiens+".nc"
        str_state_projection_name="'"+state_vectors_names[:-4]+"_"+stringiens+".nc'"
        
        state_projection_names=np.append(state_projection_names,state_projection_name)
        cmd1="ncks -d member,"+stringiens+","+stringiens+" "+state_vectors_names+" "+state_projection_name
        os.system(cmd1) 
        
        # Creating SOSIE namelist
        name_source=state_vectors_names+"_"+stringiens
        name_target=observation_name
        
        with open(sosie_path+"namelist", 'r') as file: 
            data = file.readlines() 
        data[101] = "cf_in     = "+str_state_projection_name+"\n"
        data[107] = "cf_x_in   = "+str_state_projection_name+"\n"
        data[168] = "cf_x_out   = "+str_observation_name+"\n" 
        with open(sosie_path+"namelist", 'w') as file:
            file.writelines( data ) 
               
        # Running SOSIE 
        cmd6=sosie_path+"sosie.x -f "+sosie_path+"namelist"
        os.system(cmd6)  
            
        # Renaming SOSIE output as the i_ens state_projection
        name_output="state_projections_"+str(i_ens).zfill(2)+".nc"
        cmd7="mv "+tmp_path+"ssh_QG-OSMOSIS-SWOT-SWATH_bilin.nc "+tmp_path+name_output
        os.system(cmd7)  
            
    # Erasing SOSIE map 
    cmd8="rm "+tmp_path+"../sosie_mapping_QG-OSMOSIS-SWOT-SWATH.nc"    
    os.system(cmd8)
    
    return