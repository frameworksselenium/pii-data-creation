import pandas as pd
import psycopg2
import mysql.connector


# Function to fetch data from PostgreSQL database
def fetch_postgresql_data():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="postgres",
        user="postgres",
        password="India\@123",
        port="5432"
    )
    query = "SELECT * FROM public.personal_information"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


# Function to fetch data from MySQL database
def fetch_mysql_data():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        database="pii",
        user="root",
        password="rootroot",
        port="3306"
    )
    query = "SELECT * FROM pii.personal_information"
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# Fetch data from PostgreSQL
postgresql_df = fetch_postgresql_data()

# Fetch data from MySQL
mysql_df = fetch_mysql_data()

# Compare data
comparison_result = postgresql_df.compare(mysql_df)
print("Differences between PostgreSQL and MySQL data:")
print(comparison_result)
