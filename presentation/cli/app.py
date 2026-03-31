from repositories.database import Database

from presentation.cli.menu import show_menu
from presentation.cli.visits_page import show_visits_page
from presentation.cli.ships_page import show_ships_page
from presentation.cli.ports_page import show_ports_page
from presentation.cli.countries_page import show_countries_page
from presentation.cli.dashboard_page import show_dashboard_page

from auth.login import login

def main():
    db = Database()

    role = login()
    if not role:
        return

    try:
        while True:
            show_menu()
            choice = input("Izberi: ").strip()

            if choice == "1":
                show_dashboard_page()
                

            elif choice == "2":
                    show_visits_page(db)

            elif choice == "3":
                if role == "admin":
                        show_ships_page(db)
                else:
                        print("Do strani nimate dostopa!")

            elif choice == "4":
                    show_ports_page(db)

            elif choice == "5":
                    show_countries_page(db)

            elif choice == "0":
                    print("\nLep pozdrav!")
                    break

            else:
                    print("\nNeveljavna izbira. Poskusi ponovno.\n")

    finally:
        db.close()


if __name__ == "__main__":
    main()