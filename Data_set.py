#Neil McCaul

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Importing CSVs download from the semopx website. Dynamic report section

#Eirgrid Wind forecast data from the SEMOPX website
data1 = pd.read_csv(r"\\vir-hvh-fs-01.energia.local\Energia-Users\Eanam\Desktop\UCD PROJECT\Aggregated Eir Wind Forecast.csv")

#Eigrid electricity demand forecast from SEMOPX website
data2 = pd.read_csv(r"\\vir-hvh-fs-01.energia.local\Energia-Users\Eanam\Desktop\UCD PROJECT\Daily Load Forecast Summary.csv")

#Physical notifications (Power plants running in Ireland)
data3 = pd.read_csv(r"\\vir-hvh-fs-01.energia.local\Energia-Users\Eanam\Desktop\UCD PROJECT\Final Physical Notification.csv")

#how in balance is the Iirsh power system
data4 = pd.read_csv(r"\\vir-hvh-fs-01.energia.local\Energia-Users\Eanam\Desktop\UCD PROJECT\Forecast Imbalance.csv")

#Eigrid electricity Imbalance price from SEMOPX website
data5 = pd.read_csv(r"\\vir-hvh-fs-01.energia.local\Energia-Users\Eanam\Desktop\UCD PROJECT\Imbalance Price Report.csv")

data4_copy = data4



# Change StartTime column to date/time
data4_copy['StartTime'] = pd.to_datetime(data4_copy['StartTime'])
# create Month, Day and Hour columns using the 'strftime' method
data4_copy['Month'] = data4_copy['StartTime'].dt.strftime('%b')
data4_copy['Day'] = data4_copy['StartTime'].dt.strftime('%A')
data4_copy['Hour'] = data4_copy['StartTime'].dt.hour
# Sort by StartTime
data4_copy = data4_copy.sort_values(by = 'StartTime')

# sort data into weekdays and months
week_days = data4_copy.sort_values(by='Day', ascending=False)
month_df = data4_copy.sort_values(by='Month', ascending=True)

# Group variables versus days
wind = data4_copy.groupby('Day')['TSORenewableForecast'].mean()

Demand = data4_copy.groupby('Day')['TSODemandForecast'].mean()

IC = data4_copy.groupby('Day')['NetInterconnectorSchedule'].mean()

totalPN =  data4_copy.groupby('Day')['TotalPN'].mean()

#Check for missing values
data4.isna().sum()

# slice part of the dataset for graphing later
Jan = data4_copy.loc[data4_copy['Month'] == 'Jan']

Feb = data4_copy.loc[data4_copy['Month'] == 'Feb']

march = data4_copy.loc[data4_copy['Month'] == 'Mar']

# iterate over the dataframe
#a = [] # Create a list
#for index, row in data4_copy.iterrows():
#    a.append(row['TSORenewableForecast'] > 2500)
#   a.append(row['TSODemandForecast'] > 3000)

#selected = [False, True]

#print(data4_copy[a])

# Seaborn plot of 4x4 variables
sns.pairplot(data4_copy[['TSODemandForecast', 'TSORenewableForecast', 'NetInterconnectorSchedule', 'TotalPN']], diag_kind='kde')

plt.plot(data4_copy.index, 'TSORenewableForecast', data=data4_copy)
plt.plot(data4_copy.index, 'TotalPN', data=data4_copy)
plt.title('Renewable vs PNs')
plt.xlabel('Date/Time')
plt.ylabel('MW')
plt.legend()
plt.show()
