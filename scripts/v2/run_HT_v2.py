# This notebook runs the run_HT function for each basin,
# emission scenario, model, and time period.

# Import numpy and matplotlib
import numpy as np
from numpy import reshape
import os
import collections
from pathlib import Path

# Import the pymt package
import pymt.models

# Create new instance. With each new run, it is wise to rename the instance.
hydrotrend = pymt.models.Hydrotrend()

# Set relative path -- avoid writing absolute path
collections.__file__
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Hydrotrend')

# Add directory for output files
config_file, config_folder = "hydro_config.txt", filename

# Initialize the model with the configure file in the configure folder
hydrotrend.initialize(config_file, config_folder)

# The following code chunk is the bulk of the code needed to run HydroTrend
# First create numpy arrays for several important parameters we want to save
# np.empty is declaring space in memory for info to go in
n_days = int(hydrotrend.end_time)
q = np.empty(n_days) # river discharge at the outlet
qs = np.empty(n_days)# sediment load at the outlet
cs = np.empty(n_days) # suspended sediment concentration for different grainsize classes at the outlet
qb = np.empty(n_days) # bedload at the outlet
# Below we have coded up the time loop using i as the index
# We update the model with one timestep at a time, until we reach the end time (specified in input file)
# For each time step we also get the values for the output parameters
for i in range(n_days):
    hydrotrend.update()
    q[i] = hydrotrend.get_value("channel_exit_water__volume_flow_rate")
    qs[i] = hydrotrend.get_value("channel_exit_water_sediment~suspended__mass_flow_rate")
    cs[i] = hydrotrend.get_value("channel_exit_water_sediment~suspended__mass_concentration")
    qb[i] = hydrotrend.get_value("channel_exit_water_sediment~bedload__mass_flow_rate")

# The following code chunks are reshaping the output arrays into useful datasets for post-processing
# Calculate mean annual discharge (30 since model runs for 30 years)
Qw_Reshape = q.reshape(30,365)
Qw_Mean_Rows = np.mean(Qw_Reshape, axis = 1)

# Calculate mean daily discharge
Qw_Reshape = q.reshape(30,365)
Qw_Mean_Cols = np.mean(Qw_Reshape, axis = 0)

# Calculate day of peak Qw
Qw_Max_Index_Col = np.nanargmax(Qw_Mean_Cols, axis=0)

# Calculate mean daily sediment discharge
Qs_Reshape = qs.reshape(30,365)
Qs_Mean_Rows = np.mean(Qs_Reshape, axis = 1)

# Calculate mean daily sediment discharge
Qs_Mean_Cols = np.mean(Qs_Reshape, axis = 0)

# Calculate day of peak Qs
Qs_Max_Index_Col = np.nanargmax(Qs_Mean_Cols, axis=0)

# Write summary statistics to a csv file
import csv
# Field names (headers)
fields = ['Mean Qw', 'Mean Qs', 'Mean SSC', 'Mean Qb', 'Max Qw', 'Max Qs', 'Max SSC', 'Max Qb', 'SD Qw', 'SD Qs', 'SD SSC', 'SD Qb', 'Qw 10 %ile', 'Qs 10 %ile', 'SSC 10 %ile', 'QB 10 %ile', 'Qw 20 %ile', 'Qs 20 %ile', 'SSC 20 %ile', 'QB 20 %ile','Qw 50 %ile', 'Qs 50 %ile', 'SSC 50 %ile', 'QB 50 %ile','Qw 90 %ile', 'Qs 90 %ile', 'SSC 90 %ile', 'QB 90 %ile', 'DOY Peak Qw', 'DOY Peak Qs']
# Calculate statstics for each field
rows = [q.mean(), qs.mean(), cs.mean(), qb.mean(), q.max(), qs.max(), cs.max(), qb.max(), q.std(), qs.std(), cs.std(), qb.std(), np.percentile(q,10), np.percentile(qs,10),np.percentile(cs,10), np.percentile(qb,10), np.percentile(q,20), np.percentile(qs,20),np.percentile(cs,20), np.percentile(qb,20), np.percentile(q,50), np.percentile(qs,50),np.percentile(cs,50), np.percentile(qb,50),np.percentile(q,90), np.percentile(qs,90), np.percentile(cs,90), np.percentile(qb,90), Qw_Max_Index_Col, Qs_Max_Index_Col]
# Direct csv to be saved in relative path location
collections.__file__
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'summ_stats_v3.csv')
# Write summary statistics to csv file
with open(filename, 'w') as csvfile:
    # Creates a csv writer object
    csvwriter = csv.writer(csvfile)
    # Writes the fields
    csvwriter.writerow(fields)
    # Writes the data rows
    csvwriter.writerow(rows)
