import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
        'background': '#111111',
        'text': '#7FDBFF'
    }

# assume you have a "wide-form" data frame with no index
# see https://plotly.com/python/wide-form/ for more options
df_bar = pd.DataFrame({"x": [1, 2, 3], "SF": [4, 1, 9], "Montreal": [2, 4, 5]})

fig_bar = px.bar(df_bar, x="x", y=["SF", "Montreal"], barmode="group")
fig_bar.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'])

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
        html.H1(
            children='Hello Dash',
            style = {
                'textAlign': 'center',
                'color': colors['text']
                }
        ),

        html.Div(
            children='''Dash: A web application framework for Python.''',
            style = {
                'textAlign': 'center',
                'color': colors['text']
                }            
        ),

        dcc.Graph (
            id='example-graph',
            figure=fig_bar
        ),
    ])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080, debug=True)
