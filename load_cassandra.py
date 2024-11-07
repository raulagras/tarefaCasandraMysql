from cassandra.cluster import Cluster
import pandas as pd

# Conectar a Cassandra
cluster = Cluster(['localhost'])
session = cluster.connect()

# Crear el keyspace y la tabla
session.execute("""
CREATE KEYSPACE IF NOT EXISTS testkeyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
""")
session.set_keyspace('testkeyspace')

session.execute("""
CREATE TABLE IF NOT EXISTS estudiantes (
    ID_Estudiante INT PRIMARY KEY,
    Nombre TEXT,
    Grado TEXT,
    Materia TEXT,
    Calificacion FLOAT,
    Asistencia DECIMAL,
    Fecha_Registro DATE
);
""")

# Leer el dataset CSV
df = pd.read_csv("extracto_datos.csv")

# Insertar los datos
for _, row in df.iterrows():
    session.execute("""
    INSERT INTO estudiantes (ID_Estudiante, Nombre, Grado, Materia, Calificacion, Asistencia, Fecha_Registro) 
    VALUES (%s, %s, %s, %s, %s, %s, %s);
    """, (row['ID_Estudiante'], row['Nombre'], row['Grado'], row['Materia'], row['Calificación'], row['Asistencia (%)'], row['Fecha_Registro']))

print("Datos cargados en Cassandra!")

