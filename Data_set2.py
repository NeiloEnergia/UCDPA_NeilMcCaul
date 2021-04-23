#Neil McCaul

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Eigrid electricity demand forecast from SEMOPX website
data2 = pd.read_csv(r"\\vir-hvh-fs-01.energia.local\Energia-Users\Eanam\Desktop\UCD PROJECT\Daily Load Forecast Summary.csv")

#how in balance is the Iirsh power system
data4 = pd.read_csv(r"\\vir-hvh-fs-01.energia.local\Energia-Users\Eanam\Desktop\UCD PROJECT\Forecast Imbalance.csv")

# making a copy of data in case of mistakes
data4_copy = data4

# merge dataframes together - due to duplicate columns in both data frames for example "start time" merge data frames with the columns that arent the same
# Get the columns we need from the second dataframe to avoid duplicating columns - Notes: Getting the difference between data set 2 & 4
columns_needed = data2.columns.difference(data4_copy.columns)
# Merge dataframes using pandas
df = pd.merge(data4_copy, data2[columns_needed], left_index = True, right_index = True, how="outer")


# Change StartTime column to date/time format
df['StartTime'] = pd.to_datetime(df['StartTime'])
# create Month, Day and Hour columns using the 'starftime' method in chronological order
df['Month'] = df['StartTime'].dt.strftime('%b')
df['Day'] = df['StartTime'].dt.strftime('%A')
df['Hour'] = df['StartTime'].dt.hour
# Sort by StartTime
df = df.sort_values(by = 'StartTime')

#Check for missing values
df.isna().sum()

# iterate over the dataframe and return boolean values for condition
#Going through the data set to check when TSO renewable forecast colum is greater then 5000
a = [] # Create a list to store true or false values
for index, row in df.iterrows():
    a.append(row['TSORenewableForecast'] > 5000)

high_wind = df[a] # filter dataframe by list to return rows of higher than 5000 values
# this shows errors in the dataset that need to be removed ude to the fact that there is not more than 5000mw of wind on the system
# Remove errors from dataset
df = df.drop(high_wind.index)

# sort data into weekdays and months
week_days = df.sort_values(by='Day', ascending=False)
month_df = df.sort_values(by='Month', ascending=True)

# Group variables versus days
wind = df.groupby('Day')['TSORenewableForecast'].mean()
#create bar chart
plt.figure()
plt.bar(wind.index, wind.values, align='center', alpha=0.5)
plt.ylabel('MW')
plt.title('Average Wind per Day')
# Demand (note demand lower on weekends due to non working day)
Demand = df.groupby('Day')['TSODemandForecast'].mean()
# create bar chart
plt.figure()
plt.bar(Demand.index, Demand.values, align='center', alpha=0.5)
plt.ylabel('MW')
plt.title('Average Demand per Day')
# Interconnectors
IC = df.groupby('Day')['NetInterconnectorSchedule'].mean()
#create bar chart
plt.figure()
plt.bar(IC.index, IC.values, align='center', alpha=0.5)
plt.ylabel('MW')
plt.title('Average IC values per Day')
#total Physical notications (generation capcity of power plants on the irish system)
totalPN =  df.groupby('Day')['TotalPN'].mean()
# create bar chart
plt.figure()
plt.bar(totalPN.index, totalPN.values, align='center', alpha=0.5)
plt.ylabel('MW')
plt.title('Average PNs per Day')
#plt.show()

NIV = df.groupby('Day')['CalculatedImbalance'].mean()
plt.figure()
plt.bar(NIV.index, NIV.values, align='center', alpha=0.5)
plt.ylabel('MW')
plt.title('Average of NIV per Day')
# slice part of the dataset for graphing later
Jan = df.loc[df['Month'] == 'Jan']

Feb = df.loc[df['Month'] == 'Feb']

march = df.loc[df['Month'] == 'Mar']

# Create line graph of the impact of high and low wind on the requirement for power plant generation on the system. Low wind Higher capacity required and vice versa
fig = plt.plot(df.StartTime, 'TSORenewableForecast', data=df)
plt.plot(df.StartTime, 'TotalPN', data=df)
plt.title('Renewable vs PNs')
plt.xlabel('Date/Time')
plt.ylabel('MW')
plt.legend()
# plt.show()

# Seaborn plot of 4x4 variables
fig1 = sns.pairplot(df[['TSODemandForecast', 'TSORenewableForecast', 'NetInterconnectorSchedule', 'TotalPN']], diag_kind='kde')

print("script complete")



