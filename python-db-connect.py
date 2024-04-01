import psycopg2;

conn = psycopg2.connect(database = "gepnic_v21", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "postgres",
                        port = 5432)

cur = conn.cursor()
cur.execute('Select announcementcontent from gep_announcement limit 5')
rows = cur.fetchall()
conn.commit()
conn.close()
for row in rows:
  print(row)




