import psycopg2

class RedshiftConnection:

    def __init__(self, connection_string):
        self.conn_string = connection_string

    def run_query(self, query):
        conn = psycopg2.connect(self.conn_string)
        cur = conn.cursor()
        cur.execute(query)
        try:
            result = cur.fetchall()
        except:
            result = []
        cur.close()
        conn.commit()
        conn.close()
        return result
