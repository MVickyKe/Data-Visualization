from dash import Dash
import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output




app = Dash(__name__)

# -- Import and clean data (importing csv into pandas)
# df = pd.read_csv("intro_bees.csv")
df = pd.read_csv("/Users/keke/Desktop/map/covid_country_data_perc.csv")

#df = df.groupby(['Country/Region'])[['Confirmed_Case']].max()
#df.reset_index(inplace=True)
df.drop(df.columns[[0, 2,3,8,9,10]], axis = 1, inplace = True)

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Covid-19 Web Application Dashboards", style={'text-align': 'center'}),

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
                 #style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={})

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The type chosen by user was: {}".format(option_slctd)

    dff = df.copy()
    dff = dff.groupby(['Country/Region'])[[option_slctd]].max()
    dff.index.name = "Country/Region"
    dff.reset_index(inplace=True)
    #dff = dff[dff["Year"] == option_slctd]
    #dff = dff[dff["Affected by"] == "Varroa_mites"]

    # Plotly Express
    # fig = px.choropleth(
    #     data_frame=dff,
    #     locationmode='country names',
    #     locations='Country/Region',
    #     scope="world",
    #     color=dff.iloc[:, 1],
    #     hover_data=['Country/Region', dff[option_slctd]],
    #     color_continuous_scale=px.colors.sequential.Sunsetdark,
    #     #labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
    #     template='plotly_dark'
    # )

 #   Plotly Graph Objects (GO)
    fig = go.Figure(
        data=[go.Choropleth(
            locationmode='country names',
            locations=dff['Country/Region'],
            z=dff[option_slctd],
            colorscale='Reds',
        )]
    )
    
    fig.update_layout(
        title_text="Covid 19 Cases Report",
        title_xanchor="center",
        title_font=dict(size=24),
        title_x=0.5,
        geo=dict(scope='world'),
    )

    return container, fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)