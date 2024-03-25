import psycopg2


def connect():
    return psycopg2.connect(
        dbname="SQL-Student",
        user="postgres",
        password="161213",
        host="localhost"
    )
