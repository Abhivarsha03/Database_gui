import psycopg2
import os
# from psycopg2.extras import RealDictCursor

# DATABASE = {
#     'dbname': 'postgres',
#     'user': 'postgres',
#     'password': 'imabhildi',
#     'host': 'localhost',
# }

def create_table():
    dbname = os.getenv('DB_DATABASE')
    user = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')

    conn = psycopg2.connect(database= dbname, user= user, password= password,host= host,port=port)
    cur=conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS courses (id serial PRIMARY KEY, name varchar(100),fees integer,duration integer);")
    cur.execute("INSERT INTO courses (name,fees,duration) VALUES ('Web',1500,15),('Python',2500,20),('AI',5500,50);")

    conn.commit()
    cur.close()
    conn.close()