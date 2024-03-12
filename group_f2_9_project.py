# Group F2-9 Project Source Code
# Group Members
# Qingyuan Zheng  |  qingyuaz
# Frank Zhao      |  yanzhiz
# Yuvraj Mehra    |  ymehra
# Peter Previte   |  pprevite
# Yuding Wang     |  yudingw

# Code Overview - a user will input a stock ticker (4 digits) as well as a start and end date
#  The program will then return plots for the stock price of that stock over the time period given
#  as well as the market momentum during that time period

import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt


# Main function gets the user input, scrapes using Beautiful Soup, and generates the plots

def main():
    while True:
        stock = input("Welcome, which stock would you like to analyze today?: (tickers such as AAPL, NFLX): ")
        start_date = input("Please input the start date (YYYY-MM-DD): ")
        end_date = input("Please input the end date (YYYY-MM-DD): ") 
        try:
            stock_df = web.get_data_yahoo(stock, start = start_date, end = end_date)
            break
        except:
            print('Invalid Inputs, Please Try Again!')
    print("We start by analyzing the stock price over the time period")
    stock_df["Adj Close"].plot()
    plt.xlabel("Date")
    plt.ylabel("Adjusted Close")
    plt.title( "Stock Price data")
    plt.show()
    print("We then calculate the daily returns and plot those")
    stock_df['Daily_Returns'] = stock_df['Adj Close'].pct_change()
    stock_df['Daily_Returns'].plot()
    plt.xlabel("Date")
    plt.ylabel("Daily Return")
    plt.title( "Stock Price Performance")
    plt.show()
    print("We proceed with plotting some other important information")
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

    # the inflation rate from January to October (that only available so far)
    l1=[]
    for i in list_infv[1:11]:
        l=i[0]
        l1.append(l)

    dict_inflv={list_infv[0][0]:l1[0:10]}
    dict_inflv_df = pd.DataFrame(dict_inflv ,index=['Jan', 'Feb','Mar','April','May'
                                ,'June','July','Agust','Sep','Oct'])
    #print(dict_inflv_df)

    plt.figure(figsize=(4,2),dpi=100)
    game=['Jan', 'Feb','Mar','April','May'
                                ,'June','July','Agust','Sep','Oct']
    scores=[7.5,7.9,8.5,8.3,8.6,9.1,8.5,8.3,8.2,7.7]
    plt.plot(game, scores)
    plt.show()

    #market momentum
    #market momentum is calculated by current price subtract the price of 10 days ago 
    #we use the high price of each day to do this
    f2=stock_df['High']
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
    return 1

main()
