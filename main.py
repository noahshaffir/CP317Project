import pandas as p
import matplotlib.pyplot as mpl
from matplotlib import pylab
from tkinter import *
data=p.read_excel("caloric_data.xlsx").iloc[:,0:]
x_axis = data['Day of month']
y_axis = data['Calories']
mean=data['Calories'].mean()
median=data['Calories'].median()
mode=data['Calories'].mode()
stdev=data['Calories'].std()
stats="\nAverage: "+str(int(mean))+", Median: "+str(int(median))+", Standard deviation: "+str(int(stdev))
win=Tk()
win.title("Daily caloric intake visualizer")
win.geometry("500x200")
radio = IntVar()
r1 = Radiobutton(win, text="Line graph", variable=radio, value=1)
r1.pack(anchor=N)
r2 = Radiobutton(win, text="Bar graph", variable=radio, value=2)
r2.pack(anchor=N)
exit_button = Button(win, text="Display graph", height=5,width=30, command=win.destroy)
exit_button.pack(pady=20)
win.mainloop()
if(radio.get()==1):
    mpl.plot(x_axis, y_axis)
    mpl.title("Daily caloric intake for the month (line graph)"+stats)
    mpl.xlabel("Day of month")
    mpl.ylabel("Calories")
    fig = pylab.gcf()
    fig.canvas.manager.set_window_title('Line graph')
    mpl.show()
else:
    if(radio.get()==2):
        mpl.bar(x_axis,y_axis)
        mpl.title("Daily caloric intake for the month (bar graph)"+stats)
        mpl.xlabel("Day of month")
        mpl.ylabel("Calories")
        fig = pylab.gcf()
        fig.canvas.manager.set_window_title('Bar graph')
        mpl.show()