from repositories.repository import (
    VisitRepository,
    ShipRepository,
    PortRepository,
    StatusRepository,
    CargoTypeRepository
)

def get_visits_detailed(db):
    visits = VisitRepository.get_all(db)
    ships = ShipRepository.get_all(db)
    ports = PortRepository.get_all(db)
    statuses = StatusRepository.get_all(db)
    cargos = CargoTypeRepository.get_all(db)

    
    ship_map = {s[0]: s[1] for s in ships}        # ship_id -> ship_name
    port_map = {p[0]: p[1] for p in ports}        # port_id -> port_name
    status_map = {s[0]: s[1] for s in statuses}   # status_id -> status_name
    cargo_map = {c[0]: c[1] for c in cargos}      # cargo_id -> cargo_name

    result = []

    for v in visits:
        visit_id = v[0]
        ship_id = v[1]
        port_id = v[2]
        ETA = v[3]
        ATA = v[4]
        ETD = v[5]   
        ATD = v[6] 
        status_id = v[7]
        cargo_id = v[8]

        result.append({
        "ship": ship_map.get(ship_id, "Unknown"),
        "port": port_map.get(port_id, "Unknown"),
        "status": status_map.get(status_id, "Unknown"),
        "ETA": ETA,
        "ATA": ATA,
        "ETD": ETD,  
        "ATD": ATD,   
        "cargo": cargo_map.get(cargo_id, "Unknown")
    })

    return result