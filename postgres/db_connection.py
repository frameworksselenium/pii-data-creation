import psycopg2

conn = None


def postgre_conn(sec_data, execution_mode):
    global conn
    conn_string = "postgres_" + execution_mode + "_"
    conn = psycopg2.connect(
        database=sec_data[conn_string + 'database'],  # "postgres",
        host=sec_data[conn_string + 'host'],  # "127.0.0.1",
        user=sec_data[conn_string + 'user'],  # "postgres",
        password=sec_data[conn_string + 'password'],  # "India\@123"
        port=sec_data[conn_string + 'port'],  # "5432"
    )
    conn.autocommit = True
    return conn
