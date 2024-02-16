import psycopg2.extras

import postgres.db_connection as db_connection


def insert(pii, conn=None):
    try:
        if not conn:
            conn = db_connection.postgre_conn()

        psycopg2.extras.register_uuid()
        insert_query = b'''INSERT INTO public.personal_information(sno, first_name, last_name, ssn, 
        period, started_by, ended_by)VALUES '''

        cur = conn.cursor()
        args_val = b','.join(cur.mogrify(b'''(%s, %s, %s, %s, %s, %s, %s)''', x) for x in pii)

        cur.execute(insert_query + args_val)

    except Exception as e:
        print(f"An error occurred: {e}")

    conn.close()
