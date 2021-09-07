#import python packages
import pandas as pd
import numpy as np
import os
import collections

## This notebook will read in one output variable at a time. The first is water discharge (Qw).

#assign text file path for a specific climate model and output variable
collections.__file__
dirname = os.path.dirname(__file__)

Qw_2020_path = os.path.join(dirname,'2020/Hydrotrend/HYDROASCII.Q')
Qw_2040_path = os.path.join(dirname,'2040/Hydrotrend/HYDROASCII.Q')
Qw_2060_path = os.path.join(dirname,'2060/Hydrotrend/HYDROASCII.Q')
Qw_2080_path = os.path.join(dirname,'2080/Hydrotrend/HYDROASCII.Q')

#read csvs
Qw_2020_df = pd.read_csv(Qw_2020_path)
Qw_2040_df = pd.read_csv(Qw_2040_path)
Qw_2060_df = pd.read_csv(Qw_2060_path)
Qw_2080_df = pd.read_csv(Qw_2080_path)

#create panda dataframe from files
Qw_2020 = pd.DataFrame(Qw_2020_df)
Qw_2040 = pd.DataFrame(Qw_2040_df)
Qw_2060 = pd.DataFrame(Qw_2060_df)
Qw_2080 = pd.DataFrame(Qw_2080_df)

#print as one single record and create new dataframe
Qw_all = pd.concat([Qw_2020[1:7301], Qw_2040[1:7301], Qw_2060[1:7301], Qw_2080[1:]])
Qw_all_df = pd.DataFrame(Qw_all)
Qw_all_df.columns = ['Qw(m3/s)']

# now lets add the next ascii file output to the same dataframe: Sediment Discharge (Qs)
#assign text file path for a specific climate model and output variable
Qs_2020_path = os.path.join(dirname,'2020/Hydrotrend/HYDROASCII.QS')
Qs_2040_path = os.path.join(dirname,'2040/Hydrotrend/HYDROASCII.QS')
Qs_2060_path = os.path.join(dirname,'2060/Hydrotrend/HYDROASCII.QS')
Qs_2080_path = os.path.join(dirname,'2080/Hydrotrend/HYDROASCII.QS')

#read csvs
Qs_2020_df = pd.read_csv(Qs_2020_path)
Qs_2040_df = pd.read_csv(Qs_2040_path)
Qs_2060_df = pd.read_csv(Qs_2060_path)
Qs_2080_df = pd.read_csv(Qs_2080_path)

#create panda dataframe from files
Qs_2020 = pd.DataFrame(Qs_2020_df)
Qs_2040 = pd.DataFrame(Qs_2040_df)
Qs_2060 = pd.DataFrame(Qs_2060_df)
Qs_2080 = pd.DataFrame(Qs_2080_df)

#print as one single record and create new dataframe
Qs_all = pd.concat([Qs_2020[1:7301], Qs_2040[1:7301], Qs_2060[1:7301], Qs_2080[1:]])
Qs_all_df = pd.DataFrame(Qs_all)
Qs_all_df.columns = ['Qs(kg/s)']

#let's do a visual check of the record to see if concat argument worked
Qw_all_df = Qw_all_df.astype(float)
Qs_all_df = Qs_all_df.astype(float)

#merge two existing dataframes (horizontal stack)
Qw_all_df = Qw_all_df.reset_index()
Qs_all_df = Qs_all_df.reset_index()
Qw_Qs_merge = pd.concat([Qw_all_df, Qs_all_df], ignore_index=False, axis=1)

## next ascii file output: Bedload discharge (Qb)
#next dataset: Qb
Qb_2020_path = os.path.join(dirname,'2020/Hydrotrend/HYDROASCII.QB')
Qb_2040_path = os.path.join(dirname,'2040/Hydrotrend/HYDROASCII.QB')
Qb_2060_path = os.path.join(dirname,'2060/Hydrotrend/HYDROASCII.QB')
Qb_2080_path = os.path.join(dirname,'2080/Hydrotrend/HYDROASCII.QB')

#read csvs
Qb_2020_df = pd.read_csv(Qb_2020_path)
Qb_2040_df = pd.read_csv(Qb_2040_path)
Qb_2060_df = pd.read_csv(Qb_2060_path)
Qb_2080_df = pd.read_csv(Qb_2080_path)

#create panda dataframes from  files
Qb_2020 = pd.DataFrame(Qb_2020_df)
Qb_2040 = pd.DataFrame(Qb_2040_df)
Qb_2060 = pd.DataFrame(Qb_2060_df)
Qb_2080 = pd.DataFrame(Qb_2080_df)

#print as one single record and create new dataframe
Qb_all = pd.concat([Qb_2020[1:7301], Qb_2040[1:7301], Qb_2060[1:7301], Qb_2080[1:]])
Qb_all_df = pd.DataFrame(Qb_all)
Qb_all_df.columns = ['Qb(kg/s)']

#merge with existing dataframe
Qb_all_df = Qb_all_df.reset_index()
Qw_Qs_Qb_merge = pd.concat([Qw_all_df, Qs_all_df, Qb_all_df], ignore_index=False, axis=1)

#### Next ascii file output: Suspended sediment concentration (Cs). This dataset has four columns.

#next dataset: Cs
Cs_2020_path = os.path.join(dirname,'2020/Hydrotrend/HYDROASCII.CS')
Cs_2040_path = os.path.join(dirname,'2040/Hydrotrend/HYDROASCII.CS')
Cs_2060_path = os.path.join(dirname,'2060/Hydrotrend/HYDROASCII.CS')
Cs_2080_path = os.path.join(dirname,'2080/Hydrotrend/HYDROASCII.CS')

#read csvs
Cs_2020_df = pd.read_csv(Cs_2020_path)
Cs_2040_df = pd.read_csv(Cs_2040_path)
Cs_2060_df = pd.read_csv(Cs_2060_path)
Cs_2080_df = pd.read_csv(Cs_2080_path)

#create panda dataframes from  files
Cs_2020 = pd.DataFrame(Cs_2020_df)
Cs_2020.columns = ['CsBin1']
Cs_2040 = pd.DataFrame(Cs_2040_df)
Cs_2040.columns = ['CsBin1']
Cs_2060 = pd.DataFrame(Cs_2060_df)
Cs_2060.columns = ['CsBin1']
Cs_2080 = pd.DataFrame(Cs_2080_df)
Cs_2080.columns = ['CsBin1']

#split single column of data into four and assign column headers
Cs_2020 = Cs_2020.reset_index()
Cs_2020_split = Cs_2020["CsBin1"].str.split(" ", n = 3, expand = True)
Cs_2020_split.columns = ["CsBin1", "CsBin2","CsBin3", "CsBin4"]

#split single column of data into four and assign column headers
Cs_2040 = Cs_2040.reset_index()
Cs_2040_split = Cs_2040["CsBin1"].str.split(" ", n = 3, expand = True)
Cs_2040_split.columns = ["CsBin1", "CsBin2","CsBin3", "CsBin4"]

#split single column of data into four and assign column headers
Cs_2060 = Cs_2060.reset_index()
Cs_2060_split = Cs_2060["CsBin1"].str.split(" ", n = 3, expand = True)
Cs_2060_split.columns = ["CsBin1", "CsBin2","CsBin3", "CsBin4"]

#split single column of data into four and assign column headers
Cs_2080 = Cs_2080.reset_index()
Cs_2080_split = Cs_2080["CsBin1"].str.split(" ", n = 3, expand = True)
Cs_2080_split.columns = ["CsBin1", "CsBin2","CsBin3", "CsBin4"]

#print as one single record and create new dataframe
Cs_all = pd.concat([Cs_2020_split[1:7301], Cs_2040_split[1:7301], Cs_2060_split[1:7301], Cs_2080_split[1:]])
Cs_all_df = pd.DataFrame(Cs_all)
Cs_all_df.columns = ["CsBin 1", "CsBin2", "CsBin3", "CsBin4"]

#merge with existing dataframe
Cs_all_df = Cs_all_df.reset_index()
Qw_Qs_Qb_Cs_merge = pd.concat([Qw_all_df, Qs_all_df, Qb_all_df, Cs_all_df], ignore_index=False, axis=1)

#### Next ascii file output: Velocity, width, depth (VWD).
#next dataset: VWD
VWD_2020_path = os.path.join(dirname,'2020/Hydrotrend/HYDROASCII.VWD')
VWD_2040_path = os.path.join(dirname,'2040/Hydrotrend/HYDROASCII.VWD')
VWD_2060_path = os.path.join(dirname,'2060/Hydrotrend/HYDROASCII.VWD')
VWD_2080_path = os.path.join(dirname,'2080/Hydrotrend/HYDROASCII.VWD')

#read csvs
VWD_2020_df = pd.read_csv(VWD_2020_path)
VWD_2040_df = pd.read_csv(VWD_2040_path)
VWD_2060_df = pd.read_csv(VWD_2060_path)
VWD_2080_df = pd.read_csv(VWD_2080_path)

#create panda dataframes from  files
VWD_2020 = pd.DataFrame(VWD_2020_df)
VWD_2020.columns = ['vel(m/s)']
VWD_2040 = pd.DataFrame(VWD_2040_df)
VWD_2040.columns = ['vel(m/s)']
VWD_2060 = pd.DataFrame(VWD_2060_df)
VWD_2060.columns = ['vel(m/s)']
VWD_2080 = pd.DataFrame(VWD_2080_df)
VWD_2080.columns = ['vel(m/s)']

#split single column of data into three and assign column headers
VWD_2020 = VWD_2020.reset_index()
VWD_2020_split = VWD_2020["vel(m/s)"].str.split("\t", n = 2, expand = True)
VWD_2020_split.columns = ["vel(m/s)", "wid(m)","dep(m)"]
VWD_2020_split["dep(m)"] = VWD_2020_split["dep(m)"].str.replace('\t', '')

#split single column of data into three and assign column headers
VWD_2040 = VWD_2040.reset_index()
VWD_2040_split = VWD_2040["vel(m/s)"].str.split("\t", n = 2, expand = True)
VWD_2040_split.columns = ["vel(m/s)", "wid(m)","dep(m)"]
VWD_2040_split["dep(m)"] = VWD_2040_split["dep(m)"].str.replace('\t', '')

#split single column of data into three and assign column headers
VWD_2060 = VWD_2060.reset_index()
VWD_2060_split = VWD_2060["vel(m/s)"].str.split("\t", n = 2, expand = True)
VWD_2060_split.columns = ["vel(m/s)", "wid(m)","dep(m)"]
VWD_2060_split["dep(m)"] = VWD_2060_split["dep(m)"].str.replace('\t', '')

#split single column of data into three and assign column headers
VWD_2080 = VWD_2080.reset_index()
VWD_2080_split = VWD_2080["vel(m/s)"].str.split("\t", n = 2, expand = True)
VWD_2080_split.columns = ["vel(m/s)", "wid(m)","dep(m)"]
VWD_2080_split["dep(m)"] = VWD_2080_split["dep(m)"].str.replace('\t', '')

#print as one single record and create new dataframe
VWD_all = pd.concat([VWD_2020_split[1:7301], VWD_2040_split[1:7301], VWD_2060_split[1:7301], VWD_2080_split[1:]])
VWD_all_df = pd.DataFrame(VWD_all)
VWD_all_df.columns = ["vel(m/s)", "wid(m)", "dep(m)"]

#merge with existing dataframe
VWD_all_df = VWD_all_df.reset_index()
Qw_Qs_Qb_Cs_VWD_merge = pd.concat([Qw_all_df, Qs_all_df, Qb_all_df, Cs_all_df, VWD_all_df], ignore_index=False, axis=1)

#### Next and last dataset: Temperature and precipitation (TP).
#next and last dataset: temp/precip
TP_2020_path = os.path.join(dirname,'2020/Hydrotrend/HYDROASCII.TEMP_PREC')
TP_2040_path = os.path.join(dirname,'2040/Hydrotrend/HYDROASCII.TEMP_PREC')
TP_2060_path = os.path.join(dirname,'2060/Hydrotrend/HYDROASCII.TEMP_PREC')
TP_2080_path = os.path.join(dirname,'2080/Hydrotrend/HYDROASCII.TEMP_PREC')

#read csvs
TP_2020_df = pd.read_csv(TP_2020_path)
TP_2040_df = pd.read_csv(TP_2040_path)
TP_2060_df = pd.read_csv(TP_2060_path)
TP_2080_df = pd.read_csv(TP_2080_path)

#create panda dataframes from  files
TP_2020 = pd.DataFrame(TP_2020_df)
TP_2020.columns = ['temp(deg.C)']
TP_2040 = pd.DataFrame(TP_2040_df)
TP_2040.columns = ['temp(deg.C)']
TP_2060 = pd.DataFrame(TP_2060_df)
TP_2060.columns = ['temp(deg.C)']
TP_2080 = pd.DataFrame(TP_2080_df)
TP_2080.columns = ['temp(deg.C)']

#split single column of data into two and assign column headers
TP_2020 = TP_2020.reset_index()
TP_2020_split = TP_2020["temp(deg.C)"].str.split("\t", n = 1, expand = True)
TP_2020_split.columns = ["temp(deg.C)", "prec(m)"]
TP_2020_split["prec(m)"] = TP_2020_split["prec(m)"].str.replace('\t', '')

#split single column of data into two and assign column headers
TP_2040 = TP_2040.reset_index()
TP_2040_split = TP_2040["temp(deg.C)"].str.split("\t", n = 1, expand = True)
TP_2040_split.columns = ["temp(deg.C)", "prec(m)"]
TP_2040_split["prec(m)"] = TP_2040_split["prec(m)"].str.replace('\t', '')

#split single column of data into two and assign column headers
TP_2060 = TP_2060.reset_index()
TP_2060_split = TP_2060["temp(deg.C)"].str.split("\t", n = 1, expand = True)
TP_2060_split.columns = ["temp(deg.C)", "prec(m)"]
TP_2060_split["prec(m)"] = TP_2060_split["prec(m)"].str.replace('\t', '')

#split single column of data into two and assign column headers
TP_2080 = TP_2080.reset_index()
TP_2080_split = TP_2080["temp(deg.C)"].str.split("\t", n = 1, expand = True)
TP_2080_split.columns = ["temp(deg.C)", "prec(m)"]
TP_2080_split["prec(m)"] = TP_2080_split["prec(m)"].str.replace('\t', '')

#print as one single record and create new dataframe
TP_all = pd.concat([TP_2020_split[1:7301], TP_2040_split[1:7301], TP_2060_split[1:7301], TP_2080_split[1:]])
TP_all_df = pd.DataFrame(TP_all)
TP_all_df.columns = ["temp(deg.C)", "prec(m)"]

#merge with existing dataframe
TP_all_df = TP_all_df.reset_index()
Qw_Qs_Qb_Cs_VWD_TP_merge = pd.concat([Qw_all_df, Qs_all_df, Qb_all_df, Cs_all_df, VWD_all_df, TP_all_df], ignore_index=False, axis=1)

#save to csv
Qw_Qs_Qb_Cs_VWD_TP_merge.to_csv(os.path.join(dirname, 'ASCII_data.csv'))
