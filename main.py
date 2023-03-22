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

def on_button_click(ticker1, ticker2, start, end, indicators):
    pass


def display_about():
    print("implement later")

stock1_text = TextInput(title="Stock 1")
stock2_text = TextInput(title="Stock 2")
date_picker_from= DatePicker(title="Start Date", value="2019-01-01",min_date="2000-01-01", max_date=datetime.datetime.now().strftime("%Y-%m-%d"))
date_picker_to= DatePicker(title="End Date", value="2020-01-01",min_date="2000-01-01", max_date=datetime.datetime.now().strftime("%Y-%m-%d"))

indicator_choice = MultiChoice(options=["100 days' average", "30 days' average", "Linear regression"])

load_button=Button(label="Display results")
load_button.on_click(lambda: on_button_click(stock1_text.value,stock2_text.value,date_picker_from.value,date_picker_to.value,indicator_choice.value,load_button))

layout = row(stock1_text,stock2_text,date_picker_from,date_picker_to,indicator_choice, load_button)

curdoc().clear()
curdoc().add_root(layout)

