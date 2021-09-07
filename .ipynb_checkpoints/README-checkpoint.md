# This repository contains HydroTrend model outputs for the Ganges and Brahmaputra basins.

All model outputs are contained in this repository.

Clone this repository to run on your local machine.

## Instructions
To run the HydroTrend model, you must run the scripts located in the "scripts" folder in sequential order.

### Step 1: Run HydroTrend for projected climate scenarios (rcp4p5 and rcp8p5).
These climate scenarios are projected by 4 different climate models over 4 different time periods. The climate models are:
- GFDL-ESM2M
- HadGEM2
- MIROC_ESM_CHEM
- NORESM-M

And the time periods are:
- 2006-2035 (representative for the climate of the year 2020)
- 2026-2055 (representative for the climate of the year 2040)
- 2046-2075 (representative of the climate of the year 2060)
- 2066-2095 (representative for the climate of the year 2080)

1. Make any code edits to the script that runs HydroTrend by editing `run_HT_v1.py`.
- When you are done editing the code...
2. Run `HT_to_folders_v1.py`
- This moves the script `run_HT_v1.py` to various folder locations so that it can be run with specific input parameters.
3. Run `run_HT_all_v1.py`
- This script runs the `run_HT_v1.py` script within each folder location.
    - It's important to run the script within each folder location. The climate data differs for each model run, so the script has to be located in multiple places in order to refer to the correct input (climate) data.

### Step 2: Run HydroTrend for the reference climate scenario.
This scenario runs from 1976-2006, thus these output data can be directly compared with observed data. This scenario uses climate hindcasts from the same 4 climate models indicated above.
1. Make any code edits to the script that runs HydroTrend by editing `run_HT_ref_BR_v1.py` and `run_HT_ref_GR_v1.py` for the Brahmaputra and Ganges basins, respectively.
- These are separate scripts since they will be compared with observed data located in different folder locations for the Ganges and Brahmaputra in the form of csvs.
- When you are done editing the code...
2. Run `HT_to_folders_ref_v1.py`
- This moves the scripts `run_HT_ref_BR_v1.py` and `run_HT_ref_GR_v1.py` to various folder locations so that it can be run with specific input paramters.
3. Run `run_HT_all_ref_v1.py`
- This script runs the `run_HT_ref_BR_v1.py` and/or `run_HT_ref_GR_v1.py`scripts within each folder location.

### Step 3: Post-process the output data from the rcp8p5 and rcp4p5 HydroTrend runs
This step concatenates all of the ASCII outputs from the model runs into one CSV file so that trends in the data can be easily assessed for the projected (future) climate scenarios.
1. Make any code edits to the script by editing `read_asciis_v1.py`
- When you are done editing the code...
2. Run `asciis_to_folders_v1.py`
- This moves the script `read_asciis_v1` to various folder locations.
3. Run `read_asciis_all_v1.py`
- This script runs the `read_asciis_v1.py` script within each folder location.

### Step 4: Check out the outputs!
Go to the post-processing folder to check out the processed data and see how the figures are generated. 
