from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
import re
#=======================================================================
browser = webdriver.Firefox()
browser.get('https://www.cmegroup.com/markets/fx/g10/euro-fx.contractSpecs.options.html#optionProductId=10301')
time.sleep(3)
#------------------------------------------------------------------------
browser.find_element(By.XPATH , '//*[@id="onetrust-accept-btn-handler"]').click()
time.sleep(1)
#click on volume/oi
browser.find_element(By.XPATH , '//*[@id="main-content"]/div/div[3]/div[2]/div/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div[7]/div/a').click()
time.sleep(0.5)
browser.execute_script('window.scrollTo(0,1000)')
time.sleep(3)
browser.execute_script('window.scrollTo(0,1500)')
time.sleep(3)
browser.execute_script('window.scrollTo(0,2600)')
time.sleep(3)
#click on load more
browser.find_element(By.XPATH , '/html/body/main/div/div[3]/div[3]/div/div/div/div/div/div[2]/div/div/div/div/div/div[9]/div/div/div[2]/div[2]/button').click()
time.sleep(2)
##browser.execute_script('window.scrollTo(500,0)')
##time.sleep(2)
i = 1
Radif=""
#NameData = []
#EcoDataInx= []
while True:
                try:                                            
                        Strike =browser.find_element(By.XPATH , '//*[@id="productTabData"]/div/div/div/div/div/div[2]/div/div/div/div/div/div[9]/div/div/div[1]/div/table/tbody/tr['+str(i)+']/td[1]').text
                        Globex =browser.find_element(By.XPATH , '//*[@id="productTabData"]/div/div/div/div/div/div[2]/div/div/div/div/div/div[9]/div/div/div[1]/div/table/tbody/tr['+str(i)+']/td[2]').text
                        #NameIndex = NameIndex1 + " " + NameIndex2
                        #NameData.append(NameIndex)
                        #===========================
                        #EcoDataIn =[]
                        At_Close =browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/div[3]/table/tbody[3]/tr['+str(i)+']/td[7]').text
                        #Forecastnumbers = re.sub(r'[^\d.-]', '', Forecast)
                        #EcoDataIn.append(Forecastnumbers)
                        #--------------------------------------
                        Change =browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/div[3]/table/tbody[3]/tr['+str(i)+']/td[6]').text
                        #Consensusnumbers = re.sub(r'[^\d.-]', '', Consensus)
                        #EcoDataIn.append(Consensusnumbers)
                        #--------------------------------------
                        #===========================
                        #EcoDataInx.append(EcoDataIn)
                        #===========================
                        Radif +='📊'+" Strike: " + Strike +"  " +"\n"
                        Radif +='⏰'+" Globex: " + Globex +"  " +"\n"
                        Radif +='🔴'+" At_Close: " + At_Close +"\n"
                        Radif +='🔴'+" Change: " + Change +"\n""\n"
                        #===========================
                        i+=1
                        print(Radif)
                except NoSuchElementException:
                        print("Element not found")
                        i = 1 # Reset i for the next tbody
                        break
#=================================================================== 
print(Radif)
f = open("Radif.txt", "a")   
f.write(Radif)
f.close()
browser.quit()
#===================================================================
#print(NameData)
#print(EcoDataInx)
'''alldata = str(NameData) + "\n" + str(EcoDataInx)
f = open("Economic-Calender-Data_analysis.txt", "a")
f.write(alldata)
f.close()
#=========================================================
#======================DataFrames=========================
#=========================================================
topic = ['Forecast','Consensus','Previous']
df1 = pd.DataFrame(data=EcoDataInx,index=NameData,columns=topic)
DFstr=df1.to_string(index=True)
df2 = pd.DataFrame(data=EcoDataInx2,index=NameData2,columns=topic)
df3 = pd.DataFrame(data=EcoDataInx3,index=NameData3,columns=topic)
#-----------------------------------------------------
Bearish1 = df1[(df1['Forecast'] < df1['Consensus']) &
        (df1['Forecast'] < df1['Previous'])]
Bearish1 = Bearish1[['Forecast','Previous','Consensus']]
Bearishdata1_str_with_index = Bearish1.to_string(index=True)
Bearishtext= "Bearish Index wednesday"+"\n""\n"
Bearishtext += Bearishdata1_str_with_index
f = open("Bearish.txt", "a")   
f.write(Bearishtext)
f.close()
#-----------------------------------------------------
Bullish1 = df1[(df1['Forecast'] > df1['Consensus']) &
        (df1['Forecast'] > df1['Previous'])]
Bullish1 = Bullish1[['Forecast','Previous','Consensus']]
Bullishdata1_str_with_index = Bullish1.to_string(index=True)
Bullishtext= "Bullish Index wednesday"+"\n""\n"
Bullishtext += Bullishdata1_str_with_index
f = open("Bullish.txt", "a")   
f.write(Bullishtext)
f.close()
#-----------------------------------------------------
#-----------------------------------------------------
Bearish2 = df2[(df2['Forecast'] < df2['Consensus']) &
        (df2['Forecast'] < df2['Previous'])]
Bearish2 = Bearish2[['Forecast','Previous','Consensus']]
Bearishdata2_str_with_index = Bearish2.to_string(index=True)
Bearishtext= "\n""\n"+"Bearish Index Thursday "+"\n""\n"
Bearishtext += Bearishdata2_str_with_index
f = open("Bearish.txt", "a")   
f.write(Bearishtext)
f.close()
#-----------------------------------------------------
Bullish2 = df2[(df2['Forecast'] > df2['Consensus']) &
        (df2['Forecast'] > df2['Previous'])]
Bullish2 = Bullish2[['Forecast','Previous','Consensus']]
Bullishdata2_str_with_index = Bullish2.to_string(index=True)
Bullishtext= "\n""\n"+"Bullish Index Thursday "+"\n""\n"
Bullishtext += Bullishdata2_str_with_index
f = open("Bullish.txt", "a")   
f.write(Bullishtext)
f.close()
#-----------------------------------------------------
#-----------------------------------------------------
Bearish3 = df3[(df3['Forecast'] < df3['Consensus']) &
        (df3['Forecast'] < df3['Previous'])]
Bearish3 = Bearish3[['Forecast','Previous','Consensus']]
Bearishdata3_str_with_index = Bearish3.to_string(index=True)
Bearishtext= "\n""\n"+"Bearish Index Friday "+"\n""\n"
Bearishtext += Bearishdata3_str_with_index
f = open("Bearish.txt", "a")   
f.write(Bearishtext)
f.close()
#-----------------------------------------------------
Bullish3 = df3[(df3['Forecast'] > df3['Consensus']) &
        (df3['Forecast'] > df3['Previous'])]
Bullish3 = Bullish3[['Forecast','Previous','Consensus']]
Bullishdata3_str_with_index = Bullish3.to_string(index=True)
Bullishtext= "\n""\n"+"Bullish Index Friday "+"\n""\n"
Bullishtext += Bullishdata3_str_with_index
f = open("Bullish.txt", "a")   
f.write(Bullishtext)
f.close()
#-----------------------------------------------------
print(EcoDataInx)
f = open("Economic-Calender-Data_analysis2.txt", "a")
f.write(DFstr)
f.close()
'''
