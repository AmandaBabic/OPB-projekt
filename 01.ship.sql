-- 1. Ship
CREATE TABLE IF NOT EXISTS dim_ship (
    ship_id SERIAL PRIMARY KEY,
    ship_name VARCHAR(100) NOT NULL,
    imo_number VARCHAR(15) NOT NULL UNIQUE,
    mmsi VARCHAR(15) NOT NULL,
    call_sign VARCHAR(10) NOT NULL,
    length DECIMAL(6,2),
    width DECIMAL(5,2),
    gross_tonnage DECIMAL(10,2),
    ship_type_id INT NOT NULL REFERENCES dim_ship_type(ship_type_id)
);

-- 2. Ship Type
CREATE TABLE IF NOT EXISTS dim_ship_type (
    ship_type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(100) NOT NULL UNIQUE
    description VARCHAR(255) 
);

-- 3. Country
CREATE TABLE IF NOT EXISTS dim_country (
    country_id SERIAL PRIMARY KEY,
    country_name VARCHAR(100) NOT NULL UNIQUE,
    iso_code CHAR(2) NOT NULL UNIQUE,
    region VARCHAR(50) NOT NULL
);

-- 4. Port
CREATE TABLE IF NOT EXISTS dim_port (
    port_id SERIAL PRIMARY KEY,
    port_name VARCHAR(100) NOT NULL,
    country_id INT NOT NULL REFERENCES dim_country(country_id),
    latitude DECIMAL(9,6) NOT NULL,
    longitude DECIMAL(9,6) NOT NULL
);

-- 5. Visit
CREATE TABLE IF NOT EXISTS fact_visit (
    visit_id SERIAL PRIMARY KEY,
    ship_id INT NOT NULL REFERENCES dim_ship(ship_id),
    port_id INT NOT NULL REFERENCES dim_port(port_id),
    ETA TIMESTAMP NOT NULL,
    ATA TIMESTAMP NOT NULL,
    ETD TIMESTAMP NOT NULL,
    ATD TIMESTAMP NOT NULL,
    status_id INT NOT NULL REFERENCES dim_status(status_id),
    cargo_type_id INT NOT NULL REFERENCES dim_cargo_type(cargo_type_id)
);

-- 6. Cargo Type
CREATE TABLE IF NOT EXISTS dim_cargo_type (
    cargo_type_id SERIAL PRIMARY KEY,
    cargo_name VARCHAR(100) NOT NULL UNIQUE,
    cargo_detailed_name VARCHAR(255),
    hazardous BOOLEAN NOT NULL
);

-- 7. Status
CREATE TABLE IF NOT EXISTS dim_status (
    status_id SERIAL PRIMARY KEY,
    status_name VARCHAR(50) NOT NULL UNIQUE
);