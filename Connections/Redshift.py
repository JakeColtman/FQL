import psycopg2

class RedshiftConnection:

    def __init__(self, connection_string):
        self.conn_string = connection_string

    def run_query(self, query):
        conn = psycopg2.connect(self.conn_string)
        result = conn.cursor().execute(query)
        conn.close()
        return result
