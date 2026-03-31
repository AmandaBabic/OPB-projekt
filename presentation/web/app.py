from flask import Flask, render_template, request, redirect, session, url_for

from repositories.repository import Database

from services.ship_service import get_ships_detailed
from services.port_service import get_ports_detailed
from services.visit_service import get_visits_detailed
from services.country_service import get_countries
from services.dashboard_service import DashboardService

app = Flask(__name__)
app.secret_key = "supersecretkey"  # NUJNO za session

db = Database()

# -------------------------
# USERS (za login)
# -------------------------
USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}


# -------------------------
# LOGIN
# -------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = USERS.get(username)

        if user and user["password"] == password:
            session["user"] = username
            session["role"] = user["role"]
            return redirect(url_for("dashboard"))

        return render_template("login.html", error="Napačni podatki!")

    return render_template("login.html")


# -------------------------
# LOGOUT
# -------------------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# -------------------------
# HOME / POVZETEK
# -------------------------
@app.route("/")
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    return redirect(url_for("dashboard"))


# -------------------------
# DASHBOARD
# -------------------------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

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
# SHIPS (ONLY ADMIN)
# -------------------------
@app.route("/ships")
def ships():
    if "user" not in session:
        return redirect(url_for("login"))

    if session.get("role") != "admin":
        return "Nimate dostopa!"

    data = get_ships_detailed(db)
    return render_template("ships.html", ships=data)


# -------------------------
# PORTS
# -------------------------
@app.route("/ports")
def ports():
    if "user" not in session:
        return redirect(url_for("login"))

    data = get_ports_detailed(db)
    return render_template("ports.html", ports=data)


# -------------------------
# VISITS
# -------------------------
@app.route("/visits")
def visits():
    if "user" not in session:
        return redirect(url_for("login"))

    data = get_visits_detailed(db)
    return render_template("visits.html", visits=data)


# -------------------------
# COUNTRIES
# -------------------------
@app.route("/countries")
def countries():
    if "user" not in session:
        return redirect(url_for("login"))

    data = get_countries(db)
    return render_template("countries.html", countries=data)


# -------------------------
# START
# -------------------------
if __name__ == "__main__":
    try:
        app.run(debug=True)
    finally:
        db.close()