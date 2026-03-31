## OPB-projekt
Projekt pri predmetu Podatkovne baze.

# Navodila za namestitev
Preden začnete, se prepričajte, da imate nameščeno naslednjo programsko opremo:

*   **Python**: [Prenos in namestitev](https://python.org)
*   **Docker**: [Navodila za namestitev](https://docker.com)
*   **Docker Compose**: [Navodila za namestitev](https://docker.com)

*Zagon Docker Compose* <br>
Zaženite vsebnike s spodnjim ukazom:
`docker compose up -d`

*Preverjanje stanja* <br>
Preverite, ali so storitve pravilno zagnane:
`docker ps --filter "name=ship"`

*Dostop do baze podatkov* <br>
Za odpiranje **psql** uporabite:
`docker compose exec db psql -U postgres -d ship`
