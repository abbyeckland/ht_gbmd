# This script moves the "read_asciis_v2.py" file to each folder,

import os
import shutil

# Ganga/rcp8p5/GFDL-ESM2M
if not os.access('setup/run_2/Ganga/rcp8p5/GFDL-ESM2M', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp8p5/GFDL-ESM2M', 0o700)
shutil.copy('scripts/v2/read_asciis_v2.py', 'setup/run_2/Ganga/rcp8p5/GFDL-ESM2M')

# Ganga/rcp8p5/HadGEM2
if not os.access('setup/run_2/Ganga/rcp8p5/HadGEM2', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp8p5/HadGEM2', 0o700)
shutil.copy('scripts/v2/read_asciis_v2.py', 'setup/run_2/Ganga/rcp8p5/HadGEM2')

# Ganga/rcp8p5/IPSL_CM5A
if not os.access('setup/run_2/Ganga/rcp8p5/IPSL_CM5A', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp8p5/IPSL_CM5A', 0o700)
shutil.copy('scripts/v2/read_asciis_v2.py', 'setup/run_2/Ganga/rcp8p5/IPSL_CM5A')

# Ganga/rcp8p5/MIROC-ESM-CHEM
if not os.access('setup/run_2/Ganga/rcp8p5/MIROC-ESM-CHEM', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp8p5/MIROC-ESM-CHEM', 0o700)
shutil.copy('scripts/v2/read_asciis_v2.py', 'setup/run_2/Ganga/rcp8p5/MIROC-ESM-CHEM')

# Ganga/rcp8p5/NORESM-M
if not os.access('setup/run_2/Ganga/rcp8p5/NORESM-M', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp8p5/NORESM-M', 0o700)
shutil.copy('scripts/v2/read_asciis_v2.py', 'setup/run_2/Ganga/rcp8p5/NORESM-M')

# Ganga/rcp4p5/GFDL-ESM2M
if not os.access('setup/run_2/Ganga/rcp4p5/GFDL-ESM2M', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp4p5/GFDL-ESM2M', 0o700)
shutil.copy('scripts/v2/read_asciis_v2.py', 'setup/run_2/Ganga/rcp4p5/GFDL-ESM2M')

# Ganga/rcp4p5/HadGEM2
if not os.access('setup/run_2/Ganga/rcp4p5/HadGEM2', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp4p5/HadGEM2', 0o700)
shutil.copy('scripts/v2/read_asciis_v2.py', 'setup/run_2/Ganga/rcp4p5/HadGEM2')

# Ganga/rcp4p5/IPSL_CM5A
if not os.access('setup/run_2/Ganga/rcp4p5/IPSL_CM5A', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp4p5/IPSL_CM5A', 0o700)
shutil.copy('scripts/v2/read_asciis_v2.py', 'setup/run_2/Ganga/rcp4p5/IPSL_CM5A')

# Ganga/rcp4p5/MIROC-ESM-CHEM
if not os.access('setup/run_2/Ganga/rcp4p5/MIROC-ESM-CHEM', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp4p5/MIROC-ESM-CHEM', 0o700)
shutil.copy('scripts/v2/read_asciis_v2.py', 'setup/run_2/Ganga/rcp4p5/MIROC-ESM-CHEM')

# Ganga/rcp4p5/NORESM-M
if not os.access('setup/run_2/Ganga/rcp4p5/NORESM-M', os.F_OK):
    os.mkdir('setup/run_2/Ganga/rcp4p5/NORESM-M', 0o700)
shutil.copy('scripts/v2/read_asciis_v2.py', 'setup/run_2/Ganga/rcp4p5/NORESM-M')

# Brahmaputra/rcp8p5/GFDL-ESM2M
if not os.access('setup/run_2/Brahmaputra/rcp8p5/GFDL-ESM2M', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp8p5/GFDL-ESM2M', 0o700)
shutil.copy('scripts/v2/read_asciis_v2.py', 'setup/run_2/Brahmaputra/rcp8p5/GFDL-ESM2M')

# Brahmaputra/rcp8p5/HadGEM2
if not os.access('setup/run_2/Brahmaputra/rcp8p5/HadGEM2', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp8p5/HadGEM2', 0o700)
shutil.copy('scripts/v2/read_asciis_v2.py', 'setup/run_2/Brahmaputra/rcp8p5/HadGEM2')

# Brahmaputra/rcp8p5/IPSL_CM5A
if not os.access('setup/run_2/Brahmaputra/rcp8p5/IPSL_CM5A', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp8p5/IPSL_CM5A', 0o700)
shutil.copy('scripts/v2/read_asciis_v2.py', 'setup/run_2/Brahmaputra/rcp8p5/IPSL_CM5A')

# Brahmaputra/rcp8p5/MIROC-ESM-CHEM
if not os.access('setup/run_2/Brahmaputra/rcp8p5/MIROC-ESM-CHEM', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp8p5/MIROC-ESM-CHEM', 0o700)
shutil.copy('scripts/v2/read_asciis_v2.py', 'setup/run_2/Brahmaputra/rcp8p5/MIROC-ESM-CHEM')

# Brahmaputra/rcp8p5/NORESM-M
if not os.access('setup/run_2/Brahmaputra/rcp8p5/NORESM-M', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp8p5/NORESM-M', 0o700)
shutil.copy('scripts/v2/read_asciis_v2.py', 'setup/run_2/Brahmaputra/rcp8p5/NORESM-M')

# Brahmaputra/rcp4p5/GFDL-ESM2M
if not os.access('setup/run_2/Brahmaputra/rcp4p5/GFDL-ESM2M', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp4p5/GFDL-ESM2M', 0o700)
shutil.copy('scripts/v2/read_asciis_v2.py', 'setup/run_2/Brahmaputra/rcp4p5/GFDL-ESM2M')

# Brahmaputra/rcp4p5/HadGEM2
if not os.access('setup/run_2/Brahmaputra/rcp4p5/HadGEM2', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp4p5/HadGEM2', 0o700)
shutil.copy('scripts/v2/read_asciis_v2.py', 'setup/run_2/Brahmaputra/rcp4p5/HadGEM2')

# Brahmaputra/rcp4p5/IPSL_CM5A
if not os.access('setup/run_2/Brahmaputra/rcp4p5/IPSL_CM5A', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp4p5/IPSL_CM5A', 0o700)
shutil.copy('scripts/v2/read_asciis_v2.py', 'setup/run_2/Brahmaputra/rcp4p5/IPSL_CM5A')

# Brahmaputra/rcp4p5/MIROC-ESM-CHEM
if not os.access('setup/run_2/Brahmaputra/rcp4p5/MIROC-ESM-CHEM', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp4p5/MIROC-ESM-CHEM', 0o700)
shutil.copy('scripts/v2/read_asciis_v2.py', 'setup/run_2/Brahmaputra/rcp4p5/MIROC-ESM-CHEM')

# Brahmaputra/rcp4p5/NORESM-M
if not os.access('setup/run_2/Brahmaputra/rcp4p5/NORESM-M', os.F_OK):
    os.mkdir('setup/run_2/Brahmaputra/rcp4p5/NORESM-M', 0o700)
shutil.copy('scripts/v2/read_asciis_v2.py', 'setup/run_2/Brahmaputra/rcp4p5/NORESM-M')
