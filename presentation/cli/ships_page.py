from services.ship_service import get_ships_detailed

def show_ships_page(db):
    ships = get_ships_detailed(db)

    if not ships:
        print("\nNi ladij.\n")
        return

    print("\n--- Ladje ---")
    print(f"{'Ladja':20} | {'IMO številka':15} | {'MMSI številka':12} | {'Klicni znak':12} | {'Dolžina':8} | {'Bruto tonaža':10} | {'Tip':15} | {'Opis':20}")
    print("-"*130)

    for s in ships[:20]:
        print(f"{s['ship_name'][:20]:20} | {s['imo']:15} | {s['mmsi']:12} | "
              f"{s['call_sign'][:12]:12} | {str(s['length']):8} | "
              f"{str(s['gross_tonnage']):10} | {s['type'][:15]:15} | {s['description'][:20]:20}")