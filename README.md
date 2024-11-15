Instrucciones para Levantar Contenedores y Ejecutar Scripts de MySQL y Cassandra
Este proyecto detalla los pasos necesarios para levantar contenedores de MySQL y Cassandra, configurar sus bases de datos y ejecutar scripts de consultas.

0. Requisitos Previos
Tener instalado Docker y Docker Compose.
Tener configurados los scripts de inicialización para MySQL (.sql) y Cassandra (.cql).

Pasos para Configuración y Ejecución
1. Clonar el Repositorio
Clona este repositorio en tu máquina local y accede al directorio del proyecto.

2. Configurar Docker Compose
Asegúrate de que el archivo docker-compose.yml está correctamente configurado, incluyendo los servicios para MySQL y Cassandra, junto con las rutas a los scripts.

3. Levantar los Contenedores
Ejecuta el comando para iniciar los contenedores en segundo plano. Una vez iniciado, verifica que ambos servicios están activos.

4. Cargar los Scripts
MySQL: Los scripts colocados en la carpeta configurada se ejecutarán automáticamente al iniciar el contenedor. Estos scripts suelen incluir la creación de bases de datos, tablas e inserción de datos iniciales. Cassandra: Los scripts deben ser ejecutados manualmente dentro del contenedor, a menos que se configure un proceso automático para su ejecución.

5. Cómo Ejecutar Consultas
MySQL: Accede al contenedor de MySQL para ejecutar consultas manualmente o conéctate desde un cliente externo usando las credenciales configuradas.
Cassandra: Ingresa al contenedor de Cassandra y utiliza la herramienta cqlsh para ejecutar comandos de forma interactiva o cargar scripts adicionales.

6. Detención y Limpieza
Detén los contenedores cuando termines de trabajar.
Si necesitas eliminar los volúmenes asociados, asegúrate de usar la opción que limpia los datos persistentes.

7. Notas Importantes
Verifica que los scripts de inicialización no contengan errores.
Personaliza las configuraciones de los contenedores según tus necesidades específicas.
