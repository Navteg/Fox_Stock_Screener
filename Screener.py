import pandas as pd
from pandas import ExcelWriter
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf

filename = (r'C:\Users\DELL\Downloads\StockData.xlsx')


%matplotlib inline

SPX = pd.read_excel(filename).round(15)
SPX = SPX.tail(5)
writer = ExcelWriter("ScreenOutput.xlsx")
SPX.to_excel(writer, "Sheet1")
writer.save()

SPX.iloc[:,0]= pd.to_datetime(SPX.iloc[:,1],format = "%d-%m-%y")
SPX = SPX.set_index(pd.DatetimeIndex(SPX['Date']))
mpf.plot(SPX,type = "candle",mav = 5)
# print(SPX.head())
