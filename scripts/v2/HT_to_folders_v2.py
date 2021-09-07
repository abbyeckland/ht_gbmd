# This script moves the "v2/run_HT_v2.py" file to each folder,

import os
import shutil

# Ganga/rcp8p5/GFDL-ESM2M
if not os.access('setup/run_2/Ganga/rcp8p5/GFDL-ESM2M/2020', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp8p5/GFDL-ESM2M/2020', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp8p5/GFDL-ESM2M/2020')

if not os.access('setup/run_2/Ganga/rcp8p5/GFDL-ESM2M/2040', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp8p5/GFDL-ESM2M/2040', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp8p5/GFDL-ESM2M/2040')

if not os.access('setup/run_2/Ganga/rcp8p5/GFDL-ESM2M/2060', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp8p5/GFDL-ESM2M/2060', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp8p5/GFDL-ESM2M/2060')

if not os.access('setup/run_2/Ganga/rcp8p5/GFDL-ESM2M/2080', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp8p5/GFDL-ESM2M/2080', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp8p5/GFDL-ESM2M/2080')

# Ganga/rcp8p5/HadGEM2
if not os.access('setup/run_2/Ganga/rcp8p5/HadGEM2/2020', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp8p5/HadGEM2/2020', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp8p5/HadGEM2/2020')

if not os.access('setup/run_2/Ganga/rcp8p5/HadGEM2/2040', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp8p5/HadGEM2/2040', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp8p5/HadGEM2/2040')

if not os.access('setup/run_2/Ganga/rcp8p5/HadGEM2/2060', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp8p5/HadGEM2/2060', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp8p5/HadGEM2/2060')

if not os.access('setup/run_2/Ganga/rcp8p5/HadGEM2/2080', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp8p5/HadGEM2/2080', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp8p5/HadGEM2/2080')

# Ganga/rcp8p5/IPSL_CM5A
if not os.access('setup/run_2/Ganga/rcp8p5/IPSL_CM5A/2020', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp8p5/IPSL_CM5A/2020', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp8p5/IPSL_CM5A/2020')

if not os.access('setup/run_2/Ganga/rcp8p5/IPSL_CM5A/2040', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp8p5/IPSL_CM5A/2040', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp8p5/IPSL_CM5A/2040')

if not os.access('setup/run_2/Ganga/rcp8p5/IPSL_CM5A/2060', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp8p5/IPSL_CM5A/2060', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp8p5/IPSL_CM5A/2060')

if not os.access('setup/run_2/Ganga/rcp8p5/IPSL_CM5A/2080', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp8p5/IPSL_CM5A/2080', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp8p5/IPSL_CM5A/2080')

# Ganga/rcp8p5/MIROC-ESM-CHEM
if not os.access('setup/run_2/Ganga/rcp8p5/MIROC-ESM-CHEM/2020', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp8p5/IPSL_CM5A/2020', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp8p5/MIROC-ESM-CHEM/2020')

if not os.access('setup/run_2/Ganga/rcp8p5/MIROC-ESM-CHEM/2040', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp8p5/MIROC-ESM-CHEM/2040', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp8p5/MIROC-ESM-CHEM/2040')

if not os.access('setup/run_2/Ganga/rcp8p5/MIROC-ESM-CHEM/2060', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp8p5/MIROC-ESM-CHEM/2060', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp8p5/MIROC-ESM-CHEM/2060')

if not os.access('setup/run_2/Ganga/rcp8p5/MIROC-ESM-CHEM/2080', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp8p5/MIROC-ESM-CHEM/2080', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp8p5/MIROC-ESM-CHEM/2080')

# Ganga/rcp8p5/NORESM-M
if not os.access('setup/run_2/Ganga/rcp8p5/NORESM-M/2020', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp8p5/NORESM-M/2020', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp8p5/NORESM-M/2020')

if not os.access('setup/run_2/Ganga/rcp8p5/NORESM-M/2040', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp8p5/NORESM-M/2040', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp8p5/NORESM-M/2040')

if not os.access('setup/run_2/Ganga/rcp8p5/NORESM-M/2060', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp8p5/NORESM-M/2060', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp8p5/NORESM-M/2060')

if not os.access('setup/run_2/Ganga/rcp8p5/NORESM-M/2080', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp8p5/NORESM-M/2080', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp8p5/NORESM-M/2080')

# Ganga/rcp4p5/GFDL-ESM2M
if not os.access('setup/run_2/Ganga/rcp4p5/GFDL-ESM2M/2020', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp4p5/GFDL-ESM2M/2020', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp4p5/GFDL-ESM2M/2020')

if not os.access('setup/run_2/Ganga/rcp4p5/GFDL-ESM2M/2040', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp4p5/GFDL-ESM2M/2040', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp4p5/GFDL-ESM2M/2040')

if not os.access('setup/run_2/Ganga/rcp4p5/GFDL-ESM2M/2060', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp4p5/GFDL-ESM2M/2060', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp4p5/GFDL-ESM2M/2060')

if not os.access('setup/run_2/Ganga/rcp4p5/GFDL-ESM2M/2080', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp4p5/GFDL-ESM2M/2080', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp4p5/GFDL-ESM2M/2080')

# Ganga/rcp4p5/HadGEM2
if not os.access('setup/run_2/Ganga/rcp4p5/HadGEM2/2020', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp4p5/HadGEM2/2020', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp4p5/HadGEM2/2020')

if not os.access('setup/run_2/Ganga/rcp4p5/HadGEM2/2040', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp4p5/HadGEM2/2040', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp4p5/HadGEM2/2040')

if not os.access('setup/run_2/Ganga/rcp4p5/HadGEM2/2060', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp4p5/HadGEM2/2060', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp4p5/HadGEM2/2060')

if not os.access('setup/run_2/Ganga/rcp4p5/HadGEM2/2080', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp4p5/HadGEM2/2080', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp4p5/HadGEM2/2080')

# Ganga/rcp4p5/IPSL_CM5A
if not os.access('setup/run_2/Ganga/rcp4p5/IPSL_CM5A/2020', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp4p5/IPSL_CM5A/2020', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp4p5/IPSL_CM5A/2020')

if not os.access('setup/run_2/Ganga/rcp4p5/IPSL_CM5A/2040', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp4p5/IPSL_CM5A/2040', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp4p5/IPSL_CM5A/2040')

if not os.access('setup/run_2/Ganga/rcp4p5/IPSL_CM5A/2060', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp4p5/IPSL_CM5A/2060', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp4p5/IPSL_CM5A/2060')

if not os.access('setup/run_2/Ganga/rcp4p5/IPSL_CM5A/2080', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp4p5/IPSL_CM5A/2080', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp4p5/IPSL_CM5A/2080')

# Ganga/rcp4p5/MIROC-ESM-CHEM
if not os.access('setup/run_2/Ganga/rcp4p5/MIROC-ESM-CHEM/2020', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp4p5/MIROC-ESM-CHEM/2020', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp4p5/MIROC-ESM-CHEM/2020')

if not os.access('setup/run_2/Ganga/rcp4p5/MIROC-ESM-CHEM/2040', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp4p5/MIROC-ESM-CHEM/2040', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp4p5/MIROC-ESM-CHEM/2040')

if not os.access('setup/run_2/Ganga/rcp4p5/MIROC-ESM-CHEM/2060', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp4p5/MIROC-ESM-CHEM/2060', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp4p5/MIROC-ESM-CHEM/2060')

if not os.access('setup/run_2/Ganga/rcp4p5/MIROC-ESM-CHEM/2080', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp4p5/MIROC-ESM-CHEM/2080', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp4p5/MIROC-ESM-CHEM/2080')

# Ganga/rcp4p5/NORESM-M
if not os.access('setup/run_2/Ganga/rcp4p5/NORESM-M/2020', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp4p5/NORESM-M/2020', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp4p5/NORESM-M/2020')

if not os.access('setup/run_2/Ganga/rcp4p5/NORESM-M/2040', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp4p5/NORESM-M/2040', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp4p5/NORESM-M/2040')

if not os.access('setup/run_2/Ganga/rcp4p5/NORESM-M/2060', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp4p5/NORESM-M/2060', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp4p5/NORESM-M/2060')

if not os.access('setup/run_2/Ganga/rcp4p5/NORESM-M/2080', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp4p5/NORESM-M/2080', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Ganga/rcp4p5/NORESM-M/2080')

# Brahmaputra/rcp8p5/GFDL-ESM2M
if not os.access('setup/run_2/Brahmaputra/rcp8p5/GFDL-ESM2M/2020', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp8p5/GFDL-ESM2M/2020', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp8p5/GFDL-ESM2M/2020')

if not os.access('setup/run_2/Brahmaputra/rcp8p5/GFDL-ESM2M/2040', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp8p5/GFDL-ESM2M/2040', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp8p5/GFDL-ESM2M/2040')

if not os.access('setup/run_2/Brahmaputra/rcp8p5/GFDL-ESM2M/2060', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp8p5/GFDL-ESM2M/2060', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp8p5/GFDL-ESM2M/2060')

if not os.access('setup/run_2/Brahmaputra/rcp8p5/GFDL-ESM2M/2080', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp8p5/GFDL-ESM2M/2080', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp8p5/GFDL-ESM2M/2080')

# Brahmaputra/rcp8p5/HadGEM2
if not os.access('setup/run_2/Brahmaputra/rcp8p5/HadGEM2/2020', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp8p5/HadGEM2/2020', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp8p5/HadGEM2/2020')

if not os.access('setup/run_2/Brahmaputra/rcp8p5/HadGEM2/2040', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp8p5/HadGEM2/2040', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp8p5/HadGEM2/2040')

if not os.access('setup/run_2/Brahmaputra/rcp8p5/HadGEM2/2060', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp8p5/HadGEM2/2060', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp8p5/HadGEM2/2060')

if not os.access('setup/run_2/Brahmaputra/rcp8p5/HadGEM2/2080', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp8p5/HadGEM2/2080', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp8p5/HadGEM2/2080')

# Brahmaputra/rcp8p5/IPSL_CM5A
if not os.access('setup/run_2/Brahmaputra/rcp8p5/IPSL_CM5A/2020', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp8p5/IPSL_CM5A/2020', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp8p5/IPSL_CM5A/2020')

if not os.access('setup/run_2/Brahmaputra/rcp8p5/IPSL_CM5A/2040', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp8p5/IPSL_CM5A/2040', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp8p5/IPSL_CM5A/2040')

if not os.access('setup/run_2/Brahmaputra/rcp8p5/IPSL_CM5A/2060', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp8p5/IPSL_CM5A/2060', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp8p5/IPSL_CM5A/2060')

if not os.access('setup/run_2/Brahmaputra/rcp8p5/IPSL_CM5A/2080', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp8p5/IPSL_CM5A/2080', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp8p5/IPSL_CM5A/2080')

# Brahmaputra/rcp8p5/MIROC-ESM-CHEM
if not os.access('setup/run_2/Brahmaputra/rcp8p5/MIROC-ESM-CHEM/2020', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp8p5/IPSL_CM5A/2020', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp8p5/MIROC-ESM-CHEM/2020')

if not os.access('setup/run_2/Brahmaputra/rcp8p5/MIROC-ESM-CHEM/2040', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp8p5/MIROC-ESM-CHEM/2040', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp8p5/MIROC-ESM-CHEM/2040')

if not os.access('setup/run_2/Brahmaputra/rcp8p5/MIROC-ESM-CHEM/2060', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp8p5/MIROC-ESM-CHEM/2060', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp8p5/MIROC-ESM-CHEM/2060')

if not os.access('setup/run_2/Brahmaputra/rcp8p5/MIROC-ESM-CHEM/2080', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp8p5/MIROC-ESM-CHEM/2080', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp8p5/MIROC-ESM-CHEM/2080')

# Brahmaputra/rcp8p5/NORESM-M
if not os.access('setup/run_2/Brahmaputra/rcp8p5/NORESM-M/2020', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp8p5/NORESM-M/2020', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp8p5/NORESM-M/2020')

if not os.access('setup/run_2/Brahmaputra/rcp8p5/NORESM-M/2040', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp8p5/NORESM-M/2040', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp8p5/NORESM-M/2040')

if not os.access('setup/run_2/Brahmaputra/rcp8p5/NORESM-M/2060', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp8p5/NORESM-M/2060', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp8p5/NORESM-M/2060')

if not os.access('setup/run_2/Brahmaputra/rcp8p5/NORESM-M/2080', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp8p5/NORESM-M/2080', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp8p5/NORESM-M/2080')

# Brahmaputra/rcp4p5/GFDL-ESM2M
if not os.access('setup/run_2/Brahmaputra/rcp4p5/GFDL-ESM2M/2020', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp4p5/GFDL-ESM2M/2020', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp4p5/GFDL-ESM2M/2020')

if not os.access('setup/run_2/Brahmaputra/rcp4p5/GFDL-ESM2M/2040', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp4p5/GFDL-ESM2M/2040', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp4p5/GFDL-ESM2M/2040')

if not os.access('setup/run_2/Brahmaputra/rcp4p5/GFDL-ESM2M/2060', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp4p5/GFDL-ESM2M/2060', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp4p5/GFDL-ESM2M/2060')

if not os.access('setup/run_2/Brahmaputra/rcp4p5/GFDL-ESM2M/2080', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp4p5/GFDL-ESM2M/2080', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp4p5/GFDL-ESM2M/2080')

# Brahmaputra/rcp4p5/HadGEM2
if not os.access('setup/run_2/Brahmaputra/rcp4p5/HadGEM2/2020', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp4p5/HadGEM2/2020', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp4p5/HadGEM2/2020')

if not os.access('setup/run_2/Brahmaputra/rcp4p5/HadGEM2/2040', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp4p5/HadGEM2/2040', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp4p5/HadGEM2/2040')

if not os.access('setup/run_2/Brahmaputra/rcp4p5/HadGEM2/2060', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp4p5/HadGEM2/2060', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp4p5/HadGEM2/2060')

if not os.access('setup/run_2/Brahmaputra/rcp4p5/HadGEM2/2080', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp4p5/HadGEM2/2080', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp4p5/HadGEM2/2080')

# Brahmaputra/rcp4p5/IPSL_CM5A
if not os.access('setup/run_2/Brahmaputra/rcp4p5/IPSL_CM5A/2020', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp4p5/IPSL_CM5A/2020', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp4p5/IPSL_CM5A/2020')

if not os.access('setup/run_2/Brahmaputra/rcp4p5/IPSL_CM5A/2040', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp4p5/IPSL_CM5A/2040', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp4p5/IPSL_CM5A/2040')

if not os.access('setup/run_2/Brahmaputra/rcp4p5/IPSL_CM5A/2060', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp4p5/IPSL_CM5A/2060', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp4p5/IPSL_CM5A/2060')

if not os.access('setup/run_2/Brahmaputra/rcp4p5/IPSL_CM5A/2080', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp4p5/IPSL_CM5A/2080', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp4p5/IPSL_CM5A/2080')

# Brahmaputra/rcp4p5/MIROC-ESM-CHEM
if not os.access('setup/run_2/Brahmaputra/rcp4p5/MIROC-ESM-CHEM/2020', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp4p5/MIROC-ESM-CHEM/2020', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp4p5/MIROC-ESM-CHEM/2020')

if not os.access('setup/run_2/Brahmaputra/rcp4p5/MIROC-ESM-CHEM/2040', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp4p5/MIROC-ESM-CHEM/2040', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp4p5/MIROC-ESM-CHEM/2040')

if not os.access('setup/run_2/Brahmaputra/rcp4p5/MIROC-ESM-CHEM/2060', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp4p5/MIROC-ESM-CHEM/2060', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp4p5/MIROC-ESM-CHEM/2060')

if not os.access('setup/run_2/Brahmaputra/rcp4p5/MIROC-ESM-CHEM/2080', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp4p5/MIROC-ESM-CHEM/2080', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp4p5/MIROC-ESM-CHEM/2080')

# Brahmaputra/rcp4p5/NORESM-M
if not os.access('setup/run_2/Brahmaputra/rcp4p5/NORESM-M/2020', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp4p5/NORESM-M/2020', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp4p5/NORESM-M/2020')

if not os.access('setup/run_2/Brahmaputra/rcp4p5/NORESM-M/2040', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp4p5/NORESM-M/2040', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp4p5/NORESM-M/2040')

if not os.access('setup/run_2/Brahmaputra/rcp4p5/NORESM-M/2060', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp4p5/NORESM-M/2060', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp4p5/NORESM-M/2060')

if not os.access('setup/run_2/Brahmaputra/rcp4p5/NORESM-M/2080', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp4p5/NORESM-M/2080', 0o700)
shutil.copy('scripts/v2/run_HT_v2.py', 'setup/run_2/Brahmaputra/rcp4p5/NORESM-M/2080')
