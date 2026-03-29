from flask import Flask, render_template_string
import plotly.express as px
import pandas as pd

from services.visit_service import get_visits_detailed

app = Flask(__name__)


def load_data(db):
    visits = get_visits_detailed(db)

    if not visits:
        return pd.DataFrame()  

    return pd.DataFrame(visits)


@app.route("/")
def dashboard():

    
    import sqlite3
    db = sqlite3.connect("ship.db")

    df = load_data(db)

    if df.empty:
        return "<h1>No data in DB</h1>"

    # --------------------------
    # 1. VISITS BY STATUS
    # --------------------------
    status_counts = df["status"].value_counts().reset_index()
    status_counts.columns = ["status", "count"]

    fig_status = px.bar(
        status_counts,
        x="status",
        y="count",
        title="Visits by Status"
    )

    # --------------------------
    # 2. CARGO PIE CHART
    # --------------------------
    cargo_counts = df["cargo"].value_counts().reset_index()
    cargo_counts.columns = ["cargo", "count"]

    fig_cargo = px.pie(
        cargo_counts,
        names="cargo",
        values="count",
        title="Cargo Distribution"
    )

    # --------------------------
    # 3. BUSIEST PORTS
    # --------------------------
    port_counts = df["port"].value_counts().reset_index()
    port_counts.columns = ["port", "visits"]

    fig_ports = px.bar(
        port_counts,
        x="port",
        y="visits",
        title="Busiest Ports"
    )

    # --------------------------
    # 4. HAZARDOUS CARGO
    # --------------------------
    df["is_hazardous"] = df["cargo"].str.lower().str.contains("hazard")

    hazard_counts = df["is_hazardous"].value_counts().reset_index()
    hazard_counts.columns = ["hazard", "count"]

    fig_hazard = px.bar(
        hazard_counts,
        x="hazard",
        y="count",
        title="Hazardous vs Non-Hazardous Cargo"
    )

    # --------------------------
    # HTML RENDER
    # --------------------------
    html = f"""
    <html>
    <head>
        <title>Ship Dashboard</title>
    </head>
    <body>
        <h1>🚢 Ship Dashboard</h1>

        <h2>Visits by Status</h2>
        {fig_status.to_html(full_html=False)}

        <h2>Cargo Distribution</h2>
        {fig_cargo.to_html(full_html=False)}

        <h2>Busiest Ports</h2>
        {fig_ports.to_html(full_html=False)}

        <h2>Hazardous Cargo</h2>
        {fig_hazard.to_html(full_html=False)}

    </body>
    </html>
    """

    return render_template_string(html)


if __name__ == "__main__":
    app.run(debug=True)