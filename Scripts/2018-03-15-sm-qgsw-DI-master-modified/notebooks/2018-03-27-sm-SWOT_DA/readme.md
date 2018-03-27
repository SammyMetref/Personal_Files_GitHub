{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Assimilation of SWOT data "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Description"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1. Experiment setting\n",
    "#### 1.1. Initialization settings \n",
    "\n",
    "###### Definitions\n",
    "\n",
    "- <span style=\"color:blue\">n_ensemble</span>: number of ensemble members, *<span style=\"color:gray\">integer</span>*\n",
    "  \n",
    "###### Imports\n",
    "\n",
    "- Initialization from initialization_functions: global initialization function calling *initialization*\n",
    "- initialization from initialization_functions:\n",
    "    * <span style=\"color:blue\">NATL60state</span>: initialization of a single SSH field (n_ensemble==1) using an internally prescribed SSH field of dimensions\n",
    "\n",
    "#### 1.2.  Time settings\n",
    "\n",
    "###### Definitions\n",
    "\n",
    "- <span style=\"color:blue\">init_date</span>: experimental starting date, *<span style=\"color:gray\">datetime object (yyyy,mm,dd,hh)</span>*\n",
    "- present_date: current date starting at *init_date* and ending at *final_date* during time loop, *<span style=\"color:gray\">datetime object (yyyy,mm,dd,hh)</span>*\n",
    "- <span style=\"color:blue\">final_date</span>: experimental ending date, *<span style=\"color:gray\">datetime object (yyyy,mm,dd,hh)</span>*\n",
    "- <span style=\"color:blue\">assimilation_time_step</span>: assimilation cycle time step, *<span style=\"color:gray\">timedelta object (in hours)</span>* \n",
    "- cycle_time: SWOT cycle time step, *<span style=\"color:gray\">timedelta object (in hours)</span>* \n",
    "\n",
    "#### 1.3.  Model settings \n",
    "\n",
    "###### Definitions\n",
    " \n",
    "###### Imports\n",
    "- EnsembleModel from Model: global model function propagating an ensemble of state vectors over a time period by calling *model* *n_ensemble*-times \n",
    "\n",
    "- model from Model:   \n",
    "    * <span style=\"color:blue\">QG_SW</span>: quasi-geostrophic shallow-water model propagating an SSH field over a time period \n",
    "        \n",
    " \n",
    "\n",
    "#### 1.4.  Observation settings\n",
    "\n",
    "###### Definitions\n",
    "\n",
    "- <span style=\"color:blue\">obs_path</span>: observation directory path, *<span style=\"color:gray\">string</span>*  \n",
    "\n",
    "###### Imports\n",
    "\n",
    "- ObservationCheck from Observation: function checking if observations are available at assimilation time \n",
    "\n",
    "\n",
    "#### 1.5.  Analysis settings\n",
    "\n",
    "###### Parameters\n",
    "\n",
    "- a \n",
    "\n",
    "###### Functions\n",
    "\n",
    "- a\n",
    "\n",
    "#### 1.6.  Outputs settings\n",
    "\n",
    "###### Definitions\n",
    "\n",
    "- <span style=\"color:blue\"> outputs</span>: command the \"plot\" or \"save\" of state vectors, *<span style=\"color:gray\"> string </span>*\n",
    "\n",
    "###### Functions\n",
    "\n",
    "- Save_present_time_outputs from Saveoutputs: save an ensemble state vectors at a definite time in a file\n",
    "\n",
    "### 2. Initialization\n",
    "\n",
    "###### Definitions\n",
    "  \n",
    "- state_vectors0: ensemble of initial state vectors produced by *Initialization* function, *<span style=\"color:gray\">tuple (3D array of dimensions [n_ensemble,n_lon, n_lat])</span>*\n",
    "- lon: longitud field produced by *Initialization* function, *<span style=\"color:gray\">2D array of dimensions [n_lon, n_lat]</span>*\n",
    "- lat: latitud field produced by *Initialization* function, *<span style=\"color:gray\">2D array of dimensions [n_lon, n_lat]</span>*\n",
    "\n",
    "### 3. Time loop\n",
    "\n",
    "- i_cycle: temporary cycle counter, *<span style=\"color:gray\">integer</span>* \n",
    "- present_date: date of the current cycle, *<span style=\"color:gray\">datetime object (yyyy,mm,dd,hh)</span>*\n",
    "\n",
    "\n",
    "#### 3.1. Propagation \n",
    "\n",
    "###### Definitions\n",
    "- state_vectors: ensemble of *present_date* state vectors produced by *model* function, *<span style=\"color:gray\">tuple (3D array of dimensions [n_ensemble,n_lon,n_lat])</span>*\n",
    "\n",
    "#### 3.2. Observation check\n",
    "#### 3.3. Observation retrieval\n",
    "#### 3.4. Analysis \n",
    "#### 3.5. Outputs \n",
    "### 4. Final outputs\n",
    " "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}