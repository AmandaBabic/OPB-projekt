from services.port_service import get_ports_detailed

def show_ports_page(db):
    ports = get_ports_detailed(db)

    if not ports:
        print("\nNi pristanišč.\n")
        return

    print("\n--- Pristanišča ---")
    print(f"{'Pristanišče':25} | {'Država':20} | {'Regija':15} | {'Lokacija':25}")
    print("-"*95)

    for p in ports[:5]:
        print(f"{p['port_name'][:25]:25} | {p['country'][:20]:20} | "
              f"{p['region'][:15]:15} | {p['location']:25}")