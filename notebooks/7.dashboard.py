import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

DATA_PATH = "spaceX_clean.csv"

df = pd.read_csv(DATA_PATH)
sites = sorted(df["LaunchSite"].unique())
min_payload, max_payload = float(df["PayloadMass"].min()), float(df["PayloadMass"].max())

app = Dash(__name__)
app.title = "SpaceX Launch Records Dashboard"

app.layout = html.Div(
    style={"fontFamily": "Arial, sans-serif", "maxWidth": "1000px", "margin": "0 auto"},
    children=[
        html.H1("SpaceX Falcon 9 Launch Records Dashboard", style={"textAlign": "center"}),

        html.Div(
            [
                html.Label("Launch Site:"),
                dcc.Dropdown(
                    id="site-dropdown",
                    options=[{"label": "All Sites", "value": "ALL"}]
                    + [{"label": s, "value": s} for s in sites],
                    value="ALL",
                    clearable=False,
                ),
            ],
            style={"width": "60%", "margin": "20px auto"},
        ),

        dcc.Graph(id="success-pie-chart"),

        html.Div(
            [
                html.Label("Payload Mass Range (kg):"),
                dcc.RangeSlider(
                    id="payload-slider",
                    min=0,
                    max=int(max_payload) + 500,
                    step=500,
                    value=[min_payload, max_payload],
                    marks={i: str(i) for i in range(0, int(max_payload) + 1000, 2000)},
                ),
            ],
            style={"width": "90%", "margin": "30px auto"},
        ),

        dcc.Graph(id="payload-scatter-chart"),
    ],
)


@app.callback(Output("success-pie-chart", "figure"), Input("site-dropdown", "value"))
def update_pie(selected_site):
    if selected_site == "ALL":
        counts = df[df["Class"] == 1].groupby("LaunchSite").size().reset_index(name="Successes")
        fig = px.pie(counts, names="LaunchSite", values="Successes",
                     title="Total Successful Launches by Site")
    else:
        site_df = df[df["LaunchSite"] == selected_site]
        counts = site_df["Class"].value_counts().rename({0: "Failure", 1: "Success"}).reset_index()
        counts.columns = ["Outcome", "Count"]
        fig = px.pie(counts, names="Outcome", values="Count",
                     title=f"Success vs. Failure for {selected_site}",
                     color="Outcome",
                     color_discrete_map={"Success": "#3BB273", "Failure": "#E4572E"})
    return fig


@app.callback(
    Output("payload-scatter-chart", "figure"),
    Input("site-dropdown", "value"),
    Input("payload-slider", "value"),
)
def update_scatter(selected_site, payload_range):
    low, high = payload_range
    filtered = df[(df["PayloadMass"] >= low) & (df["PayloadMass"] <= high)]
    if selected_site != "ALL":
        filtered = filtered[filtered["LaunchSite"] == selected_site]

    fig = px.scatter(
        filtered, x="PayloadMass", y="Class", color="BoosterVersion",
        title="Payload Mass vs. Landing Outcome",
        labels={"Class": "Landing Outcome (0=Failure, 1=Success)", "PayloadMass": "Payload Mass (kg)"},
    )
    fig.update_yaxes(tickvals=[0, 1])
    return fig


if __name__ == "__main__":
    app.run(debug=True)
