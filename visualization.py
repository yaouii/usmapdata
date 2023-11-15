import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv('https://github.com/marestaing/hosting/blob/main/visited_states.csv?raw=true')

fig = go.Figure(data=go.Choropleth(
    locations=df['code'], # Spatial coordinates
    z = df['number students'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'dense',
    colorbar_title = "most to least visited states",
))

fig.update_layout(
    title_text = 'ap computer science u.s. map cool',
    geo_scope='usa', # limite map scope to USA
)

fig.show()