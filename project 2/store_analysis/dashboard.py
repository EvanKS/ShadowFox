
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import os

# Initialize App
app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
app.title = "Retail Analytics Dashboard"

# Load Data
DATA_PATH = "store_analysis/data/store_data.csv"

def get_data():
    if os.path.exists(DATA_PATH):
        try:
            if DATA_PATH.endswith('.csv'):
                df = pd.read_csv(DATA_PATH, encoding='latin1')
            else:
                df = pd.read_excel(DATA_PATH)
            df['Order Date'] = pd.to_datetime(df['Order Date'])
            return df
        except:
            return None
    return None

df = get_data()

# App Layout
if df is not None:
    categories = ['All'] + sorted(df['Category'].unique().tolist())
    regions = ['All'] + sorted(df['Region'].unique().tolist())
    
    app.layout = html.Div([
        # Header
        html.Div([
            html.H1("STORE SALES & PROFIT DASHBOARD", style={
                'textAlign': 'center', 
                'color': '#2c3e50', 
                'fontFamily': 'Arial, sans-serif',
                'fontWeight': 'bold',
                'marginBottom': '10px'
            }),
            html.P("Interactive analysis of sales performance and profitability", style={
                'textAlign': 'center',
                'color': '#7f8c8d',
                'fontSize': '16px'
            })
        ], style={'padding': '30px', 'backgroundColor': '#f8f9fa', 'borderBottom': '1px solid #ddd'}),
        
        # Filters
        html.Div([
            html.Div([
                html.Label("Select Category:", style={'fontWeight': 'bold'}),
                dcc.Dropdown(id='cat-dropdown', options=categories, value='All', clearable=False)
            ], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'}),
            
            html.Div([
                html.Label("Select Region:", style={'fontWeight': 'bold'}),
                dcc.Dropdown(id='region-dropdown', options=regions, value='All', clearable=False)
            ], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'}),
        ], style={'maxWidth': '1200px', 'margin': '20px auto', 'padding': '20px', 'backgroundColor': 'white', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}),
        
        # Key Metrics Row
        html.Div([
            html.Div(id='total-sales', style={'padding': '20px', 'textAlign': 'center', 'backgroundColor': '#e8f6f3', 'color': '#16a085', 'borderRadius': '5px', 'width': '30%'}),
            html.Div(id='total-profit', style={'padding': '20px', 'textAlign': 'center', 'backgroundColor': '#fcf3cf', 'color': '#f39c12', 'borderRadius': '5px', 'width': '30%'}),
            html.Div(id='profit-margin', style={'padding': '20px', 'textAlign': 'center', 'backgroundColor': '#ebf5fb', 'color': '#2980b9', 'borderRadius': '5px', 'width': '30%'}),
        ], style={'display': 'flex', 'justifyContent': 'space-around', 'maxWidth': '1200px', 'margin': '20px auto'}),
        
        # Graphs Row 1
        html.Div([
            dcc.Graph(id='trend-chart', style={'width': '65%', 'display': 'inline-block'}),
            dcc.Graph(id='segment-pie', style={'width': '33%', 'display': 'inline-block'}),
        ], style={'maxWidth': '1200px', 'margin': '0 auto'}),
        
        # Graphs Row 2
        html.Div([
            dcc.Graph(id='scatter-plot', style={'width': '100%'})
        ], style={'maxWidth': '1200px', 'margin': '20px auto'})
    ], style={'backgroundColor': '#f4f6f6', 'minHeight': '100vh', 'fontFamily': 'Arial, sans-serif'})
    
    @app.callback(
        [Output('trend-chart', 'figure'),
         Output('segment-pie', 'figure'),
         Output('scatter-plot', 'figure'),
         Output('total-sales', 'children'),
         Output('total-profit', 'children'),
         Output('profit-margin', 'children')],
        [Input('cat-dropdown', 'value'),
         Input('region-dropdown', 'value')]
    )
    def update_dashboard(cat, region):
        try:
            # Handle None inputs safely
            if cat is None: cat = 'All'
            if region is None: region = 'All'

            dff = df.copy()
            
            # Filter Data
            if cat != 'All':
                dff = dff[dff['Category'] == cat]
            if region != 'All':
                dff = dff[dff['Region'] == region]
            
            # Check for empty data
            if dff.empty:
                empty_fig = px.scatter(title="No Data Matches Filters")
                return empty_fig, empty_fig, empty_fig, "$0", "$0", "0.0%"

            # Metrics
            sales = dff['Sales'].sum()
            profit = dff['Profit'].sum()
            margin = (profit/sales)*100 if sales > 0 else 0
            
            # Charts
            # 1. Trend
            trend = dff.groupby('Order Date')['Sales'].sum().reset_index()
            fig1 = px.line(trend, x='Order Date', y='Sales', title='Sales Trend Over Time')
            fig1.update_layout(title_font_size=18, title_x=0.5)
            
            # 2. Segment
            seg = dff.groupby('Segment')['Sales'].sum().reset_index()
            fig2 = px.pie(seg, values='Sales', names='Segment', title='Sales by Segment', hole=0.4)
            fig2.update_layout(title_font_size=18, title_x=0.5)
            
            # 3. Scatter
            # Ensure Quantity is numeric and fill NaNs for size safety
            dff['Quantity'] = pd.to_numeric(dff['Quantity'], errors='coerce').fillna(1)
            
            fig3 = px.scatter(dff, x='Sales', y='Profit', color='Sub-Category', size='Quantity',
                              title='Sales vs Profit Analysis (Bubble Size: Quantity)', 
                              hover_data=['Product Name'])
            fig3.update_layout(title_font_size=18, title_x=0.5)
            
            # Format Metrics with Labels
            return (
                fig1, fig2, fig3, 
                [html.H3("Total Sales", style={'margin': 0, 'fontSize': '16px'}), html.H2(f"${sales:,.0f}", style={'margin': '10px 0'})],
                [html.H3("Total Profit", style={'margin': 0, 'fontSize': '16px'}), html.H2(f"${profit:,.0f}", style={'margin': '10px 0'})],
                [html.H3("Profit Margin", style={'margin': 0, 'fontSize': '16px'}), html.H2(f"{margin:.1f}%", style={'margin': '10px 0'})]
            )
            
        except Exception as e:
            print(f"Error in dashboard callback: {e}")
            # Return safe error defaults
            err_fig = px.scatter(title=f"Error: {str(e)}")
            return err_fig, err_fig, err_fig, "Error", "Error", "Error"

else:
    app.layout = html.H1("Dataset not found. Please upload 'store_analysis/data/store_data.csv'")

if __name__ == '__main__':
    app.run(debug=True)
