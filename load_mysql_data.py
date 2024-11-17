import mysql.connector
import pandas as pd

# Conectar á base de datos MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="contraseñasegura",
    database="escuela"
)

cursor = conn.cursor()

# Ler o dataset CSV
df = pd.read_csv("extracto_datos.csv")

# Crear a táboa en MySQL
cursor.execute("""
CREATE TABLE IF NOT EXISTS estudiantes (
    ID_Estudiante INT PRIMARY KEY,
    Nombre VARCHAR(100),
    Grado VARCHAR(50),
    Materia VARCHAR(50),
    Calificacion DECIMAL(4,2),
    Asistencia DECIMAL(5,2),
    Fecha_Registro DATE
)
""")

# Insertar os datos en MySQL
for _, row in df.iterrows():
    cursor.execute("""
    INSERT INTO estudiantes (ID_Estudiante, Nombre, Grado, Materia, Calificacion, Asistencia, Fecha_Registro)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (row['ID_Estudiante'], row['Nombre'], row['Grado'], row['Materia'], row['Calificación'], row['Asistencia (%)'], row['Fecha_Registro']))

conn.commit()
cursor.close()
conn.close()

print("Datos cargados en MySQL!")
