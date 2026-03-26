import dataretrieval as dr
from dataretrieval import nwis
import pandas as pd
import pydaymet as daymet

# Selected basin:
#Alaska: USGS, 15274600 SNOTEL: 1070

#Pull streamflow data
site_id = '15274600'
start_date = "2024-01-01"
end_date = "2024-12-31"

Ak_streamflow_data,meta = nwis.get_dv(sites=site_id,
                           parameterCd="00060",
                           start=start_date,
                           end=end_date)
#print(Ak_streamflow_data.head())

#Clean streamflow
Ak_streamflow_data.index = pd.to_datetime(Ak_streamflow_data.index)
Ak_streamflow_data = Ak_streamflow_data.rename(columns={'00060_Mean': 'streamflow (cfs)'})
Ak_streamflow_data.drop(columns=['00060_Mean_cd'], inplace=True)
print(Ak_streamflow_data.head())

#Pull SNOTEL/Swe data
'''
Data pulled from: Gagliano, E. (2024). 
snotel_ccss_stations (Version v1.0) [Computer software]. https://github.com/egagli/snotel_ccss_stations
'''
url = 'https://github.com/egagli/snotel_ccss_stations/blob/main/data/1070_AK_SNTL.csv?raw=true'

try:
    # Read CSV directly into a DataFrame
    snotel_AK = pd.read_csv(url)
    print("CSV loaded successfully!")
    print(snotel_AK.head())  # Display first 5 rows
except Exception as e:
    print(f"Error loading CSV: {e}")

#Pull daymet data
#Pull gages 2

#Get centroid of basin (HUC 6, KNIK ARM)

var = ["prcp", "tmin", "tmax",'srad', 'swe', 'vp', 'dayl'] # Variables to fetch, precip, temperature, solar radiation, snow water equivalent, vapor pressure, day length
dates = pd.date_range(start=start_date, end=end_date)
met_df = daymet.get_bycoords(centroid, dates, variables=var)



