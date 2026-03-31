from repositories.repository import (
    PortRepository,
    CountryRepository
)

def get_ports_detailed(db):
    ports = PortRepository.get_all(db)
    countries = CountryRepository.get_all(db)

    country_map = {
        c[0]: (c[1], c[3])  # country_id -> (country_name, region)
        for c in countries
    }

    result = []

    for p in ports:
        port_id = p[0]
        port_name = p[1]
        country_id = p[2]
        lat = p[3]
        lon = p[4]

        country_name, region = country_map.get(country_id, ("Unknown", "Unknown"))

        # format lokacije: "lat°, lon°"
        location = f"{lat}°, {lon}°"

        result.append({
            "port_name": port_name,
            "country": country_name,
            "region": region,
            "location": location
        })

    return result