import mysql.connector

conn = None


def insert(pii, sec_data, execution_mode):
    global conn
    conn_string = "mysql_" + execution_mode + "_"
    try:
        conn = mysql.connector.connect(
            database=sec_data[conn_string + 'database'],  # "pii",
            host=sec_data[conn_string + 'host'],  # "127.0.0.1",
            user=sec_data[conn_string + 'user'],  # "root",
            password=sec_data[conn_string + 'password'],  # "rootroot",
            port=sec_data[conn_string + 'port'],  # "3306"
        )

        # Create a cursor object to execute SQL queries

        # Define your SQL query to insert data
        sql = (
            "INSERT INTO personal_information (first_name, last_name, ssn, period, started_by, ended_by)"
            " VALUES (%s, %s, %s, %s, %s, %s)")
        cursor = conn.cursor()
        # Execute the SQL query for multiple records
        cursor.executemany(sql, pii)

        # Commit the transaction
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"An error occurred: {e}")
