import psycopg2

conn = psycopg2.connect("dbname=northwind user=postgres password=pass1234 host=0.0.0.0")
print(conn)