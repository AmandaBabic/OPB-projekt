# test_services.py

from repositories.repository import Database
from services.ship_service import (
    get_all_ships,
    get_all_ship_types,
    get_all_countries,
    get_all_ports,
    get_all_cargo_types,
    get_all_statuses,
    get_all_visits,
    get_large_ships
)

# Povezava na bazo
db = Database()

ships = get_all_ships(db)
print("Število ladij:", len(ships))
print("Prvih 3 ladje:", ships[:3])

large_ships = get_large_ships(db)
print("Velike ladje (>30 GT):", len(large_ships))
print("Prvih 3 velike ladje:", large_ships[:3])


ship_types = get_all_ship_types(db)
print("Število tipov ladij:", len(ship_types))

countries = get_all_countries(db)
print("Število držav:", len(countries))

ports = get_all_ports(db)
print("Število pristanišč:", len(ports))

cargo_types = get_all_cargo_types(db)
print("Število tipov tovora:", len(cargo_types))

statuses = get_all_statuses(db)
print("Število statusov:", len(statuses))

visits = get_all_visits(db)
print("Število obiskov:", len(visits))

# Zapremo bazo
db.close()