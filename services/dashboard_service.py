# services/dashboard_service.py

class DashboardService:

    @staticmethod
    def get_visits_by_status(db):
        """
        Vrne število visits po statusu (sorted desc).
        Output format:
        [
            ("Completed", 120),
            ("In Port", 80),
            ...
        ]
        """

        query = """
        SELECT 
            s.status_name,
            COUNT(v.visit_id) AS total_visits
        FROM fact_visit v
        JOIN dim_status s ON v.status_id = s.status_id
        GROUP BY s.status_name
        ORDER BY total_visits DESC;
        """

        cur = db.conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()

        return rows
    

    @staticmethod
    def get_cargo_type_distribution(db, top_n=10):
        """
        Vrne TOP N cargo type-ov po številu visits.
        """

        query = """
        SELECT 
            c.cargo_name,
            COUNT(v.visit_id) AS total_visits
        FROM fact_visit v
        JOIN dim_cargo_type c ON v.cargo_type_id = c.cargo_type_id
        GROUP BY c.cargo_name
        ORDER BY total_visits DESC
        LIMIT %s;
        """

        cur = db.conn.cursor()
        cur.execute(query, (top_n,))
        rows = cur.fetchall()
        cur.close()

        return rows
    

    @staticmethod
    def get_busiest_ports(db, top_n=5):
        """
        Vrne TOP N portov po številu obiskov.
        """

        query = """
        SELECT 
            p.port_name,
            COUNT(v.visit_id) AS total_visits
        FROM fact_visit v
        JOIN dim_port p ON v.port_id = p.port_id
        GROUP BY p.port_name
        ORDER BY total_visits DESC
        LIMIT %s;
        """

        cur = db.conn.cursor()
        cur.execute(query, (top_n,))
        rows = cur.fetchall()
        cur.close()

        return rows
    

    @staticmethod
    def get_hazardous_cargo_distribution(db):
        """
        Vrne število visitov po hazardous / non-hazardous cargo.
        """

        query = """
        SELECT 
            CASE 
                WHEN c.hazardous = TRUE THEN 'Hazardous'
                ELSE 'Standard'
            END AS cargo_risk,
            COUNT(v.visit_id) AS total_visits
        FROM fact_visit v
        JOIN dim_cargo_type c ON v.cargo_type_id = c.cargo_type_id
        GROUP BY cargo_risk
        ORDER BY total_visits DESC;
        """

        cur = db.conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()

        return rows