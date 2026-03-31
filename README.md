## OPB-projekt: Register ladij

Projekt implementira preprost podatkovni skladiščni sistem za podatke o obiskih ladij v pristaniščih.
Podatki so shranjeni v PostgreSQL bazi, ki teče v Docker kontejnerju, aplikacija pa je zapisana v Pythonu.

Projekt uporablja večslojno arhitekturo:

* Scripts – skripte za pridobivanje in pripravo podatkov
* Repository layer – dostop do baze (SQL poizvedbe)
* Service layer – poslovna logika
* Presentation layer – uporabniški vmesnik (CLI ali web)


# Zahteve
Preden začnete, se prepričajte, da imate nameščeno naslednjo programsko opremo:

*   **Python**: [Prenos in namestitev](https://python.org)
*   **Docker**: [Navodila za namestitev](https://docker.com)
*   **Docker Compose**: [Navodila za namestitev](https://docker.com)

## Navodila za namestitev

### 1. Kloniranje repozitorija

```bash
git clone https://github.com/AmandaBabic/OPB-projekt.git
cd OPB-projekt
```

### 2. Ustvarjanje virtualnega okolja
```bash
python -m venv venv
```

Aktivacija virtualnega okolja:
```bash
venv\Scripts\activate
```


### 3. Namestitev potrebnih paketov
```bash
pip install -r requirements.txt
```

### 4. Zagon Docker Compose
Zaženite Docker s spodnjim ukazom:
```bash
docker compose up -d
```

### 5. Preverjanje stanja
Preverite, ali so storitve pravilno zagnane:
```bash
docker ps --filter "name=ship"
```

### 6. Dostop do baze podatkov
Za odpiranje psql uporabite:
```bash
docker compose exec db psql -U postgres -d ship
```

### 7. Uvoz podatkov
CSV datoteke iz mape scripts/ se uvozijo v bazo preko ukaza:
```bash
python scripts/insert_data.py
```

### 8. Zagon aplikacije
Zagon preko CLI:
```bash
python presentation/cli/app.py
```

Zagon preko web:
```bash
python presentation/web/app.py
```










































