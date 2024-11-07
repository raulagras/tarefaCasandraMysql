import mysql.connector
import time

# Conectar a MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="contraseñasegura",
    database="escuela"
)
cursor = conn.cursor()

# Medir o tempo de execución da consulta
start_time = time.time()
cursor.execute("SELECT AVG(Calificacion) FROM estudiantes")
avg_mysql = cursor.fetchone()[0]
end_time = time.time()

print(f"Media en MySQL: {avg_mysql}")
print(f"Tempo de execución en MySQL: {end_time - start_time} segundos")

cursor.close()
conn.close()
