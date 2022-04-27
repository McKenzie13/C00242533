# index page
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import benford
from server import app

header = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand("Deep Fake Detection Tool, by Marcin Kaczmarek - C00242533", href="/"),
        ]
    ),
    className="mb-5",
    color="dark",
    dark=True,
)
app.layout = html.Div(
    [
        header,
        html.Div(
            [
                dbc.Container(
                    id='page-content'
                )
            ]
        ),
        dcc.Location(id='base-url', refresh=False)
    ]
)
@app.callback(
    Output('page-content', 'children'),
    [Input('base-url', 'pathname')])
def router(pathname):
    return benford.layout

if __name__ == '__main__':
    app.run_server(debug=True)
