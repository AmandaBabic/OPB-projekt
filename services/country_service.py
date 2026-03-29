from repositories.repository import CountryRepository

def get_countries(db):
    countries = CountryRepository.get_all(db)

    result = []

    for c in countries:
        country_id = c[0]
        name = c[1]
        iso = c[2]
        region = c[3]

        result.append({
            "name": name,
            "iso": iso,
            "region": region
        })

    return result