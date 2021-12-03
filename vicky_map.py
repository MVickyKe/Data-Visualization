import pandas as pd
import numpy as np
from datetime import datetime
import dash
from dash import Dash
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import json

#load dataset
df = pd.read_csv("covid_country_data_perc.csv", index_col=0, na_filter=False, parse_dates=['Year-Month'], dtype={"Country/Region": str})

#with open('/Users/keke/Desktop/Data-Visualization/countries.geojson') as response:
#    counties = json.load(response)

app = Dash(__name__)

app.layout = html.Div(children = [
    # title
    html.H1('Covid Cases Visualization Dashboard',
           style={
            'textAlign': 'center',
            'color': "black"
    }),


    ############################################ block1: map radio items
    html.Div([
        html.H2("Covid Cases Map", style={'textAlign': 'center'}),
        dcc.RadioItems(id="slct_year",
                 options=[
                     {"label": "Confirmed Case", "value": "Confirmed_Case"},
                     {"label": "Deaths Case", "value": "Deaths_Case"},
                     {"label": "Recovered Case", "value": "Recovered_Case"}],
                 value="Confirmed_Case",
                 #labelStyle={'display': 'flex'}
                 labelStyle={
                    'display': 'flex',
                    'margin-right': '10px',
                    'font-weight': 500
                 },
    ),
    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={})

])])

@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)


def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The type chosen by user was: {}".format(option_slctd)

    map_data = df.copy()
    map_data = map_data.groupby(['Country/Region'])[[option_slctd]].max()

    map_data.index.name = "Country/Region"
    map_data.reset_index(inplace=True)
    map_data_final = map_data.rename(columns={'Country/Region': 'Country'})


    #   Plotly Graph Objects (GO)
    fig = go.Figure(
        data=[go.Choropleth(
            locationmode='country names',
            locations=map_data_final['Country'],
            z = map_data_final[option_slctd],
            colorscale='Blues'
        )]
    )
    
    fig.update_layout(
        geo=dict(scope='world'),
    )

    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    return container, fig

if __name__ == '__main__':
    app.run_server(debug=True)