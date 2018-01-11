import plotly.plotly as py
import plotly
from plotly import __version__
from plotly.offline import download_plotlyjs, plot, iplot
import plotly.graph_objs as go
import numpy as np
print __version__
from random import randint
import pandas as pd

# Need to pivot data from the csv
df = pd.read_csv('timesheet.csv', parse_dates=[4])
blogs = df.blog.unique()
print blogs
df['dates'] = df['date']
df = df.pivot_table(values = 'followers',index = 'date', columns = ['blog'], aggfunc = 'first')

print df


lines = []
for blog in blogs:
    newline = go.Scatter(
        x=df.index,
        y=df[blog],
        name = blog,
        # randomise colour
        line = dict(color = ('%06X' % randint(0, 0xFFFFFF))),
        opacity = 0.8)
    lines.append(newline)

data = lines

layout = dict(
    title='Tumblr follower time series',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(),
        type='date'
    )
)
fig = dict(data=data, layout=layout)
# online / offline
plotly.offline.plot(fig, filename = "Tumblr timeseries")