This folder contains recently aquired sediment concentration data from IWM corresponding with water discharge values. 

Within the ***run_2*** folder, there contains 2 jupyter notebooks:
- BR_sedcal.ipynb
- GR_sedcal.ipynb

The purpose of these two notebooks are to import the newly collected water discharge and sediment concentration data, visualize the data, and create a sediment rating curve for the new, observed dataset.

Then, sediment rating curves are generated from the simulated (HydroTrend) data, using Qw and Qs outputs to generate a power law relationship. Two sets of rating curves are generated in both notebooks:
1. HydroTrend rating curves over the reference (historic) time period
2. HydroTrend rating curves over the recent (2020) time period

These rating curves are plotted with additional rating curves, including the newly generated rating curve from the newly aquired observed data (as mentioned above), as well as historic rating curves generated around ~1980 (see Higgins et. al., 2018 paper for reference on these historic curves). The goal is to see how the simulated rating curves compare with rating curves generated based on observed data. This is best practice to ensure the model is calibrated correctly to real-world conditions.

Finally, sediment discharge values are computed a variety of different ways to aid in the sediment validation process. Simulated sediment discharge values are compared with observed values, from both the reference time period and the recent time period.

The ***sed_data*** folder contains the raw water discharge and ssc data in the form of a text file with the associated date of data collection. 