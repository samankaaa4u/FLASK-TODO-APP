from psycopg_pool import ConnectionPool
from dotenv import load_dotenv
from os import environ

load_dotenv()

con_string = f"host={environ.get('HOST')} dbname={environ.get('DATABASE')} user={environ.get('UN')} password={environ.get('PASSWORD')}"


conn_pool = ConnectionPool(con_string)




def connection(sql: str, params: tuple = ()):
    with conn_pool.connection() as conn:
        with conn.cursor() as cur:
            if params == ():
                return cur.execute(sql,).fetchall()
            else:
                return cur.execute(sql, params).fetchall()


def connection_insert(sql: str, params: tuple = ()):
    with conn_pool.connection() as conn:
        with conn.cursor() as cur:
            if params == ():
                return cur.execute(sql,)
            else:
                return cur.execute(sql, params)






