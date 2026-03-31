from services.visit_service import get_visits_detailed

def show_visits_page(db):
    visits = get_visits_detailed(db)

    if not visits:
        print("\nNi nobenih obiskov.\n")
        return

    print("\n--- Obiski ---")
    print(f"{'Ladja':25} | {'Pristanišče':20} | {'Status':10} | {'ETA':19} | {'ATA':19} | {'ETD':19} | {'ATD':19} | {'Cargo':20}")
    print("-"*155)

    for v in visits[:20]:  # limit!
        print(f"{v['ship'][:25]:25} | {v['port'][:20]:20} | {v['status'][:10]:10} | "
              f"{v['ETA']} | {v['ATA']} | {v['ETD']} | {v['ATD']} | {v['cargo'][:20]:20}")