import earthaccess

# Log in (prompts for credentials if not found in environmental variables)
auth = earthaccess.login()

# FIX: Added the first coordinate (-110.0, 30.0) to the end of the list
polygon = [
    (-110.0, 30.0), 
    (-100.0, 30.0), 
    (-100.0, 40.0), 
    (-110.0, 40.0), 
    (-110.0, 30.0)  # The closing pair
]

# Searching for NLDAS-2 Hourly Forcing (Precipitation is inside this collection)
# Short Name: NLDAS_FORA0125_H
results = earthaccess.search_data(
    short_name="NLDAS_FORA0125_H",
    polygon=polygon,
    temporal=("2023-01-01", "2023-01-02")
)

print(f"Found {len(results)} granules.")

# To download the files locally
earthaccess.download(results, "files/EE_NLDAS2")


import xarray as xr

# Open the downloaded NLDAS file
ds = xr.open_dataset('files/EE_NLDAS2/NLDAS_FORA0125_H.A20230102.1900.020.nc')

# See what's inside (variables, coordinates, etc.)
ds

# Access the values in the 'Rainf' variable
ds['Rainf'].values