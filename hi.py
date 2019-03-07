import plotly as py
import plotly.graph_objs as go

plotly.offline.plot({
    "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
    "data" = [go.Bar(
                x=['giraffes', 'orangutans', 'monkeys'],
                y=[20, 14, 23]
        )]
    "layout": go.Layout(title="hello world") })
data = [go.Bar(
            x=['giraffes', 'orangutans', 'monkeys'],
            y=[20, 14, 23]
    )]
