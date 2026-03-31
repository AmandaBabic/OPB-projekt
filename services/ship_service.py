from repositories.repository import (
    ShipRepository,
    ShipTypeRepository
)

def get_ships_detailed(db):
    ships = ShipRepository.get_all(db)
    ship_types = ShipTypeRepository.get_all(db)

    
    type_map = {t[0]: (t[1], t[2]) for t in ship_types}
    # ship_type_id -> (type_name, description)

    result = []

    for s in ships:
        ship_id = s[0]
        ship_name = s[1]
        imo = s[2]
        mmsi = s[3]
        call_sign = s[4]
        length = s[5]
        width = s[6]
        gross_tonnage = s[7]
        ship_type_id = s[8]

        type_name, description = type_map.get(ship_type_id, ("Unknown", ""))

        result.append({
            "ship_name": ship_name,
            "imo": imo,
            "mmsi": mmsi,
            "call_sign": call_sign,
            "length": length,
            "gross_tonnage": gross_tonnage,
            "type": type_name,
            "description": description
        })

    return result