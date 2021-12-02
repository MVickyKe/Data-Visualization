import pandas as pd
from datetime import datetime

import dash
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

# Reference: https://docs.google.com/document/d/1O76ws8azib9Nf6pYlqf_4w8jklBfdRKvh-WwVL1mcmE/edit

#%%%% Read Data

# by_month Data
country_data = pd.read_csv("covid_country_data.csv", index_col=0, na_filter=False, parse_dates=['Year-Month'])
continent_data = pd.read_csv("covid_continent_data.csv", index_col=0, na_filter=False, parse_dates=['Year-Month'])

# by_date Data
country_data_bydate = pd.read_csv("covid_country_bydate.csv", index_col=0, na_filter=False, parse_dates=['Date'])
continent_data_bydate = pd.read_csv("covid_continent_bydate.csv", index_col=0, na_filter=False, parse_dates=['Date'])

#%%%% Dashboard
# https://dash.plot.ly/dash-core-components/dropdown
# We need to construct a dictionary of dropdown values for the years
    
app = dash.Dash()

# get all continent options
continent_options = []
for continent in continent_data['Continent_Name'].unique():
    continent_options.append({'label':continent,'value':continent})

# get all country optioins
country_options = []
for country in country_data_bydate['Country/Region'].unique():
    country_options.append({'label':country,'value':country})

# start building our dashboard
app.layout = html.Div(children = [
    # title
    html.H1('Covid Cases Visualization Dashboard',
           style={
            'textAlign': 'center',
            'color': "black"
    }),

    ############################################ block1: Continent Cases by Month
    # drop down
    html.Div([
        html.H2("Covid Cases by Continent & Month", style={'textAlign': 'center'}),
        dcc.Dropdown(id='continent_picker_block1',options= continent_options, value="North America")
    ],style={
            'textAlign': 'center',
            'color': "black",
            'backgroundColor': "white",
            }
    ),
    # add a Button element
    html.Div([
        html.Button(
            id='submit_button_block1',
            n_clicks=0,
            children='Submit',
            style={'fontSize':16}
        ),
    ], style={'display':'inline-block'}),

    #graph
    html.Div([
        dcc.Graph(id='continent_month_graph')
    ],style={'backgroundColor': "white"}),

    ############################################ block2: Country Cases by Month
    #### 1
    html.H2("Covid Cases by Country & Month", style={'textAlign': 'center'}),
    html.Div([
        # drop down
        html.Div([
            html.H3('Confirmed Cases:', style={'paddingRight':'30px'}),
            dcc.Dropdown(
                id='country_picker_confirm_block2',
                options=country_options,
                value=['US'],
                multi=True
            )],style={
                'color': "black",
                'backgroundColor': "white",
                'verticalAlign':'top'}
        ),

        # add a Button element
        html.Div([
            html.Button(
                id='submit_button0_block2',
                n_clicks=0,
                children='Submit',
                style={'fontSize':16}
            ),
        ], style={'display':'inline-block'}),

        #graph
        html.Div([
            dcc.Graph(id='country_graph_confirm_block2')
        ])
    ], style={'display':'inline-block','verticalAlign':'top', 'width':'32%', 'border':'3px pink solid'}),   
        
    #### 2
    html.Div([
        # another drop down
        html.Div([
            html.H3('Death Cases:', style={'paddingRight':'30px'}),
            dcc.Dropdown(
                id='country_picker_death_block2',
                options=country_options,
                value=['US'],
                multi=True
            )],style={
                'color': "black",
                'backgroundColor': "white",
                'verticalAlign':'top'}
        ),

        # add a Button element
        html.Div([
            html.Button(
                id='submit_button1_block2',
                n_clicks=0,
                children='Submit',
                style={'fontSize':16}
            ),
        ], style={'display':'inline-block'}),

        #graph
        html.Div([
            dcc.Graph(id='country_graph_death_block2')
        ])
    ], style={'display':'inline-block','verticalAlign':'top', 'width':'32%', 'border':'3px pink solid'}),

    #### 3
    html.Div([
        # another drop down
        html.Div([
            html.H3('Recovered Cases:', style={'paddingRight':'30px'}),
            dcc.Dropdown(
                id='country_picker_recover_block2',
                options=country_options,
                value=['US'],
                multi=True
            )],style={
                'color': "black",
                'backgroundColor': "white",
                'verticalAlign':'top'}
        ),

        # add a Button element
        html.Div([
            html.Button(
                id='submit_button2_block2',
                n_clicks=0,
                children='Submit',
                style={'fontSize':16}
            ),
        ], style={'display':'inline-block'}),

        #graph
        html.Div([
            dcc.Graph(id='country_graph_recover_block2')
        ])
    ], style={'display':'inline-block','verticalAlign':'top', 'width':'32%', 'border':'3px pink solid'}),

    ############################################ block3: Continent Cases by Date
    html.H2("Covid Cases by Continent & Date", style={'textAlign': 'center'}),
    # drop down
    html.Div([
        html.H3("Monthly Covid Cases by Continent:"),
        dcc.Dropdown(id='continent_picker_block3',options=continent_options, value="North America")
    ],style={
            'textAlign': 'center',
            'color': "black",
            'backgroundColor': "white",
            'display':'inline-block',
            'verticalAlign':'top', 
            'width':'30%'}
    ),

    html.H3("", style={'display':'inline-block', 'width':'2%'}),

    # date picker
    html.Div([
    html.H3('Start & End dates:'),   
    dcc.DatePickerRange(
        id='my_date_picker_block3',
        min_date_allowed = datetime(2020, 1, 22),
        max_date_allowed = datetime(2021, 11, 6),
        start_date = datetime(2021, 6, 1),
        end_date = datetime(2021, 11, 6)
    )], style={'display':'inline-block', 
                'width':'30%'}),
    
    # add a Button element
    html.Div([
        html.Button(
            id='submit_button_block3',
            n_clicks=0,
            children='Submit',
            style={'fontSize':16}
        ),
    ], style={'display':'inline-block'}),

    #graph
    html.Div([
        dcc.Graph(id='continent_date_graph_block3')
    ],style={'backgroundColor': "white"}),

    ############################################ block4: Country Cases by Date
    html.H2("Covid Cases by Country & Date", style={'textAlign': 'center'}),
    #### 1
    html.Div([
        # drop down
        html.Div([
            html.H3('Confirmed Cases:', style={'paddingRight':'40px'}),
            dcc.Dropdown(
                id='country_picker_confirm_block4',
                options=country_options,
                value=['US'],
                multi=True
            )],style={
                'color': "black",
                'backgroundColor': "white",
                'verticalAlign':'top'}
        ),
        
        # date picker
        html.Div([
        html.H3('Start & End dates:'),   
        dcc.DatePickerRange(
            id='my_date_picker0_block4',
            min_date_allowed = datetime(2020, 1, 22),
            max_date_allowed = datetime(2021, 11, 6),
            start_date = datetime(2021, 6, 1),
            end_date = datetime(2021, 11, 6),

        )], style={'display':'inline-block', 
                    'width':'30%'}),

        # add a Button element
        html.Div([
            html.Button(
                id='submit_button0_block4',
                n_clicks=0,
                children='Submit',
                style={'fontSize':16}
            ),
        ], style={'display':'inline-block'}),

        #graph
        html.Div([
            dcc.Graph(id='country_graph_confirm_block4')
        ])
    ], style={'display':'inline-block','verticalAlign':'top', 'width':'48.75%', 'border':'3px plum solid'}),
    
    html.H3("", style={'display':'inline-block', 'width':'0.75%'}),

    #### 2
    html.Div([
        # another drop down
        html.Div([
            html.H3('Death Cases:', style={'paddingRight':'30px'}),
            dcc.Dropdown(
                id='country_picker_death_block4',
                options=country_options,
                value=['US'],
                multi=True
            )],style={
                'color': "black",
                'backgroundColor': "white",
                'verticalAlign':'top'}
        ),
        
        # date picker
        html.Div([
        html.H3('Start & End dates:'),   
        dcc.DatePickerRange(
            id='my_date_picker1_block4',
            min_date_allowed = datetime(2020, 1, 22),
            max_date_allowed = datetime(2021, 11, 6),
            start_date = datetime(2021, 6, 1),
            end_date = datetime(2021, 11, 6),

        )], style={'display':'inline-block', 
                    'width':'30%'}),

        # add a Button element
        html.Div([
            html.Button(
                id='submit_button1_block4',
                n_clicks=0,
                children='Submit',
                style={'fontSize':16}
            ),
        ], style={'display':'inline-block'}),

        #graph
        html.Div([
            dcc.Graph(id='country_graph_death_block4')
        ])
    ], style={'paddingLeft':'10px', 'display':'inline-block','verticalAlign':'top', 'width':'48.75%', 'border':'3px gold solid'}),
    
    html.H4(),
    
    #### 3
    html.Div([
        # another drop down
        html.Div([
            html.H3('Recovered Cases:', style={'paddingRight':'30px'}),
            dcc.Dropdown(
                id='country_picker_recover_block4',
                options=country_options,
                value=['US'],
                multi=True
            )],style={
                'color': "black",
                'backgroundColor': "white",
                'verticalAlign':'top'}
        ),

        # date picker
        html.Div([
        html.H3('Start & End dates:'),   
        dcc.DatePickerRange(
            id='my_date_picker2_block4',
            min_date_allowed = datetime(2020, 1, 22),
            max_date_allowed = datetime(2021, 11, 6),
            start_date = datetime(2021, 6, 1),
            end_date = datetime(2021, 11, 6),

        )], style={'display':'inline-block', 
                    'width':'30%'}),
        
        # add a Button element
        html.Div([
            html.Button(
                id='submit_button2_block4',
                n_clicks=0,
                children='Submit',
                style={'fontSize':16}
            ),
        ], style={'display':'inline-block'}),

        #graph
        html.Div([
            dcc.Graph(id='country_graph_recover_block4')
        ])
    ], style={'display':'inline-block','width':'48.75%', 'border':'3px slateblue solid'})
    
],style={'backgroundColor': "white"})

############################################ Callbacks ############################################
############################################ block1: Continent Cases by Month
@app.callback(Output('continent_month_graph', 'figure'),
              [Input('submit_button_block1', 'n_clicks')],
              [State('continent_picker_block1', 'value')])

def update_figure(n_clicks, selected_country):
    filtered_df = continent_data[continent_data['Continent_Name'] == selected_country]
    
    trace0 = go.Scatter(
        x = filtered_df["Year-Month"],
        y = filtered_df["Confirmed_Case"],
        mode = 'markers+lines',
        name = "Confirmed",
        line=dict(color="plum"))

    trace1 = go.Scatter(
        x = filtered_df["Year-Month"],
        y = filtered_df["Deaths_Case"],
        mode = 'markers+lines',
        name = "Deaths",
        line=dict(color="gold"))

    trace2 = go.Scatter(
        x = filtered_df["Year-Month"],
        y = filtered_df["Recovered_Case"],
        mode = 'markers+lines',
        name = "Recovered",
        line=dict(color="slateblue"))

    traces = [trace0, trace1, trace2]
 
    return {
        'data': traces,
        'layout': go.Layout({
            'plot_bgcolor': "white",
            'paper_bgcolor': "white",
            'font': {'color': "black"}},
            xaxis={'title': 'Year-Month'},
            yaxis={'title': 'Case Numbers'},
            hovermode='closest'
        )
    }

############################################ block2: Country Cases by Month
# confirm
@app.callback(Output('country_graph_confirm_block2', 'figure'),
              [Input('submit_button0_block2', 'n_clicks')],
              [State('country_picker_confirm_block2', 'value')])
def update_figure(nlicks, selected_country):  
    traces = []
    for country in selected_country:
        filtered_df = country_data[country_data['Country/Region'] == country]
        traces.append({'x': filtered_df["Year-Month"], 
                       'y': filtered_df["Confirmed_Case"], 
                       'mode': 'markers+lines',
                       'name': country})
 
    return {
        'data': traces,
        'layout': go.Layout({
            'plot_bgcolor': "white",
            'paper_bgcolor': "white",
            'font': {'color': "black"}},
            xaxis={'title': 'Year-Month'},
            yaxis={'title': 'Confirmed Case Numbers'},
            hovermode='closest'
        )
    }

# recover
@app.callback(Output('country_graph_death_block2', 'figure'),
              [Input('submit_button1_block2', 'n_clicks')],
              [State('country_picker_death_block2', 'value')])
def update_figure(nlicks, selected_country):  
    traces = []
    for country in selected_country:
        filtered_df = country_data[country_data['Country/Region'] == country]
        traces.append({'x': filtered_df["Year-Month"], 
                       'y': filtered_df["Deaths_Case"], 
                       'mode': 'markers+lines',
                       'name': country})
 
    return {
        'data': traces,
        'layout': go.Layout({
            'plot_bgcolor': "white",
            'paper_bgcolor': "white",
            'font': {'color': "black"}},
            xaxis={'title': 'Year-Month'},
            yaxis={'title': 'Death Case Numbers'},
            hovermode='closest'
        )
    }

# recover
@app.callback(Output('country_graph_recover_block2', 'figure'),
              [Input('submit_button2_block2', 'n_clicks')],
              [State('country_picker_recover_block2', 'value')])
def update_figure(nlicks, selected_country):  
    traces = []
    for country in selected_country:
        filtered_df = country_data[country_data['Country/Region'] == country]
        traces.append({'x': filtered_df["Year-Month"], 
                       'y': filtered_df["Recovered_Case"], 
                       'mode': 'markers+lines',
                       'name': country})
 
    return {
        'data': traces,
        'layout': go.Layout({
            'plot_bgcolor': "white",
            'paper_bgcolor': "white",
            'font': {'color': "black"}},
            xaxis={'title': 'Year-Month'},
            yaxis={'title': 'Recovered Case Numbers'},
            hovermode='closest'
        )
    }

############################################ block3: Continent Cases by Date
@app.callback(Output('continent_date_graph_block3', 'figure'),
              [Input('submit_button_block3', 'n_clicks')],
            [State('continent_picker_block3', 'value'),
             State('my_date_picker_block3', 'start_date'),
             State('my_date_picker_block3', 'end_date')]
             )
def update_figure(n_clicks, selected_country, start_date, end_date):
    filtered_df = continent_data_bydate[(continent_data_bydate["Date"]>=start_date) & (continent_data_bydate["Date"]<=end_date) & (continent_data_bydate['Continent_Name'] == selected_country)]
    
    trace0 = go.Scatter(
        x = filtered_df["Date"],
        y = filtered_df["Confirmed_Case"],
        mode = 'markers+lines',
        name = "Confirmed",
        line=dict(color="plum"))

    trace1 = go.Scatter(
        x = filtered_df["Date"],
        y = filtered_df["Deaths_Case"],
        mode = 'markers+lines',
        name = "Deaths",
        line=dict(color="gold"))

    trace2 = go.Scatter(
        x = filtered_df["Date"],
        y = filtered_df["Recovered_Case"],
        mode = 'markers+lines',
        name = "Recovered",
        line=dict(color="mediumpurple"))

    traces = [trace0, trace1, trace2]
 
    return {
        'data': traces,
        'layout': go.Layout({
            'plot_bgcolor': "white",
            'paper_bgcolor': "white",
            'font': {'color': "black"}},
            xaxis={'title': 'Date'},
            yaxis={'title': 'Case Numbers'},
            hovermode='closest'
        )
    }

############################################ block4: Continent Cases by Date
############################################
# 1 --- confirm
@app.callback(Output('country_graph_confirm_block4', 'figure'),
              [Input('submit_button0_block4', 'n_clicks')],
              [State('country_picker_confirm_block4', 'value'),
               State('my_date_picker0_block4', 'start_date'),
               State('my_date_picker0_block4', 'end_date')])
def update_figure(n_clicks, selected_country, start_date, end_date):  
    traces = []
    for country in selected_country:
        filtered_df = country_data_bydate[(country_data_bydate["Date"]>=start_date) & (country_data_bydate["Date"]<=end_date) &(country_data_bydate['Country/Region'] == country)]
        traces.append({'x': filtered_df["Date"], 
                       'y': filtered_df["Confirmed_Case"], 
                       'mode': 'markers+lines',
                       'name': country})
 
    return {
        'data': traces,
        'layout': go.Layout({
            'plot_bgcolor': "white",
            'paper_bgcolor': "white",
            'font': {'color': "black"}},
            xaxis={'title': 'Date'},
            yaxis={'title': 'Confirmed Case Numbers'},
            hovermode='closest'
        )
    }

# 2 --- death
@app.callback(Output('country_graph_death_block4', 'figure'),
              [Input('submit_button1_block4', 'n_clicks')],
              [State('country_picker_death_block4', 'value'),
               State('my_date_picker1_block4', 'start_date'),
               State('my_date_picker1_block4', 'end_date')])
def update_figure(n_clicks, selected_country, start_date, end_date):  
    traces = []
    for country in selected_country:
        filtered_df = country_data_bydate[(country_data_bydate["Date"]>=start_date) & (country_data_bydate["Date"]<=end_date) &(country_data_bydate['Country/Region'] == country)]
        traces.append({'x': filtered_df["Date"], 
                       'y': filtered_df["Deaths_Case"], 
                       'mode': 'markers+lines',
                       'name': country})
 
    return {
        'data': traces,
        'layout': go.Layout({
            'plot_bgcolor': "white",
            'paper_bgcolor': "white",
            'font': {'color': "black"}},
            xaxis={'title': 'Date'},
            yaxis={'title': 'Death Case Numbers'},
            hovermode='closest'
        )
    }

# 3 --- recover
@app.callback(Output('country_graph_recover_block4', 'figure'),
              [Input('submit_button2_block4', 'n_clicks')],
              [State('country_picker_recover_block4', 'value'),
               State('my_date_picker2_block4', 'start_date'),
               State('my_date_picker2_block4', 'end_date')])
def update_figure(n_licks, selected_country, start_date, end_date):  
    traces = []
    for country in selected_country:
        filtered_df = country_data_bydate[(country_data_bydate["Date"]>=start_date) & (country_data_bydate["Date"]<=end_date) &(country_data_bydate['Country/Region'] == country)]
        traces.append({'x': filtered_df["Date"], 
                       'y': filtered_df["Recovered_Case"], 
                       'mode': 'markers+lines',
                       'name': country})
 
    return {
        'data': traces,
        'layout': go.Layout({
            'plot_bgcolor': "white",
            'paper_bgcolor': "white",
            'font': {'color': "black"}},
            xaxis={'title': 'Date'},
            yaxis={'title': 'Recovered Case Numbers'},
            hovermode='closest'
        )
    }
if __name__ == '__main__':
    app.run_server()