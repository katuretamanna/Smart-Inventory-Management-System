from dash import Dash, html, dcc
import plotly.graph_objs as go
import pandas as pd

data = pd.read_csv('../data/optimized_inventory_data.csv')

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Smart Inventory Management System Dashboard"),
    
    dcc.Graph(
        id='inventory-levels',
        figure={
            'data': [
                go.Scatter(x=data['Date'], y=data['demand'], mode='lines', name='Actual Demand'),
                go.Scatter(x=data['Date'], y=data['Reorder_Point'], mode='lines', name='Reorder Point')
            ],
            'layout': go.Layout(title='Inventory Levels and Reorder Points')
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
