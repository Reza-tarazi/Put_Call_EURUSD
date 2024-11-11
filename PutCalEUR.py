#In the previous code, it was related to web scraping from the site, but because it was an easier way, we preferred to change it
import pandas as pd
#====================
#https://www.cmegroup.com/tools-information/quikstrike/options-calendar-fx.html
#You can choose your desired day from the desired site and then download the desired file in the Volemw/OI section. Then examine the Excel file
c = pd.read_excel("EURUSD-Mon.xls")
#-------------------------------------
#Now we have to separate the call and put data for each part and adjust the rows and columns like Excel and according to our desired data.
fc= fc.iloc[19:,:10]
fc.columns = fc.iloc[1]
fc.index=fc.Strike
fc.drop("Strike",axis=1,inplace=True)
call=fc.iloc[:45]
put = fc.iloc[46:98]
#-------------------------------------
#In this step, we have to separate that part of the data where the orders have changed for each part
call2 = call.iloc[2:]
call2['Globex'] = pd.to_numeric(call2['Globex'], errors='coerce')
call2 = call2.dropna(subset=['Globex'])
result = call2[call2['Globex'] >= 1]
print(result)
#-------------------------------------
put['Globex'] = pd.to_numeric(put['Globex'], errors='coerce')
put = put.dropna(subset=['Globex'])
result2 = put[put['Globex'] >= 1]
print(result2)
#The number of indexes to separate data is different for each Excel. So be sure to check it yourself
