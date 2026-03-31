# test_import.py

from repositories.repository import (
    Database,
    ShipRepository,
    ShipTypeRepository,
    CountryRepository,
    PortRepository,
    CargoTypeRepository,
    StatusRepository,
    VisitRepository
)

def main():
    print("Povezujem se na bazo...")
    db = Database()

    try:
        print("Uvažam dim_status...")
        StatusRepository.insert_from_csv("status.csv", db)

        print("Uvažam dim_ship_type...")
        ShipTypeRepository.insert_from_csv("ship_type.csv", db)

        print("Uvažam dim_country...")
        CountryRepository.insert_from_csv("country.csv", db)

        print("Uvažam dim_port...")
        PortRepository.insert_from_csv("port.csv", db)

        print("Uvažam dim_cargo_type...")
        CargoTypeRepository.insert_from_csv("cargo_type.csv", db)

        print("Uvažam dim_ship...")
        ShipRepository.insert_from_csv("ship.csv", db)

        print("Uvažam fact_visit...")
        VisitRepository.insert_from_csv("visit.csv", db)

        print("Vsi CSV-ji so uspešno uvoženi!")

    finally:
        db.close()
        print("Povezava z bazo zaprta.")

if __name__ == "__main__":
    main()