import pandas as pd
from datetime import datetime

import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import json

#load dataset
df = pd.read_csv("covid_country_data_perc.csv", index_col=0, na_filter=False, parse_dates=['Year-Month'], dtype={"Country/Region": str})

with open('/Users/keke/Desktop/Data-Visualization/countries.geojson') as response:
    counties = json.load(response)
