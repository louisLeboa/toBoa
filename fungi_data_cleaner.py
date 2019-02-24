import numpy as np
import pandas as pd

#imports the fungi_data
fungi_data = pd.read_csv("0045302-181108115102211.csv",  delimiter = "\t")

#Shows the head
fungi_data.head()

#Shows the columns
fungi_data.columns
I
print("hello")
print("bye")

print("my oh my")

#%%
msg = "Hello World"
print(msg)
#%%
msg = "good bye world"
print(msg)

import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = [trace0, trace1]

py.plot(data, filename = 'basic-line', auto_open=True)





import plotly.plotly as py
import plotly.graph_objs as go

import plotly
import plotly.graph_objs as go

plotly.offline.plot({
    "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
    "layout": go.Layout(title="hello world")
}, auto_open=True)
