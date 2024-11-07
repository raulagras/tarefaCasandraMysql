from cassandra.cluster import Cluster
import time

# Conectar a Cassandra
cluster = Cluster(['localhost'])
session = cluster.connect('testkeyspace')

# Definir la consulta
query = "SELECT AVG(Calificacion) FROM estudiantes"
print(f"Ejecutando consulta en Cassandra: {query}")

# Medir el tiempo de ejecución de la consulta
start_time = time.time()
rows = session.execute(query)

# Usar 'one()' para obtener la primera fila (única fila) y acceder al valor
avg_cassandra = rows.one()[0]  # 'one()' devuelve la primera fila, y [0] es el primer valor de esa fila
end_time = time.time()

session.shutdown()

# Mostrar el resultado
print(f"Promedio de Calificación en Cassandra: {avg_cassandra}")
print(f"Tiempo de ejecución en Cassandra: {end_time - start_time} segundos")
