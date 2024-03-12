#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 20:42:56 2022

@author: Qingyuan Zheng
"""
import requests
import datetime
import time
import pandas as pd


#the stock price 
#this data is directly downloaded 

f1=pd.read_csv('AAPL.csv')
print(f1)
del f1['Volume']
import matplotlib.pyplot as plt
f1.plot(title='stock price perform, the past one year')
plt.show()

#the stock volume 

f2=pd.read_csv('AAPL.csv')
del f2['Open']
del f2['High']
del f2['Low']
del f2['Close']
del f2['Adj Close']

f2.plot (title='stock volume, the past one year')   
plt.show


#inflation rate (we scrape this data source)
from urllib.request import urlopen  
from bs4 import BeautifulSoup
html = urlopen('https://www.usinflationcalculator.com/inflation/current-inflation-rates/#:~:text=The%20annual%20inflation%20rate%20for,ET.')

bsyc = BeautifulSoup(html.read(), "lxml")

fout = open('inflation.txt', 'wt',
		encoding='utf-8')

table_list = bsyc.findAll('table')

table = table_list[0]

rows = table.findAll('tr')
headers = rows[0].findAll('th')

#the year of inflation rate
list_year=[]
for h in headers:
    list_year.append(h)
    

#inflation rate values 
list_infv=[]
for row in rows[1:]:
    row_data = row.findAll('td')
    list_infv.append(row_data[0].contents[0].contents)
    for d in row_data[1:]:
        list_infv.append(d.contents)

list_infv.pop(11)
list_infv.pop(12)
list_infv.pop(11)

# the inflation rate from January to Octorber (that only available so far)
l1=[]
for i in list_infv[1:11]:
    l=i[0]
    l1.append(l)

dict_inflv={list_infv[0][0]:l1[0:10]}
dict_inflv_df = pd.DataFrame(dict_inflv ,index=['Jan', 'Feb','Mar','April','May'
                             ,'June','July','Agust','Sep','Oct'])
print(dict_inflv_df)

plt.figure(figsize=(4,2),dpi=100)
game=['Jan', 'Feb','Mar','April','May'
                             ,'June','July','Agust','Sep','Oct']
scores=[7.5,7.9,8.5,8.3,8.6,9.1,8.5,8.3,8.2,7.7]
plt.plot(game, scores)
plt.show()

#market momentum
#market momentum is calculate by current price subtract the price of 10 days ago 
#we use the high price of each day to do this
f2=f1['High']
list_hp=[]
for i in f2:
    list_hp.append(i)

i=0
list_mm=[]
while i <= len(list_hp)-10:
    mm=list_hp[i+9]-list_hp[i]
    list_mm.append(mm)
    i=i+1

market_momentum_df=pd.DataFrame(list_mm, 
            columns = ['market momentum'])    

    
market_momentum_df.plot(title='Market Momentum in 2022')
plt.show()
  
#the average personal consumption expenditure in US
#this data is directly downloaded 
f_=pd.read_csv('Consumption.csv')
print(f_[3:55])



#prediction 









