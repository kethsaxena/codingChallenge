# app.py

import dash
from dash import dcc, html, Input, Output, State, dash_table
import plotly.express as px
import pandas as pd
import io
import base64

# Initialize the app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("📈 Monthly Data Dashboard"),

    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select CSV File')
        ]),
        style={
            'width': '90%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '2px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '20px'
        },
        multiple=False  # Only allow one file at a time
    ),

    html.Div(id='output-data-upload')
])

# Helper function to parse the uploaded file
# def parse_contents(contents, filename):
#     content_type, content_string = contents.split(',')
#     decoded = base64.b64decode(content_string)
#     try:
#         if 'csv' in filename:
#             # Assume the user uploaded a CSV file
#             df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
#     except Exception as e:
#         return html.Div([
#             'There was an error processing this file.'
#         ])

#     # Display the DataFrame and a sample chart
#     return html.Div([
#         html.H5(filename),
#         dash_table.DataTable(
#             data=df.head(10).to_dict('records'),
#             columns=[{'name': i, 'id': i} for i in df.columns],
#             page_size=10,
#             style_table={'overflowX': 'auto'}
#         ),
#         html.Br(),
#         dcc.Graph(
#             figure=px.histogram(df, x=df.columns[0])  # You can customize this!
#         )
#     ])

def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
    except Exception as e:
        return html.Div([
            'There was an error processing this file.'
        ])

    # 🔥 Calculate positive sum from the first numeric column
    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) > 0:
        first_numeric_col = numeric_cols[0]
        positive_sum = df[df[first_numeric_col] > 0][first_numeric_col].sum()
        positive_sum_formatted = "${:,.2f}".format(positive_sum)

    else:
        first_numeric_col = None
        positive_sum_formatted = "N/A"

    return html.Div([
        html.H5(filename),
        
        # 🔥 Display the positive sum
        html.H4(f"Total Positive Sum ({first_numeric_col}): {positive_sum_formatted}"),

        # Show the DataTable
        dash_table.DataTable(
            data=df.head(10).to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns],
            page_size=10,
            style_table={'overflowX': 'auto'}
        ),
        html.Br(),
        dcc.Graph(
            figure=px.histogram(df, x=df.columns[0]) if len(df.columns) > 0 else {}
        )
    ])


# Callback to update the page when a file is uploaded
@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'))
def update_output(contents, filename):
    if contents is not None:
        return parse_contents(contents, filename)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
