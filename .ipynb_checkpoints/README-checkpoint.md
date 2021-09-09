# This repository contains HydroTrend model outputs for the Ganges and Brahmaputra basins.

All scripts, model outputs, climate, water and sediment data, and jupyter notebooks for post processing, are contained in this repository.

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

  - Note that data from a fifth climate model, IPSL_CM5A, was initially included in the model runs; however, the results from these simulations resulted in too much error, and were removed from further analysis.

1. Make any code edits to the script that runs HydroTrend by editing `run_HT_v2.py`.
- When you are done editing the code...
2. Run `HT_to_folders_v2.py` **FROM THE TERMINAL WHILE IN THE CURRENT REPOSITORY.** Type "python scripts/v2/HT_to_folders_v2.py".
- This moves the script `run_HT_v2.py` to various folder locations so that it can be run with specific input parameters.
3. Activate pymt in order to run HydroTrend. Type "conda activate pymt" into the terminal.
- If you don't have pymt installed on your laptop, go to the CSDMS website for instructions: https://pymt.readthedocs.io/en/latest/install.html.
4. Run `run_HT_all_v2.py` **FROM THE TERMINAL WHILE IN THE CURRENT REPOSITORY.** Type "python scripts/v2/run_HT_all_v2.py".
- This script runs the `run_HT_v2.py` script within each folder location.
- This step will take several minutes. You will see the model being implemented in the terminal window.
    - Note: it's important that the script is located within each folder since each model run is driven by different climate data, so the script has to be located in multiple places in order to refer to the correct input (climate) data. (There may be a more efficient way to do this but I haven't sat down to figure it out yet).

*Before moving on to Step 2, note that you should always run the script from your terminal, ensuring your current directory is set to the present repository, pointed to the correct folder (scripts) and version number (v2).*

### Step 2: Run HydroTrend for the reference climate scenario.
This scenario runs from 1976-2006, thus these output data can be directly compared with observed data. This scenario uses climate hindcasts from the same 4 climate models indicated above.
1. Make any code edits to the scripts that runs HydroTrend by editing `run_HT_ref_BR_v2.py` and `run_HT_ref_GR_v2.py` for the Brahmaputra and Ganges basins, respectively.
- These are separate scripts since they will be compared with observed data that have records of unequal lengths.
- When you are done editing the code...
2. Run `HT_to_folders_ref_v2.py`
- This moves the scripts `run_HT_ref_BR_v2.py` and `run_HT_ref_GR_v2.py` to various folder locations so that it can be run with specific input paramters.
3. Run `run_HT_all_ref_v2.py`
- This script runs the `run_HT_ref_BR_v2.py` and/or `run_HT_ref_GR_v2.py`scripts within each folder location.

### Step 3: Post-process the output data from the rcp8p5 and rcp4p5 HydroTrend runs
This step concatenates all of the ASCII outputs from the model runs into one CSV file so that trends in the data can be easily assessed for the projected (future) climate scenarios.
1. Make any code edits to the script by editing `read_asciis_v2.py`
- When you are done editing the code...
2. Run `asciis_to_folders_v2.py`
- This moves the script `read_asciis_v2` to various folder locations.
3. Run `read_asciis_all_v2.py`
- This script runs the `read_asciis_v2.py` script within each folder location.

### Step 4: Check out the outputs!
Go to the post-processing folder to check out the processed data and see how the figures are generated.

Here you will find several notebooks described below:
- GR_projected_rcp4p5.ipynb
    - Loads output data and plots water and sediment discharge projections from 2006-2096 for *rcp4.5* climate scenario for Ganges River
- GR_projected_rcp8.5.ipynb
    - Loads output data and plots water and sediment discharge projections from 2006-2096 for *rcp8.5* climate scenario for Ganges River
- GR_reference.ipynb
    - Compares simulated versus observed water discharge data for the Ganges River
    - Evalulates mean and maximum simulated versus observed water discharge
    - Calculates goodness-of fit standards for water discharge
    - Plots simulated mean daily and mean annual water discharge compared with observed values
    - Computes average sediment discharge over reference scenario using the sum method
- GR_peakdischarge.ipynb
    - Loads simulation arrays for each time period, reshapes these into annual arrays
    - Calculates how the magnitude of peak discharge and minimum discharge changes over the century, as well as the timing of peak water discharge
    - Plots how water hydrographs and sediment loads change over the century for the Ganges River
- BR_projected_rcp4.5.ipynb
    - Loads output data and plots water and sediment discharge projections from 2006-2096 for *rcp4.5* climate scenario for Brahmaputra River
- BR_projected_rcp8.5.ipynb
    - Loads output data and plots water and sediment discharge projections from 2006-2096 for *rcp8.5* climate scenario for Brahmaputra River
- BR_reference.ipynb
    - Compares simulated versus observed water discharge data for the Brahmaputra River
    - Evalulates mean and maximum simulated versus observed water discharge
    - Calculates goodness-of fit standards for water discharge
    - Plots simulated mean daily and mean annual water discharge compared with observed values
    - Computes average sediment discharge over reference scenario using the sum method
- BR_peakdischarge.ipynb
    - Loads simulation arrays for each time period, reshapes these into annual arrays
    - Calculates how the magnitude of peak discharge and minimum discharge changes over the century, as well as the timing of peak water discharge
    - Plots how water hydrographs and sediment loads change over the century for the Brahmaputra River
- GBR_combo_peakdischarge.ipynb
    - Same notebook as GR_peakdischarge.ipynb and BR_peakdischarge.ipynb, but combines water and sediment discharge to get loads for the combined GB river
    
***See README files in remaining folders for an idea of what else is provided in this repository.***