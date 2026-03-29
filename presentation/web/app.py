from flask import Flask, render_template

from repositories.repository import Database

from services.ship_service import get_ships_detailed
from services.port_service import get_ports_detailed
from services.visit_service import get_visits_detailed
from services.country_service import get_countries
from services.dashboard_service import DashboardService

app = Flask(__name__)

db = Database()


# -------------------------
# HOME / POVZETEK
# -------------------------
@app.route("/")
def home():
    return dashboard()


# -------------------------
# SHIPS
# -------------------------
@app.route("/ships")
def ships():
    data = get_ships_detailed(db)
    return render_template("ships.html", ships=data)


# -------------------------
# PORTS
# -------------------------
@app.route("/ports")
def ports():
    data = get_ports_detailed(db)
    return render_template("ports.html", ports=data)


# -------------------------
# VISITS
# -------------------------
@app.route("/visits")
def visits():
    data = get_visits_detailed(db)
    return render_template("visits.html", visits=data)


# -------------------------
# COUNTRIES
# -------------------------
@app.route("/countries")
def countries():
    data = get_countries(db)
    return render_template("countries.html", countries=data)


# -------------------------
# DASHBOARD
# -------------------------

@app.route("/dashboard")
def dashboard():
    db = Database()

    visits_by_status = [
    {"label": row[0], "value": row[1]}
    for row in DashboardService.get_visits_by_status(db)
    ]

    cargo_distribution = [
        {"label": row[0], "value": row[1]}
        for row in DashboardService.get_cargo_type_distribution(db, top_n=10)
    ]

    busiest_ports = [
        {"port": row[0], "visits": row[1]}
        for row in DashboardService.get_busiest_ports(db, top_n=5)
    ]

    hazardous = [
        {"label": row[0], "value": row[1]}
        for row in DashboardService.get_hazardous_cargo_distribution(db)
    ]

    db.close()

    return render_template(
        "dashboard.html",
        visits_by_status=visits_by_status,
        cargo_distribution=cargo_distribution,
        busiest_ports=busiest_ports,
        hazardous=hazardous
    )


# -------------------------
# START
# -------------------------
if __name__ == "__main__":
    try:
        app.run(debug=True)
    finally:
        db.close()


