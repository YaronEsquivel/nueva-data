# BETELGEUSE

BETELGEUSE es un arquetipo que fue generado sin lógica de negocio, por lo que puede aplicarse en cualquier escenario donde se necesite un microservicio backend Python.

Su alto desacoplamiento permite ser configurado para diferentes escenarios y ser integrado con múltiples plataformas de diferentes tecnologías.

Está preparado para que se le integren nuevas librerías y/o funcionalidades según el requerimiento específico del proyecto en donde se aplique.

El desarrollo de BETELGEUSE busca tener una estructura estándar de componentes y funcionalidades inherentes de una aplicación que permitan al usuario implementador contar con ejemplos prácticos reales.

## Proyecto BETELGEUSE Basado en Python con Flask

Proyecto base para microservicios en Python con Flask, ofreciendo estructura modular y enrutamiento RESTful.

**Base de Datos:**

* **PostgreSQL:** Sistema de gestión de bases de datos relacionales que ofrece un enfoque robusto y escalable para el almacenamiento de datos en aplicaciones Python.

**Testing**
* **Unittest:** Marco de pruebas unitarias en Python para garantizar la calidad y confiabilidad del código en microservicios y componentes.

**Tecnologías:**
* **Flask:** Framework ligero para la creación de aplicaciones y microservicios en Python, proporcionando enrutamiento RESTful y modularidad.

* **SQLAlchemy:** Biblioteca ORM que simplifica la interacción con bases de datos en microservicios Flask, facilitando la persistencia de datos.

* **Flask-DotEnv:** Extensión para cargar configuraciones desde archivos .env, lo que permite gestionar las variables de entorno de manera eficiente.

* **Flask-SQLAlchemy:** Integración de SQLAlchemy con Flask para abordar operaciones de base de datos en aplicaciones web y microservicios.
  
* **psycopg2:** Proporciona una interfaz para conectarse y trabajar con bases de datos PostgreSQL

## Requisitos

* [Instalar Docker Desktop](https://www.docker.com/products/docker-desktop/)
* [Instalar Python](https://www.python.org/)

## Configuración de Base de Datos PostgreSQL

En caso de no tener un servidor de Base de Datos PostgreSQL, se puede instalar una imagen en un contenedor Docker, reemplazar los datos del servidor creado y ejecutar el servicio, por lo que se ejecutan los siguientes pasos:

Ejecutar el siguiente comando para crear el servidor PostgreSQL:

```bash
    docker run --name some-postgres -e POSTGRES_DB=pruebas -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -p 5432:5432 -d postgres:11-bullseye
```
Después de ejecutar el comando anterior, tendremos disponible el servidor:

![Docker](/assets/docker-PostgreSQL.png)
![Docker_Desktop](/assets/docker_desktop.png)

Para la creación de la tabla y datos de prueba puede usar el siguiente [Script](https://github.com/Axitymx/23_Axity_python_flask_archetype/tree/feature/AR-12-A-BETELGEUSE-ARQUETIPO-PYTHON-FLASK/assets/sql):
```bash
    \assets\sql\data.sql
```

## Creación y Configuración de los servicios

Para más información de la creación, configuración y contenido adicional, revise [Ficha Técnica](https://github.com/Axitymx/23_Axity_python_flask_archetype/tree/feature/AR-12-A-BETELGEUSE-ARQUETIPO-PYTHON-FLASK/backend) 

## Casos de uso

BETELGEUSE dispone de la arquitectura de componentes diseñadas para implementar los métodos HTTP Consulta, Creación, Eliminación y Edición que serán expuestos a través del servicio. Para lo cual ejemplifica los siguientes métodos:

### Manage User

**Descripción del método – GET USER BY ID**

* **Funcionalidad:** Obtener un usuario de una lista de usuarios.

* **Url:** Dirección Ip donde se encuentre publicado el servicio (Se utiliza localhost de prueba) 

* **Puerto:** Puerto donde se encuentre publicado el servicio (Se utiliza el puerto 5432 de prueba)  

* **Parámetros:** user_id 

* **Ejemplo:** http://localhost:3000/users/{user_id}

* **Http Verb:** GET 

* **Response:** 200 OK 

![Docker](/assets/Postman-GET.png)


**Descripción del método – CREATE USER**

* **Funcionalidad:** Crear un nuevo usuario.

* **Url:** Dirección Ip donde se encuentre publicado el servicio (Se utiliza localhost de prueba) 

* **Puerto:** Puerto donde se encuentre publicado el servicio (Se utiliza el puerto 5432 de prueba)  

* **Parámetros:** N/A 

* **Ejemplo:** http://localhost:3000/users/

* **Http Verb:** POST 


![Docker](/assets/Postman-POST.png)


**Descripción del método – UPDATE USER**

* **Funcionalidad:** Actualizar información de un usuario existente.

* **Url:** Dirección Ip donde se encuentre publicado el servicio (Se utiliza localhost de prueba) 

* **Puerto:** Puerto donde se encuentre publicado el servicio (Se utiliza el puerto 5432 de prueba)  

* **Parámetros:** user_id 

* **Ejemplo:** http://localhost:3000/users/{user_id}

* **Http Verb:** PUT 

![Docker](/assets/Postman-PUT.png)


**Descripción del método – DELETE USER**

* **Funcionalidad:** Eliminar un usuario existente.

* **Url:** Dirección Ip donde se encuentre publicado el servicio (Se utiliza localhost de prueba) 

* **Puerto:** Puerto donde se encuentre publicado el servicio (Se utiliza el puerto 5432 de prueba)  

* **Parámetros:** N/A 

* **Ejemplo:** http://localhost:3000/users/{user_id}

* **Http Verb:** DELETE  

![Docker](/assets/Postman-DELETE.png)



## Colaboradores


## Licencia

[MIT](https://opensource.org/licenses/MIT)

![Audience](/assets/CReA.png)

### Este ARTE forma parte del CReA de Axity, para más información visitar [CReA](https://intellego365.sharepoint.com/sites/CentralAxity/M%C3%A9xico/Consultoria/Arquitectura/SitePages/CReA.aspx)

