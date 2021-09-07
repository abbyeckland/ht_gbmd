# This notebook runs the run_HT function for each basin,
# emission scenario, model, and time period.

# Import numpy and matplotlib
import numpy as np
from numpy import reshape
import os
import collections
import pandas as pd

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

# Initialize the model with the configure file and in the configure folder
hydrotrend.initialize(config_file, config_folder)

# this code declares numpy arrays for several important parameters we want to save.
# empty is declaring space in memory for info to go in
n_days = int(hydrotrend.end_time)
q = np.empty(n_days) # river discharge at the outlet
qs = np.empty(n_days)# sediment load at the outlet
cs = np.empty(n_days) # suspended sediment concentration for different grainsize classes at the outlet
qb = np.empty(n_days) # bedload at the outlet
# here we have coded up the time loop using i as the index
# we update the model with one timestep at the time, untill we reach the end time
# for each time step we also get the values for the output parameters we wish to
for i in range(n_days):
    hydrotrend.update()
    q[i] = hydrotrend.get_value("channel_exit_water__volume_flow_rate")
    qs[i] = hydrotrend.get_value("channel_exit_water_sediment~suspended__mass_flow_rate")
    cs[i] = hydrotrend.get_value("channel_exit_water_sediment~suspended__mass_concentration")
    qb[i] = hydrotrend.get_value("channel_exit_water_sediment~bedload__mass_flow_rate")

# Calculate mean annual discharge
Qw_Reshape = q.reshape(27,365)
Qw_Mean_Rows = np.mean(Qw_Reshape, axis = 1)

# Calculate mean daily discharge
Qw_Reshape = q.reshape(27,365)
Qw_Mean_Cols = np.mean(Qw_Reshape, axis = 0)

# Calculate day of peak Qw
Qw_Max_Index_Col = np.nanargmax(Qw_Mean_Cols, axis=0)

# Calculate mean daily sediment discharge
Qs_Reshape = qs.reshape(27,365)
Qs_Mean_Rows = np.mean(Qs_Reshape, axis = 1)

# Calculate mean daily sediment discharge
Qs_Mean_Cols = np.mean(Qs_Reshape, axis = 0)

# Calculate day of peak Qs
Qs_Max_Index_Col = np.nanargmax(Qs_Mean_Cols, axis=0)

# write summary statistics to a csv file
import csv
# field names
fields = ['Mean Qw', 'Mean Qs', 'Mean SSC', 'Mean Qb', 'Max Qw', 'Max Qs', 'Max SSC', 'Max Qb', 'SD Qw', 'SD Qs', 'SD SSC', 'SD Qb', 'Qw 10 %ile', 'Qs 10 %ile', 'SSC 10 %ile', 'QB 10 %ile', 'Qw 20 %ile', 'Qs 20 %ile', 'SSC 20 %ile', 'QB 20 %ile','Qw 50 %ile', 'Qs 50 %ile', 'SSC 50 %ile', 'QB 50 %ile','Qw 90 %ile', 'Qs 90 %ile', 'SSC 90 %ile', 'QB 90 %ile', 'DOY Peak Qw', 'DOY Peak Qs']
# data rows of csv file
rows = [q.mean(), qs.mean(), cs.mean(), qb.mean(), q.max(), qs.max(), cs.max(), qb.max(), q.std(), qs.std(), cs.std(), qb.std(), np.percentile(q,10), np.percentile(qs,10),np.percentile(cs,10), np.percentile(qb,10), np.percentile(q,20), np.percentile(qs,20),np.percentile(cs,20), np.percentile(qb,20), np.percentile(q,50), np.percentile(qs,50),np.percentile(cs,50), np.percentile(qb,50),np.percentile(q,90), np.percentile(qs,90), np.percentile(cs,90), np.percentile(qb,90), Qw_Max_Index_Col, Qs_Max_Index_Col]
# Point to relative path
collections.__file__
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'summ_stats_v3.csv')
# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(fields)
    # writing the data rows
    csvwriter.writerow(rows)

# Reference scenario only

# read in CSV with recent data from Bahadurabad Bridge
Baha_csv = pd.read_csv('/Users/aeckland/hydrotrend_gbmd/water_data/Brahmaputra/Baha_Qw_1976-2006.csv')

# create panda array from date and discharge columns
Date_Baha_csv = Baha_csv['Date']
Qw_Baha_csv = Baha_csv['Discharge (m3/s)']
Date_Baha_csv = [pd.to_datetime(d) for d in Date_Baha_csv]
Date_Baha = np.array(Date_Baha_csv)
Qw_Baha = np.array(Qw_Baha_csv)

# Create pandas dataframe
Baha_df = pd.DataFrame(Qw_Baha, Date_Baha)
Baha_df.columns = ['Discharge (m3/s)']

# Calculate observed* sediment discharge
# Brahmaputra Q-Qs relationship (1989-1994): Qs = 0.005*Q^1.56; R2 = 0.78 (Higgens et al., 2018)
Qs_Baha = (Qw_Baha**1.56)*0.005

# Calculate and plot mean annual flow (observed vs simulated)
# Calculate observed
Qw_Reshape_Obs = Qw_Baha.reshape(27,365)
Qw_Mean_Rows_Obs = np.mean(Qw_Reshape_Obs, axis = 1)

# Calculate simulated
Qw_Reshape_Sim = q.reshape(27,365)
Qw_Mean_Rows_Sim = np.mean(Qw_Reshape_Sim, axis = 1)

# Calculate mean daily discharge over simulation time period (observed vs simulated)
# calculate observed
Qw_Reshape_Obs = Qw_Baha.reshape(27,365)
Qw_Mean_Cols_Obs = np.mean(Qw_Reshape_Obs, axis = 0)

# Calculate simulated
Qw_Daily = np.mean(Qw_Reshape_Sim, axis = 0)

# Calculate mean daily discharge over simulation time period (observed vs simulated)
# Calculate observed
Qs_Reshape_Obs = Qs_Baha.reshape(27,365)
Qs_Mean_Rows_Obs = np.mean(Qs_Reshape_Obs, axis = 1)

# Calculate simulated
Qs_Reshape_Sim = qs.reshape(27,365)
Qs_Mean_Rows_Sim = np.mean(Qs_Reshape_Sim, axis = 1)

# Calculate mean daily sediment discharge over simulation time period (observed vs simulated)
# Calculate observed
Qs_Mean_Cols_Obs = np.mean(Qs_Reshape_Obs, axis = 0)

# Calculate simulated
Qs_Daily = np.mean(Qs_Reshape_Sim, axis = 0)

# compare observed and simulated max water discharge statistics
Qw_Max_Index_Col_Obs = np.nanargmax(Qw_Mean_Cols_Obs, axis=0)
Qw_Max_Index_Col_Sim = np.nanargmax(Qw_Daily, axis=0)

# compare observed and simulated max water discharge statistics
Qs_Max_Index_Col_Obs = np.nanargmax(Qs_Mean_Cols_Obs, axis=0)
Qs_Max_Index_Col_Sim = np.nanargmax(Qs_Daily, axis=0)

# write summary statistics to a csv file
import csv
# field names
fields = ['Mean Obs Qw', 'Mean Sim Qw', '% Error', 'Mean Obs Qs', 'Mean Sim Qs', '% Error', 'Max Obs Qw', 'Max Sim Qw', '% Error', 'Day Peak Qw Obs', 'Day Peak Qw Sim', 'Max Obs Qs', 'Max Sim Qs', '% Error', 'Day Peak Qs Obs', 'Day Peak Qs Sim', 'CC Qw', 'Cov Qw', 'CC Qs', 'Cov Qs', 'Std Qw Obs', 'Std Qs Obs',]
# data rows of csv file
rows = [np.nanmean(Qw_Baha), q.mean(), (((np.nanmean(Qw_Baha)-q.mean())/np.nanmean(Qw_Baha))*100), np.nanmean(Qs_Baha), qs.mean(), (((np.nanmean(Qs_Baha)-qs.mean())/np.nanmean(Qs_Baha))*100), np.nanmax(Qw_Mean_Cols_Obs), Qw_Daily.max(), ((np.nanmax(Qw_Mean_Cols_Obs)-Qw_Daily.max())/np.nanmax(Qw_Mean_Cols_Obs)*100), Qw_Max_Index_Col_Obs, Qw_Max_Index_Col_Sim, np.nanmax(Qs_Mean_Cols_Obs), Qs_Daily.max(), ((np.nanmax(Qs_Mean_Cols_Obs)-Qs_Daily.max())/np.nanmax(Qs_Mean_Cols_Obs)*100), Qs_Max_Index_Col_Obs, Qs_Max_Index_Col_Sim, np.corrcoef(Qw_Baha, q), np.cov(Qw_Baha, q), np.corrcoef(Qs_Baha, q), np.cov(Qs_Baha, q), np.nanstd(Qw_Baha), np.nanstd(Qs_Baha)]
# Point to relative path
collections.__file__
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'REF_summ_stats_v2.csv')
# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(fields)
    # writing the data rows
    csvwriter.writerow(rows)
