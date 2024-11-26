import psycopg2
# from psycopg2.extras import RealDictCursor

# DATABASE = {
#     'dbname': 'postgres',
#     'user': 'postgres',
#     'password': 'imabhildi',
#     'host': 'localhost',
# }


conn = psycopg2.connect(database= "postgres", user= "postgres",password= "imabhildi03",host= 'localhost',port="5432")
cur=conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS courses (id serial PRIMARY KEY, name varchar(100),fees integer,duration integer);")
cur.execute("INSERT INTO courses (name,fees,duration) VALUES ('Web',1500,15),('Python',2500,20),('AI',5500,50);")

conn.commit()
cur.close()
conn.close()