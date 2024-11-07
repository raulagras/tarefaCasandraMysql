from cassandra.cluster import Cluster
import time

# Conectar a Cassandra
cluster = Cluster(['localhost'])
session = cluster.connect('testkeyspace')

# Medir el tiempo de ejecución de la consulta
start_time = time.time()
rows = session.execute("SELECT AVG(Calificacion) FROM estudiantes")
avg_cassandra = rows[0][0]
end_time = time.time()

print(f"Promedio de Calificación en Cassandra: {avg_cassandra}")
print(f"Tiempo de ejecución en Cassandra: {end_time - start_time} segundos")
