# This script moves the "run_HT_v1.py" file to each model run folder,
# so that this does not have to be done manually.

import os, shutil

# Ganga/reference
if not os.access('setup/run_2/Ganga/reference/GFDL-ESM2M', os.F_OK):
    os.mkdir('setup/run_2/Ganga/reference/GFDL-ESM2M', 0o700)
shutil.copy('scripts/v2/run_HT_ref_GR_v2.py', 'setup/run_2/Ganga/reference/GFDL-ESM2M')

if not os.access('setup/run_2/Ganga/reference/HadGEM2', os.F_OK):
    os.mkdir('setup/run_2/Ganga/reference/HadGEM2', 0o700)
shutil.copy('scripts/v2/run_HT_ref_GR_v2.py', 'setup/run_2/Ganga/reference/HadGEM2')

if not os.access('setup/run_2/Ganga/reference/IPSL_CM5A', os.F_OK):
    os.mkdir('setup/run_2/Ganga/reference/IPSL_CM5A', 0o700)
shutil.copy('scripts/v2/run_HT_ref_GR_v2.py', 'setup/run_2/Ganga/reference/IPSL_CM5A')

if not os.access('setup/run_2/Ganga/reference/MIROC-ESM-CHEM', os.F_OK):
    os.mkdir('setup/run_2/Ganga/reference/MIROC-ESM-CHEM', 0o700)
shutil.copy('scripts/v2/run_HT_ref_GR_v2.py', 'setup/run_2/Ganga/reference/MIROC-ESM-CHEM')

if not os.access('setup/run_2/Ganga/reference/NORESM-M', os.F_OK):
    os.mkdir('setup/run_2/Ganga/reference/NORESM-M', 0o700)
shutil.copy('scripts/v2/run_HT_ref_GR_v2.py', 'setup/run_2/Ganga/reference/NORESM-M')

# Brahmaputra/reference
if not os.access('setup/run_2/Brahmaputra/reference/GFDL-ESM2M', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/reference/GFDL-ESM2M', 0o700)
shutil.copy('scripts/v2/run_HT_ref_BR_v2.py', 'setup/run_2/Brahmaputra/reference/GFDL-ESM2M')

if not os.access('setup/run_2/Brahmaputra/reference/HadGEM2', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/reference/HadGEM2', 0o700)
shutil.copy('scripts/v2/run_HT_ref_BR_v2.py', 'setup/run_2/Brahmaputra/reference/HadGEM2')

if not os.access('setup/run_2/Brahmaputra/reference/IPSL_CM5A', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/reference/IPSL_CM5A', 0o700)
shutil.copy('scripts/v2/run_HT_ref_BR_v2.py', 'setup/run_2/Brahmaputra/reference/IPSL_CM5A')

if not os.access('setup/run_2/Brahmaputra/reference/MIROC-ESM-CHEM', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/reference/MIROC-ESM-CHEM', 0o700)
shutil.copy('scripts/v2/run_HT_ref_BR_v2.py', 'setup/run_2/Brahmaputra/reference/MIROC-ESM-CHEM')

if not os.access('setup/run_2/Brahmaputra/reference/NORESM-M', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/reference/NORESM-M', 0o700)
shutil.copy('scripts/v2/run_HT_ref_BR_v2.py', 'setup/run_2/Brahmaputra/reference/NORESM-M')
