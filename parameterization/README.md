This folder contains lithology data for the brahmaputra and ganges basins to determine an L-value for calibration of the HydroTrend model.

There are two notebooks located in this folder:
- lithology_brahma.ipynb
- lithology_ganges.ipynb

In general terms, these notebooks read in text files with lithology data as pandas dataframes. The total area is computed and checked. Unique id's indicating lithologic type are given an l-factor, or a weight, prescribed by Syvitski and Milliman, 2007. Finally, a weighted average is computed to calculate an L-factor, or average lithologic type, used as input into HydroTrend.

- For the brahmaputra basin, the l-factor is: 1.684
- For the ganges basin, the l-factor is: 1.506 