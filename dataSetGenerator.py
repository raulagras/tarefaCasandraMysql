import pandas as pd
import numpy as np
from faker import Faker
import random

# Inicializar Faker para nombres aleatorios y datos falsos
fake = Faker()

# Parámetros de datos
num_registros = 1000000  # Cambia este valor para ajustar el tamaño del conjunto de datos
materias = ['Matemáticas', 'Ciencias', 'Historia', 'Lengua', 'Arte', 'Deportes']
grados = ['Primero', 'Segundo', 'Tercero', 'Cuarto', 'Quinto', 'Sexto']

# Función para generar calificación aleatoria
def generar_calificacion():
    return round(random.uniform(0, 10), 1)

# Generar datos aleatorios
data = {
    'ID_Estudiante': [],
    'Nombre': [],
    'Grado': [],
    'Materia': [],
    'Calificación': [],
    'Asistencia (%)': [],
    'Fecha_Registro': []
}

# Generar registros con un indicador de progreso
for i in range(num_registros):
    data['ID_Estudiante'].append(i + 1)
    data['Nombre'].append(fake.name())
    data['Grado'].append(random.choice(grados))
    data['Materia'].append(random.choice(materias))
    data['Calificación'].append(generar_calificacion())
    data['Asistencia (%)'].append(round(random.uniform(75, 100), 1))
    data['Fecha_Registro'].append(fake.date_this_year())

    # Imprimir el progreso cada 1000 registros
    if (i + 1) % 100 == 0:
        print(f"Generados {i + 1} de {num_registros} registros")

# Crear DataFrame
df = pd.DataFrame(data)

# Guardar como archivo CSV
df.to_csv('datos_educacion.csv', index=False)

print("Conjunto de datos generado y guardado como 'datos_educacion.csv'")
