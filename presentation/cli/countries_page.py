from services.country_service import get_countries

def show_countries_page(db):
    countries = get_countries(db)

    if not countries:
        print("\nNi držav.\n")
        return

    print("\n--- Države ---")
    print(f"{'Država':25} | {'ISO':10} | {'Regija':20}")
    print("-"*65)

    for c in countries[:30]:
        print(f"{c['name'][:25]:25} | {c['iso']:10} | {c['region'][:20]:20}")