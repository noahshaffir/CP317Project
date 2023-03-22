import math
import datetime 
import numpy 
import yfinance 
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.layouts import row, column
from bokeh.models import TextInput, Button, DatePicker, MultiChoice

def load_data(ticker1, ticker2, start,end):
    data1 = yfinance.download(ticker1, start, end)
    data2 = yfinance.download(ticker2, start, end)
    return data1, data2


def plot(data, indicators, sync_axis=None):
    pass

def on_click(ticker1, ticker2, start, end, indicators):
    pass

stock1_test = TextInput(title="Stock 1")
stock2_test = TextInput(title="Stock 2")
date_picker_from= DatePicker(title="Start Date", value="2022-04-07",min_date=datetime.datetime.now().strftime("%Y-%m-%d"))