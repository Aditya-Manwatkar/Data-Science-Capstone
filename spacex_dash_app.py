import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    # TASK 1: Add a dropdown list to enable Launch Site selection
    dcc.Dropdown(id='site-dropdown',
                 options=[
                     {'label': 'All Sites', 'value': 'ALL'},
                     {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                     {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
                     {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                     {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'}
                 ],
                 value='ALL',
                 placeholder="Select a Launch Site",
                 searchable=True),
    html.Br(),

    # TASK 2: Add a pie chart to show the total successful launches count for all sites
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),
    # TASK 3: Add a slider to select payload range
    dcc.RangeSlider(id='payload-slider',
                    min=min_payload,
                    max=max_payload,
                    step=1000,
                    marks={i: str(i) for i in range(int(min_payload), int(max_payload) + 1, 5000)},
                    value=[min_payload, max_payload]),

    # TASK 4: Add a scatter chart to show the correlation between payload and launch success
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# TASK 2 Callback: Update pie chart based on site selection
@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def update_pie_chart(selected_site):
    if selected_site == 'ALL':
        df = spacex_df
    else:
        df = spacex_df[spacex_df['Launch Site'] == selected_site]

    success_counts = df['class'].value_counts()
    labels = ['Failure', 'Success']
    values = [success_counts.get(0, 0), success_counts.get(1, 0)]

    fig = px.pie(values=values, names=labels, title=f"Success vs Failure for {selected_site}")
    return fig

# TASK 4 Callback: Update scatter chart based on site and payload selection
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'),
     Input('payload-slider', 'value')]
)
def update_scatter_chart(selected_site, payload_range):
    if selected_site == 'ALL':
        df = spacex_df
    else:
        df = spacex_df[spacex_df['Launch Site'] == selected_site]

    # Filter data based on payload range
    df_filtered = df[(df['Payload Mass (kg)'] >= payload_range[0]) &
                     (df['Payload Mass (kg)'] <= payload_range[1])]

    # Create scatter plot
    fig = px.scatter(df_filtered, x='Payload Mass (kg)', y='class', color='Launch Site',
                     labels={'class': 'Launch Success (1=Success, 0=Failure)', 'Payload Mass (kg)': 'Payload Mass (kg)'},
                     title="Payload Mass vs Launch Success")

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
