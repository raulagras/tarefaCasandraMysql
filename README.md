<h2>Instrucciones para Levantar Contenedores y Ejecutar Scripts de MySQL y Cassandra</h2>
Este proyecto detalla los pasos necesarios para levantar contenedores de MySQL y Cassandra, configurar sus bases de datos y ejecutar scripts de consultas.

<h5>0. Requisitos Previos</h5>
Tener instalado Docker y Docker Compose.<br/>
Tener configurados los scripts de inicialización para MySQL (.sql) y Cassandra (.cql).

<h4>Pasos para Configuración y Ejecución</h4>
<h5>1. Clonar el Repositorio</h5>
Clona este repositorio en tu máquina local y accede al directorio del proyecto.

<h5>2. Configurar Docker Compose</h5>
Asegúrate de que el archivo docker-compose.yml está correctamente configurado, incluyendo los servicios para MySQL y Cassandra, junto con las rutas a los scripts.

<h5>3. Levantar los Contenedores</h5>
Ejecuta el comando para iniciar los contenedores en segundo plano. Una vez iniciado, verifica que ambos servicios están activos.

<h5>4. Cargar los Scripts</h5>
MySQL: Los scripts colocados en la carpeta configurada se ejecutarán automáticamente al iniciar el contenedor. Estos scripts suelen incluir la creación de bases de datos, tablas e inserción de datos iniciales. Cassandra: Los scripts deben ser ejecutados manualmente dentro del contenedor, a menos que se configure un proceso automático para su ejecución.

<h5>5. Cómo Ejecutar Consultas</h5>
MySQL: Accede al contenedor de MySQL para ejecutar consultas manualmente o conéctate desde un cliente externo usando las credenciales configuradas.
Cassandra: Ingresa al contenedor de Cassandra y utiliza la herramienta cqlsh para ejecutar comandos de forma interactiva o cargar scripts adicionales.

<h5>6. Detención y Limpieza</h5>
Detén los contenedores cuando termines de trabajar.
Si necesitas eliminar los volúmenes asociados, asegúrate de usar la opción que limpia los datos persistentes.

<h5>7. Notas Importantes</h5>
Verifica que los scripts de inicialización no contengan errores.
Personaliza las configuraciones de los contenedores según tus necesidades específicas.
