"""
SpaceX Falcon 9 — Interactive Dashboard
Author: Piyu

A Plotly Dash app to explore launch outcomes by site and payload mass.
Run locally with: python app.py
"""
import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

df = pd.read_csv('data/dataset_part_2.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('SpaceX Falcon 9 Launch Records Dashboard', style={'textAlign': 'center'}),

    html.Div([
        html.Label('Select Launch Site:'),
        dcc.Dropdown(
            id='site-dropdown',
            options=[{'label': 'All Sites', 'value': 'ALL'}] +
                    [{'label': s, 'value': s} for s in df['LaunchSite'].unique()],
            value='ALL',
            placeholder='Select a Launch Site',
        ),
    ], style={'width': '50%', 'margin': '0 auto'}),

    dcc.Graph(id='success-pie-chart'),

    html.Div([
        html.Label('Payload Mass Range (kg):'),
        dcc.RangeSlider(
            id='payload-slider',
            min=0, max=int(df['PayloadMass'].max()) + 500, step=500,
            value=[0, int(df['PayloadMass'].max()) + 500],
            marks={i: str(i) for i in range(0, int(df['PayloadMass'].max()) + 1000, 2000)},
        ),
    ], style={'width': '80%', 'margin': '20px auto'}),

    dcc.Graph(id='payload-scatter-chart'),
])


@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def update_pie(selected_site):
    if selected_site == 'ALL':
        fig = px.pie(df, names='LaunchSite', values='Class',
                     title='Total Successful Launches by Site')
    else:
        site_df = df[df['LaunchSite'] == selected_site]
        outcome_counts = site_df['Class'].value_counts().reset_index()
        outcome_counts.columns = ['Class', 'count']
        fig = px.pie(outcome_counts, names='Class', values='count',
                     title=f'Success vs. Failure for {selected_site}')
    return fig


@app.callback(
    Output('payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'), Input('payload-slider', 'value')]
)
def update_scatter(selected_site, payload_range):
    low, high = payload_range
    filtered = df[(df['PayloadMass'] >= low) & (df['PayloadMass'] <= high)]
    if selected_site != 'ALL':
        filtered = filtered[filtered['LaunchSite'] == selected_site]
    fig = px.scatter(filtered, x='PayloadMass', y='Class', color='Orbit',
                      title='Payload Mass vs. Launch Outcome', hover_data=['LaunchSite'])
    return fig


if __name__ == '__main__':
    app.run(debug=True)
