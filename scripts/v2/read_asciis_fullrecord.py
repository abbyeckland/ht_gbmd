# Import python packages
import pandas as pd
import numpy as np
import os
import collections

# This notebook is similar to read_asciis_v2.py,
# but it imports reference scenario data in addition to projected data,
# giving a full 120 year record

## This notebook will read in one output variable at a time. The first is water discharge (Qw).

# Assign text file path for a specific climate model and output variable
collections.__file__
dirname = os.path.dirname(__file__)

Qw_2020_path = os.path.join(dirname,'2020/Hydrotrend/HYDROASCII.Q')
Qw_2040_path = os.path.join(dirname,'2040/Hydrotrend/HYDROASCII.Q')
Qw_2060_path = os.path.join(dirname,'2060/Hydrotrend/HYDROASCII.Q')
Qw_2080_path = os.path.join(dirname,'2080/Hydrotrend/HYDROASCII.Q')

# Read csvs
Qw_2020_df = pd.read_csv(Qw_2020_path)
Qw_2040_df = pd.read_csv(Qw_2040_path)
Qw_2060_df = pd.read_csv(Qw_2060_path)
Qw_2080_df = pd.read_csv(Qw_2080_path)

# Create panda dataframe from csvs
Qw_2020 = pd.DataFrame(Qw_2020_df)
Qw_2040 = pd.DataFrame(Qw_2040_df)
Qw_2060 = pd.DataFrame(Qw_2060_df)
Qw_2080 = pd.DataFrame(Qw_2080_df)

# Print as one single record and create new dataframe, ensuring no time overlap
Qw_all = pd.concat([Qw_2020[1:7301], Qw_2040[1:7301], Qw_2060[1:7301], Qw_2080[1:]])
Qw_all_df = pd.DataFrame(Qw_all)
Qw_all_df.columns = ['Qw(m3/s)']

# Add the next ascii file output to the same dataframe: Sediment Discharge (Qs)
# Assign text file path for a specific climate model and output variable
Qs_2020_path = os.path.join(dirname,'2020/Hydrotrend/HYDROASCII.QS')
Qs_2040_path = os.path.join(dirname,'2040/Hydrotrend/HYDROASCII.QS')
Qs_2060_path = os.path.join(dirname,'2060/Hydrotrend/HYDROASCII.QS')
Qs_2080_path = os.path.join(dirname,'2080/Hydrotrend/HYDROASCII.QS')

# Read csvs
Qs_2020_df = pd.read_csv(Qs_2020_path)
Qs_2040_df = pd.read_csv(Qs_2040_path)
Qs_2060_df = pd.read_csv(Qs_2060_path)
Qs_2080_df = pd.read_csv(Qs_2080_path)

# Create panda dataframe from csvs
Qs_2020 = pd.DataFrame(Qs_2020_df)
Qs_2040 = pd.DataFrame(Qs_2040_df)
Qs_2060 = pd.DataFrame(Qs_2060_df)
Qs_2080 = pd.DataFrame(Qs_2080_df)

# Print as a single record and create new dataframe
Qs_all = pd.concat([Qs_2020[1:7301], Qs_2040[1:7301], Qs_2060[1:7301], Qs_2080[1:]])
Qs_all_df = pd.DataFrame(Qs_all)
Qs_all_df.columns = ['Qs(kg/s)']

# Do quick visual check of the record to see if concat argument worked
Qw_all_df = Qw_all_df.astype(float)
Qs_all_df = Qs_all_df.astype(float)

#merge two existing dataframes (horizontal stack)
Qw_all_df = Qw_all_df.reset_index()
Qs_all_df = Qs_all_df.reset_index()
Qw_Qs_merge = pd.concat([Qw_all_df, Qs_all_df], ignore_index=False, axis=1)

# Next ascii file output: Bedload discharge (Qb)
# Assign text file path for a specific climate model and output variable
Qb_2020_path = os.path.join(dirname,'2020/Hydrotrend/HYDROASCII.QB')
Qb_2040_path = os.path.join(dirname,'2040/Hydrotrend/HYDROASCII.QB')
Qb_2060_path = os.path.join(dirname,'2060/Hydrotrend/HYDROASCII.QB')
Qb_2080_path = os.path.join(dirname,'2080/Hydrotrend/HYDROASCII.QB')

# Read csvs
Qb_2020_df = pd.read_csv(Qb_2020_path)
Qb_2040_df = pd.read_csv(Qb_2040_path)
Qb_2060_df = pd.read_csv(Qb_2060_path)
Qb_2080_df = pd.read_csv(Qb_2080_path)

# Create panda dataframes from  csvs
Qb_2020 = pd.DataFrame(Qb_2020_df)
Qb_2040 = pd.DataFrame(Qb_2040_df)
Qb_2060 = pd.DataFrame(Qb_2060_df)
Qb_2080 = pd.DataFrame(Qb_2080_df)

# Print as a single record and create new dataframe
Qb_all = pd.concat([Qb_2020[1:7301], Qb_2040[1:7301], Qb_2060[1:7301], Qb_2080[1:]])
Qb_all_df = pd.DataFrame(Qb_all)
Qb_all_df.columns = ['Qb(kg/s)']

# Merge with existing dataframe
Qb_all_df = Qb_all_df.reset_index()
Qw_Qs_Qb_merge = pd.concat([Qw_all_df, Qs_all_df, Qb_all_df], ignore_index=False, axis=1)

# Next ascii file output: Suspended sediment concentration (Cs). This dataset has four columns
# Assign text file path for a specific climate model and output variable
Cs_2020_path = os.path.join(dirname,'2020/Hydrotrend/HYDROASCII.CS')
Cs_2040_path = os.path.join(dirname,'2040/Hydrotrend/HYDROASCII.CS')
Cs_2060_path = os.path.join(dirname,'2060/Hydrotrend/HYDROASCII.CS')
Cs_2080_path = os.path.join(dirname,'2080/Hydrotrend/HYDROASCII.CS')

# Read csvs
Cs_2020_df = pd.read_csv(Cs_2020_path)
Cs_2040_df = pd.read_csv(Cs_2040_path)
Cs_2060_df = pd.read_csv(Cs_2060_path)
Cs_2080_df = pd.read_csv(Cs_2080_path)

# Create panda dataframes from  csvs
Cs_2020 = pd.DataFrame(Cs_2020_df)
Cs_2020.columns = ['CsBin1']
Cs_2040 = pd.DataFrame(Cs_2040_df)
Cs_2040.columns = ['CsBin1']
Cs_2060 = pd.DataFrame(Cs_2060_df)
Cs_2060.columns = ['CsBin1']
Cs_2080 = pd.DataFrame(Cs_2080_df)
Cs_2080.columns = ['CsBin1']

# Split single column of data into four columns and assign headers for 2020
Cs_2020 = Cs_2020.reset_index()
Cs_2020_split = Cs_2020["CsBin1"].str.split(" ", n = 3, expand = True)
Cs_2020_split.columns = ["CsBin1", "CsBin2","CsBin3", "CsBin4"]

# Split single column of data into four columns and assign headers for 2040
Cs_2040 = Cs_2040.reset_index()
Cs_2040_split = Cs_2040["CsBin1"].str.split(" ", n = 3, expand = True)
Cs_2040_split.columns = ["CsBin1", "CsBin2","CsBin3", "CsBin4"]

# Split single column of data into four columns and assign headers for 2060
Cs_2060 = Cs_2060.reset_index()
Cs_2060_split = Cs_2060["CsBin1"].str.split(" ", n = 3, expand = True)
Cs_2060_split.columns = ["CsBin1", "CsBin2","CsBin3", "CsBin4"]

# Split single column of data into four columns and assign headers for 2080
Cs_2080 = Cs_2080.reset_index()
Cs_2080_split = Cs_2080["CsBin1"].str.split(" ", n = 3, expand = True)
Cs_2080_split.columns = ["CsBin1", "CsBin2","CsBin3", "CsBin4"]

# Print as a single record and create new dataframe
Cs_all = pd.concat([Cs_2020_split[1:7301], Cs_2040_split[1:7301], Cs_2060_split[1:7301], Cs_2080_split[1:]])
Cs_all_df = pd.DataFrame(Cs_all)
Cs_all_df.columns = ["CsBin 1", "CsBin2", "CsBin3", "CsBin4"]

# Merge with existing dataframe
Cs_all_df = Cs_all_df.reset_index()
Qw_Qs_Qb_Cs_merge = pd.concat([Qw_all_df, Qs_all_df, Qb_all_df, Cs_all_df], ignore_index=False, axis=1)

# Next ascii file output: Velocity, width, depth (VWD).
# Assign text file path for a specific climate model and output variable
VWD_2020_path = os.path.join(dirname,'2020/Hydrotrend/HYDROASCII.VWD')
VWD_2040_path = os.path.join(dirname,'2040/Hydrotrend/HYDROASCII.VWD')
VWD_2060_path = os.path.join(dirname,'2060/Hydrotrend/HYDROASCII.VWD')
VWD_2080_path = os.path.join(dirname,'2080/Hydrotrend/HYDROASCII.VWD')

# Read csvs
VWD_2020_df = pd.read_csv(VWD_2020_path)
VWD_2040_df = pd.read_csv(VWD_2040_path)
VWD_2060_df = pd.read_csv(VWD_2060_path)
VWD_2080_df = pd.read_csv(VWD_2080_path)

# Create panda dataframes from  csvs
VWD_2020 = pd.DataFrame(VWD_2020_df)
VWD_2020.columns = ['vel(m/s)']
VWD_2040 = pd.DataFrame(VWD_2040_df)
VWD_2040.columns = ['vel(m/s)']
VWD_2060 = pd.DataFrame(VWD_2060_df)
VWD_2060.columns = ['vel(m/s)']
VWD_2080 = pd.DataFrame(VWD_2080_df)
VWD_2080.columns = ['vel(m/s)']

# Split single column of data into three columns and assign headers for 2020
VWD_2020 = VWD_2020.reset_index()
VWD_2020_split = VWD_2020["vel(m/s)"].str.split("\t", n = 2, expand = True)
VWD_2020_split.columns = ["vel(m/s)", "wid(m)","dep(m)"]
VWD_2020_split["dep(m)"] = VWD_2020_split["dep(m)"].str.replace('\t', '')

# Split single column of data into three columns and assign headers for 2040
VWD_2040 = VWD_2040.reset_index()
VWD_2040_split = VWD_2040["vel(m/s)"].str.split("\t", n = 2, expand = True)
VWD_2040_split.columns = ["vel(m/s)", "wid(m)","dep(m)"]
VWD_2040_split["dep(m)"] = VWD_2040_split["dep(m)"].str.replace('\t', '')

# Split single column of data into three columns and assign headers for 2060
VWD_2060 = VWD_2060.reset_index()
VWD_2060_split = VWD_2060["vel(m/s)"].str.split("\t", n = 2, expand = True)
VWD_2060_split.columns = ["vel(m/s)", "wid(m)","dep(m)"]
VWD_2060_split["dep(m)"] = VWD_2060_split["dep(m)"].str.replace('\t', '')

# Split single column of data into three columns and assign headers for 2080
VWD_2080 = VWD_2080.reset_index()
VWD_2080_split = VWD_2080["vel(m/s)"].str.split("\t", n = 2, expand = True)
VWD_2080_split.columns = ["vel(m/s)", "wid(m)","dep(m)"]
VWD_2080_split["dep(m)"] = VWD_2080_split["dep(m)"].str.replace('\t', '')

# Print as a single record and create new dataframe
VWD_all = pd.concat([VWD_2020_split[1:7301], VWD_2040_split[1:7301], VWD_2060_split[1:7301], VWD_2080_split[1:]])
VWD_all_df = pd.DataFrame(VWD_all)
VWD_all_df.columns = ["vel(m/s)", "wid(m)", "dep(m)"]

# Merge with existing dataframe
VWD_all_df = VWD_all_df.reset_index()
Qw_Qs_Qb_Cs_VWD_merge = pd.concat([Qw_all_df, Qs_all_df, Qb_all_df, Cs_all_df, VWD_all_df], ignore_index=False, axis=1)

# Next and last dataset: Temperature and precipitation (TP).
# Assign text file path for a specific climate model and output variable
TP_2020_path = os.path.join(dirname,'2020/Hydrotrend/HYDROASCII.TEMP_PREC')
TP_2040_path = os.path.join(dirname,'2040/Hydrotrend/HYDROASCII.TEMP_PREC')
TP_2060_path = os.path.join(dirname,'2060/Hydrotrend/HYDROASCII.TEMP_PREC')
TP_2080_path = os.path.join(dirname,'2080/Hydrotrend/HYDROASCII.TEMP_PREC')

# Read csvs
TP_2020_df = pd.read_csv(TP_2020_path)
TP_2040_df = pd.read_csv(TP_2040_path)
TP_2060_df = pd.read_csv(TP_2060_path)
TP_2080_df = pd.read_csv(TP_2080_path)

# Create panda dataframes from  csvs
TP_2020 = pd.DataFrame(TP_2020_df)
TP_2020.columns = ['temp(deg.C)']
TP_2040 = pd.DataFrame(TP_2040_df)
TP_2040.columns = ['temp(deg.C)']
TP_2060 = pd.DataFrame(TP_2060_df)
TP_2060.columns = ['temp(deg.C)']
TP_2080 = pd.DataFrame(TP_2080_df)
TP_2080.columns = ['temp(deg.C)']

# Split single column of data into two columns and assign headers for 2020
TP_2020 = TP_2020.reset_index()
TP_2020_split = TP_2020["temp(deg.C)"].str.split("\t", n = 1, expand = True)
TP_2020_split.columns = ["temp(deg.C)", "prec(m)"]
TP_2020_split["prec(m)"] = TP_2020_split["prec(m)"].str.replace('\t', '')

# Split single column of data into two columns and assign headers for 2040
TP_2040 = TP_2040.reset_index()
TP_2040_split = TP_2040["temp(deg.C)"].str.split("\t", n = 1, expand = True)
TP_2040_split.columns = ["temp(deg.C)", "prec(m)"]
TP_2040_split["prec(m)"] = TP_2040_split["prec(m)"].str.replace('\t', '')

# Split single column of data into two columns and assign headers for 2060
TP_2060 = TP_2060.reset_index()
TP_2060_split = TP_2060["temp(deg.C)"].str.split("\t", n = 1, expand = True)
TP_2060_split.columns = ["temp(deg.C)", "prec(m)"]
TP_2060_split["prec(m)"] = TP_2060_split["prec(m)"].str.replace('\t', '')

# Split single column of data into two columns and assign headers for 2080
TP_2080 = TP_2080.reset_index()
TP_2080_split = TP_2080["temp(deg.C)"].str.split("\t", n = 1, expand = True)
TP_2080_split.columns = ["temp(deg.C)", "prec(m)"]
TP_2080_split["prec(m)"] = TP_2080_split["prec(m)"].str.replace('\t', '')

# Print as a single record and create new dataframe
TP_all = pd.concat([TP_2020_split[1:7301], TP_2040_split[1:7301], TP_2060_split[1:7301], TP_2080_split[1:]])
TP_all_df = pd.DataFrame(TP_all)
TP_all_df.columns = ["temp(deg.C)", "prec(m)"]

# Merge with existing dataframe
TP_all_df = TP_all_df.reset_index()
Qw_Qs_Qb_Cs_VWD_TP_merge = pd.concat([Qw_all_df, Qs_all_df, Qb_all_df, Cs_all_df, VWD_all_df, TP_all_df], ignore_index=False, axis=1)

# Save to csv
Qw_Qs_Qb_Cs_VWD_TP_merge.to_csv(os.path.join(dirname, 'ASCII_data.csv'))

# Now import reference scenario data. We will append this data to the beginning of the
# concatenated arrays

Qw_ref_path_gfdl = pd.read_csv('../../reference/GFDL-ESM2M/Hydrotrend/HYDROASCII.Q')
Qs_ref_path_gfdl = os.path.join('../../reference/GFDL-ESM2M/Hydrotrend/HYDROASCII.QS')
Qb_ref_path_gfdl = os.path.join('../../reference/GFDL-ESM2M/Hydrotrend/HYDROASCII.QB')
Cs_ref_path_gfdl = os.path.join('../../reference/GFDL-ESM2M/Hydrotrend/HYDROASCII.CS')
VWD_ref_path_gfdl = os.path.join('../../reference/GFDL-ESM2M/Hydrotrend/HYDROASCII.VWD')
TP_ref_path_gfdl = os.path.join('../../reference/GFDL-ESM2M/Hydrotrend/HYDROASCII.TEMP_PREC')

Qw_ref_path_hadgem = pd.read_csv('../../reference/HadGEM2/Hydrotrend/HYDROASCII.Q')
Qs_ref_path_hadgem = os.path.join('../../reference/HadGEM2/Hydrotrend/HYDROASCII.QS')
Qb_ref_path_hadgem = os.path.join('../../reference/HadGEM2/Hydrotrend/HYDROASCII.QB')
Cs_ref_path_hadgem = os.path.join('../../reference/HadGEM2/Hydrotrend/HYDROASCII.CS')
VWD_ref_path_hadgem = os.path.join('../../reference/HadGEM2/Hydrotrend/HYDROASCII.VWD')
TP_ref_path_hadgem = os.path.join('../../reference/HadGEM2/Hydrotrend/HYDROASCII.TEMP_PREC')

Qw_ref_path_ipsl = pd.read_csv('../../reference/IPSL_CM5A/Hydrotrend/HYDROASCII.Q')
Qs_ref_path_ipsl = os.path.join('../../reference/IPSL_CM5A/Hydrotrend/HYDROASCII.QS')
Qb_ref_path_ipsl = os.path.join('../../reference/IPSL_CM5A/Hydrotrend/HYDROASCII.QB')
Cs_ref_path_ipsl = os.path.join('../../reference/IPSL_CM5A/Hydrotrend/HYDROASCII.CS')
VWD_ref_path_ipsl = os.path.join('../../reference/IPSL_CM5A/Hydrotrend/HYDROASCII.VWD')
TP_ref_path_ipsl = os.path.join('../../reference/IPSL_CM5A/Hydrotrend/HYDROASCII.TEMP_PREC')

Qw_ref_path_miroc = pd.read_csv('../../reference/MIROC-ESM-CHEM/Hydrotrend/HYDROASCII.Q')
Qs_ref_path_miroc = os.path.join('../../reference/MIROC-ESM-CHEM/Hydrotrend/HYDROASCII.QS')
Qb_ref_path_miroc = os.path.join('../../reference/MIROC-ESM-CHEM/Hydrotrend/HYDROASCII.QB')
Cs_ref_path_miroc = os.path.join('../../reference/MIROC-ESM-CHEM/Hydrotrend/HYDROASCII.CS')
VWD_ref_path_miroc = os.path.join('../../reference/MIROC-ESM-CHEM/Hydrotrend/HYDROASCII.VWD')
TP_ref_path_miroc = os.path.join('../../reference/MIROC-ESM-CHEM/Hydrotrend/HYDROASCII.TEMP_PREC')

Qw_ref_path_noresm = pd.read_csv('../../reference/NORESM-M/Hydrotrend/HYDROASCII.Q')
Qs_ref_path_noresm = os.path.join('../../reference/NORESM-M/Hydrotrend/HYDROASCII.QS')
Qb_ref_path_noresm = os.path.join('../../reference/NORESM-M/Hydrotrend/HYDROASCII.QB')
Cs_ref_path_noresm = os.path.join('../../reference/NORESM-M/Hydrotrend/HYDROASCII.CS')
VWD_ref_path_noresm = os.path.join('../../reference/NORESM-M/Hydrotrend/HYDROASCII.VWD')
TP_ref_path_noresm = os.path.join('../../reference/NORESM-M/Hydrotrend/HYDROASCII.TEMP_PREC')

# Prepare the dataset like done in the above steps
# GFDL
Qw_ref_df_gfdl = pd.DataFrame(Qw_ref_path_gfdl)
Qw_ref_df_gfdl.columns = ['Qw(m3/s)']
Qs_ref_df_gfdl = pd.DataFrame(Qs_ref_path_gfdl)
Qs_ref_df_gfdl.columns = ['Qs(kg/s)']
Qb_ref_df_gfdl = pd.DataFrame(Qb_ref_path_gfdl)
Qb_ref_df_gfdl.columns = ['Qb(kg/s)']
Cs_ref_df_gfdl = pd.DataFrame(Cs_ref_path_gfdl)
Cs_ref_df_gfdl.columns = ['CsBin1']
Cs_ref_df_gfdl = Cs_ref_df_gfdl.reset_index()
Cs_ref_df_gfdl_split = Cs_ref_df_gfdl["CsBin1"].str.split(" ", n = 3, expand = True)
Cs_ref_df_gfdl_split.columns = ["CsBin1", "CsBin2","CsBin3", "CsBin4"]
VWD_ref_df_gfdl = pd.DataFrame(VWD_ref_path_gfdl)
VWD_ref_df_gfdl.columns = ['vel(m/s)']
VWD_ref_df_gfdl = VWD_ref_df_gfdl.reset_index()
VWD_ref_df_gfdl_split = VWD_ref_df_gfdl["vel(m/s)"].str.split("\t", n = 2, expand = True)
VWD_ref_df_gfdl_split.columns = ["vel(m/s)", "wid(m)","dep(m)"]
VWD_ref_df_gfdl_split["dep(m)"] = VWD_ref_df_gfdl_split["dep(m)"].str.replace('\t', '')
TP_ref_df_gfdl = pd.DataFrame(TP_ref_path_gfdl)
TP_ref_df_gfdl.columns = ['temp(deg.C)']
TP_ref_df_gfdl = TP_ref_df_gfdl.reset_index()
TP_ref_df_gfdl_split = TP_ref_df_gfdl["temp(deg.C)"].str.split("\t", n = 1, expand = True)
TP_ref_df_gfdl_split.columns = ["temp(deg.C)", "prec(m)"]
TP_ref_df_gfdl_split["prec(m)"] = TP_ref_df_gfdl_split["prec(m)"].str.replace('\t', '')
# HadGEM2
Qw_ref_df_hadgem = pd.DataFrame(Qw_ref_path_hadgem)
Qw_ref_df_hadgem.columns = ['Qw(m3/s)']
Qs_ref_df_hadgem = pd.DataFrame(Qs_ref_path_hadgem)
Qs_ref_df_hadgem.columns = ['Qs(kg/s)']
Qb_ref_df_hadgem = pd.DataFrame(Qb_ref_path_hadgem)
Qb_ref_df_hadgem.columns = ['Qb(kg/s)']
Cs_ref_df_hadgem = pd.DataFrame(Cs_ref_path_hadgem)
Cs_ref_df_hadgem.columns = ['CsBin1']
Cs_ref_df_hadgem = Cs_ref_df_hadgem.reset_index()
Cs_ref_df_hadgem_split = Cs_ref_df_hadgem["CsBin1"].str.split(" ", n = 3, expand = True)
Cs_ref_df_hadgem_split.columns = ["CsBin1", "CsBin2","CsBin3", "CsBin4"]
VWD_ref_df_hadgem = pd.DataFrame(VWD_ref_path_hadgem)
VWD_ref_df_hadgem.columns = ['vel(m/s)']
VWD_ref_df_hadgem = VWD_ref_df_hadgem.reset_index()
VWD_ref_df_hadgem_split = VWD_ref_df_hadgem["vel(m/s)"].str.split("\t", n = 2, expand = True)
VWD_ref_df_hadgem_split.columns = ["vel(m/s)", "wid(m)","dep(m)"]
VWD_ref_df_hadgem_split["dep(m)"] = VWD_ref_df_hadgem_split["dep(m)"].str.replace('\t', '')
TP_ref_df_hadgem = pd.DataFrame(TP_ref_path_hadgem)
TP_ref_df_hadgem.columns = ['temp(deg.C)']
TP_ref_df_hadgem = TP_ref_df_hadgem.reset_index()
TP_ref_df_hadgem_split = TP_ref_df_hadgem["temp(deg.C)"].str.split("\t", n = 1, expand = True)
TP_ref_df_hadgem_split.columns = ["temp(deg.C)", "prec(m)"]
TP_ref_df_hadgem_split["prec(m)"] = TP_ref_df_hadgem_split["prec(m)"].str.replace('\t', '')
# IPSL
Qw_ref_df_ipsl = pd.DataFrame(Qw_ref_path_ipsl)
Qw_ref_df_ipsl.columns = ['Qw(m3/s)']
Qs_ref_df_ipsl = pd.DataFrame(Qs_ref_path_ipsl)
Qs_ref_df_ipsl.columns = ['Qs(kg/s)']
Qb_ref_df_ipsl = pd.DataFrame(Qb_ref_path_ipsl)
Qb_ref_df_ipsl.columns = ['Qb(kg/s)']
Cs_ref_df_ipsl = pd.DataFrame(Cs_ref_path_ipsl)
Cs_ref_df_ipsl.columns = ['CsBin1']
Cs_ref_df_ipsl = Cs_ref_df_ipsl.reset_index()
Cs_ref_df_ipsl_split = Cs_ref_df_ipsl["CsBin1"].str.split(" ", n = 3, expand = True)
Cs_ref_df_ipsl_split.columns = ["CsBin1", "CsBin2","CsBin3", "CsBin4"]
VWD_ref_df_ipsl = pd.DataFrame(VWD_ref_path_ipsl)
VWD_ref_df_ipsl.columns = ['vel(m/s)']
VWD_ref_df_ipsl = VWD_ref_df_ipsl.reset_index()
VWD_ref_df_ipsl_split = VWD_ref_df_ipsl["vel(m/s)"].str.split("\t", n = 2, expand = True)
VWD_ref_df_ipsl_split.columns = ["vel(m/s)", "wid(m)","dep(m)"]
VWD_ref_df_ipsl_split["dep(m)"] = VWD_ref_df_ipsl_split["dep(m)"].str.replace('\t', '')
TP_ref_df_ipsl = pd.DataFrame(TP_ref_path_ipsl)
TP_ref_df_ipsl.columns = ['temp(deg.C)']
TP_ref_df_ipsl = TP_ref_df_ipsl.reset_index()
TP_ref_df_ipsl_split = TP_ref_df_ipsl["temp(deg.C)"].str.split("\t", n = 1, expand = True)
TP_ref_df_ipsl_split.columns = ["temp(deg.C)", "prec(m)"]
TP_ref_df_ipsl_split["prec(m)"] = TP_ref_df_ipsl_split["prec(m)"].str.replace('\t', '')
# IPSL
Qw_ref_df_ipsl = pd.DataFrame(Qw_ref_path_ipsl)
Qw_ref_df_ipsl.columns = ['Qw(m3/s)']
Qs_ref_df_ipsl = pd.DataFrame(Qs_ref_path_ipsl)
Qs_ref_df_ipsl.columns = ['Qs(kg/s)']
Qb_ref_df_ipsl = pd.DataFrame(Qb_ref_path_ipsl)
Qb_ref_df_ipsl.columns = ['Qb(kg/s)']
Cs_ref_df_ipsl = pd.DataFrame(Cs_ref_path_ipsl)
Cs_ref_df_ipsl.columns = ['CsBin1']
Cs_ref_df_ipsl = Cs_ref_df_ipsl.reset_index()
Cs_ref_df_ipsl_split = Cs_ref_df_ipsl["CsBin1"].str.split(" ", n = 3, expand = True)
Cs_ref_df_ipsl_split.columns = ["CsBin1", "CsBin2","CsBin3", "CsBin4"]
VWD_ref_df_ipsl = pd.DataFrame(VWD_ref_path_ipsl)
VWD_ref_df_ipsl.columns = ['vel(m/s)']
VWD_ref_df_ipsl = VWD_ref_df_ipsl.reset_index()
VWD_ref_df_ipsl_split = VWD_ref_df_ipsl["vel(m/s)"].str.split("\t", n = 2, expand = True)
VWD_ref_df_ipsl_split.columns = ["vel(m/s)", "wid(m)","dep(m)"]
VWD_ref_df_ipsl_split["dep(m)"] = VWD_ref_df_ipsl_split["dep(m)"].str.replace('\t', '')
TP_ref_df_ipsl = pd.DataFrame(TP_ref_path_ipsl)
TP_ref_df_ipsl.columns = ['temp(deg.C)']
TP_ref_df_ipsl = TP_ref_df_ipsl.reset_index()
TP_ref_df_ipsl_split = TP_ref_df_ipsl["temp(deg.C)"].str.split("\t", n = 1, expand = True)
TP_ref_df_ipsl_split.columns = ["temp(deg.C)", "prec(m)"]
TP_ref_df_ipsl_split["prec(m)"] = TP_ref_df_ipsl_split["prec(m)"].str.replace('\t', '')
# MIROC
Qw_ref_df_miroc = pd.DataFrame(Qw_ref_path_miroc)
Qw_ref_df_miroc.columns = ['Qw(m3/s)']
Qs_ref_df_miroc = pd.DataFrame(Qs_ref_path_miroc)
Qs_ref_df_miroc.columns = ['Qs(kg/s)']
Qb_ref_df_miroc = pd.DataFrame(Qb_ref_path_miroc)
Qb_ref_df_miroc.columns = ['Qb(kg/s)']
Cs_ref_df_miroc = pd.DataFrame(Cs_ref_path_miroc)
Cs_ref_df_miroc.columns = ['CsBin1']
Cs_ref_df_miroc = Cs_ref_df_miroc.reset_index()
Cs_ref_df_miroc_split = Cs_ref_df_miroc["CsBin1"].str.split(" ", n = 3, expand = True)
Cs_ref_df_miroc_split.columns = ["CsBin1", "CsBin2","CsBin3", "CsBin4"]
VWD_ref_df_miroc = pd.DataFrame(VWD_ref_path_miroc)
VWD_ref_df_miroc.columns = ['vel(m/s)']
VWD_ref_df_miroc = VWD_ref_df_miroc.reset_index()
VWD_ref_df_miroc_split = VWD_ref_df_miroc["vel(m/s)"].str.split("\t", n = 2, expand = True)
VWD_ref_df_miroc_split.columns = ["vel(m/s)", "wid(m)","dep(m)"]
VWD_ref_df_miroc_split["dep(m)"] = VWD_ref_df_miroc_split["dep(m)"].str.replace('\t', '')
TP_ref_df_miroc = pd.DataFrame(TP_ref_path_miroc)
TP_ref_df_miroc.columns = ['temp(deg.C)']
TP_ref_df_miroc = TP_ref_df_miroc.reset_index()
TP_ref_df_miroc_split = TP_ref_df_miroc["temp(deg.C)"].str.split("\t", n = 1, expand = True)
TP_ref_df_miroc_split.columns = ["temp(deg.C)", "prec(m)"]
TP_ref_df_miroc_split["prec(m)"] = TP_ref_df_miroc_split["prec(m)"].str.replace('\t', '')
# NORESM
Qw_ref_df_noresm = pd.DataFrame(Qw_ref_path_noresm)
Qw_ref_df_noresm.columns = ['Qw(m3/s)']
Qs_ref_df_noresm = pd.DataFrame(Qs_ref_path_noresm)
Qs_ref_df_noresm.columns = ['Qs(kg/s)']
Qb_ref_df_noresm = pd.DataFrame(Qb_ref_path_noresm)
Qb_ref_df_noresm.columns = ['Qb(kg/s)']
Cs_ref_df_noresm = pd.DataFrame(Cs_ref_path_noresm)
Cs_ref_df_noresm.columns = ['CsBin1']
Cs_ref_df_noresm = Cs_ref_df_noresm.reset_index()
Cs_ref_df_noresm_split = Cs_ref_df_noresm["CsBin1"].str.split(" ", n = 3, expand = True)
Cs_ref_df_noresm_split.columns = ["CsBin1", "CsBin2","CsBin3", "CsBin4"]
VWD_ref_df_noresm = pd.DataFrame(VWD_ref_path_noresm)
VWD_ref_df_noresm.columns = ['vel(m/s)']
VWD_ref_df_noresm = VWD_ref_df_noresm.reset_index()
VWD_ref_df_noresm_split = VWD_ref_df_noresm["vel(m/s)"].str.split("\t", n = 2, expand = True)
VWD_ref_df_noresm_split.columns = ["vel(m/s)", "wid(m)","dep(m)"]
VWD_ref_df_noresm_split["dep(m)"] = VWD_ref_df_noresm_split["dep(m)"].str.replace('\t', '')
TP_ref_df_noresm = pd.DataFrame(TP_ref_path_noresm)
TP_ref_df_noresm.columns = ['temp(deg.C)']
TP_ref_df_noresm = TP_ref_df_noresm.reset_index()
TP_ref_df_noresm_split = TP_ref_df_noresm["temp(deg.C)"].str.split("\t", n = 1, expand = True)
TP_ref_df_noresm_split.columns = ["temp(deg.C)", "prec(m)"]
TP_ref_df_noresm_split["prec(m)"] = TP_ref_df_noresm_split["prec(m)"].str.replace('\t', '')

# Insert reference data at beginning of dataset
# GFDL
Qw_Qs_Qb_Cs_VWD_TP_merge_gfdl.loc[-1] = ([Qw_ref_df_gfdl, Qs_ref_df_gfdl, Qb_ref_df_gfdl, Cs_ref_df_gfdl_split, VWD_ref_df_gfdl_split, TP_ref_df_gfdl_split])
# Save to csv
Qw_Qs_Qb_Cs_VWD_TP_merge_gfdl.to_csv('ASCII_data_fullrecord.csv')

