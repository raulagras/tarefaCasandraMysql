<h2>Instrucciones para Levantar Contenedores y Ejecutar Scripts de MySQL y Cassandra</h2>
Este proyecto detalla los pasos necesarios para levantar contenedores de MySQL y Cassandra, configurar sus bases de datos y ejecutar scripts de consultas.

<h5>0. Requisitos Previos</h5>
Tener instalado Docker y Docker Compose.<br/>

<h4>Pasos para Configuración y Ejecución</h4>
<h5>1. Clonar el Repositorio</h5>
Clona este repositorio en tu máquina local y accede al directorio del proyecto.
Importar el enviroment tarefaCasandra y activarlo

<h5>2. Configurar Docker Compose</h5>
Asegúrate de que el archivo docker-compose.yml está correctamente configurado, incluyendo los servicios para MySQL y Cassandra, junto con las rutas a los scripts.

<h5>3. Levantar los Contenedores</h5>
Ejecuta el comando para iniciar los contenedores en segundo plano. Una vez iniciado, verifica que ambos servicios están activos.

<h5>4. Cargar los Scripts</h5>
<h6>MySQL:</h6>Ejecutar load_mysql_data.py<br/> 
<h6>Cassandra:</h6> Ejecutar load_cassandra.py

<h5>5. Cómo Ejecutar Consultas</h5>
<h6>MySQL:</h6> Ejecutar query_mysql.py<br/>
<h6>Cassandra:</h6> Ejecutar query_cassandra.py

<h5>6. Detención y Limpieza</h5>
Detén los contenedores cuando termines de trabajar.
Si necesitas eliminar los volúmenes asociados, asegúrate de usar la opción que limpia los datos persistentes.

<h5>7. Notas Importantes</h5>
El repositorio incluye un csv llamado extracto_datos que contiene un fragmento de la información. En caso de querer probar con el millón de datos será necesario ejecutar dataSetGenerator.py y renombrar en los load el "extracto_datos" por el "datos_educacion". Esto está indicado en el propio notebook.


<h4>Sobre las preguntas propuestas:</h4>

- **¿Cuál es más rápida?**
    - **MySQL**: El tiempo de consulta fue de **0.2120361328125 segundos**.

- **¿Son los resultados los esperados?**
    - La media diverge ligeramente en Cassandra respecto a MySQL. 
    - Promedio de calificación en **Cassandra**: **5.0042314529418945**.
    - Media en **MySQL**: **4.997203**.

- **¿Cómo justificas los resultados?**
    - Esta pequeña diferencia puede deberse al funcionamiento interno de los decimales y redondeos que aplican ambos lenguajes, especialmente considerando el volumen tan grande de datos con el que se calcula la media.
