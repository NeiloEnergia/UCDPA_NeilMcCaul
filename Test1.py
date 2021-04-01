#Neil McCaul
import pandas as pd
#Importing CSVs download from the semopx website. Dynamic report section

#Eirgrid Wind forecast data from the SEMOPX website
data_wind = pd.read_csv(r"\\vir-hvh-fs-01.energia.local\Energia-Users\Eanam\Desktop\UCD PROJECT\Aggregated Eir Wind Forecast.csv")
data_wind.head()

#Eigrid electricity demand forecast from SEMOPX website
data_demand = pd.read_csv(r"\\vir-hvh-fs-01.energia.local\Energia-Users\Eanam\Desktop\UCD PROJECT\Daily Load Forecast Summary.csv")
data_demand.tail()

#Eigrid electricity Imbalance price from SEMOPX website
data_imbalance = pd.read_csv(r"\\vir-hvh-fs-01.energia.local\Energia-Users\Eanam\Desktop\UCD PROJECT\Imbalance Price Report.csv")
data_imbalance.tail()

#Physical notifications (Power plants running in Ireland)
data_pn = pd.read_csv(r"\\vir-hvh-fs-01.energia.local\Energia-Users\Eanam\Desktop\UCD PROJECT\Final Physical Notification.csv")
data_pn.tail()

#how in balance is the Iirsh power system
data_fc_imb = pd.read_csv(r"\\vir-hvh-fs-01.energia.local\Energia-Users\Eanam\Desktop\UCD PROJECT\Forecast Imbalance.csv")
data_fc_imb.tail()
