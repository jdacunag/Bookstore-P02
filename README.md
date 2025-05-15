# Tópicos Especiales en Telemática
## Proyecto 02, Escalabilidad en Bookstore



## Estudiante(s):
| Nombre | Correo |
|--------|-------------|
| David Lopera Londoño | dloperal2@eafit.edu.co |
| Camilo Monsalve Montes | cmonsalvem@eafit.edu.co |
| Juan Diego Acuña Giraldo | jdacunag@eafit.edu.co |

## Profesor:
| Profesor | Correo |
|----------|-------------|
| Edwin Nelson Montoya Múnera | emontoya@eafit.edu.co |

## Vídeo de la Sustentación
Por el inconveniente que tuvimos con la aplicación, no pudimos grabar el vídeo con los objetivos 1 y 2, sin embargo, tomamos capturas del progreso de ambos objetivos. Cuando solucionemos y terminemos lo que tenemos pendiente, montaremos el vídeo a la entrega.

#### Instancia creada para el objetivo 1

![Image](https://github.com/user-attachments/assets/9428b92f-96de-49cc-b5c0-9aae2f642e9d)

#### Template de instancias 

![Image](https://github.com/user-attachments/assets/392d10ad-88fc-4c6d-bc15-6c1ddab2cff8)

#### Código de configuración inicial de las instancias

![Image](https://github.com/user-attachments/assets/5648b339-2619-4195-a0c4-b1f1c9a01205)

#### Parámetros de la imagen AMI

![Image](https://github.com/user-attachments/assets/b7d323ad-bf28-45b2-8e99-4febb31ce679)

#### Balanceador de Cargas

![Image](https://github.com/user-attachments/assets/a08af28e-d7eb-4be1-8971-1dbe5595e449)

#### Grupos de Seguridad

![Image](https://github.com/user-attachments/assets/dbcdc3ae-a81c-4b19-b4a9-e11a61d6692b)

#### Parámetros del Grupo de Seguridad

![Image](https://github.com/user-attachments/assets/ffe9aa46-d242-4c1b-9113-72f0563c9400)

#### Base de datos en RDS
![Image](https://github.com/user-attachments/assets/a9ed2280-bfd8-4b75-988e-0176ddf7106c)

#### EFS 

![Image](https://github.com/user-attachments/assets/0c2f9b7a-23b7-452a-b62e-ac28e08564b8)

## 1. Descripción de la actividad
A partir de una aplicación monolítica "BookStore" la cual corre en una sola máquina, con docker, un docker para la base de datos y otro docker para la aplicación; implementar lo siguiente:

* Objetivo 1: Desplegar la aplicación BookStore Monolítica en una Máquina Virtual en AWS, con un dominio propio, certificado SSL y Proxy inverso en NGINX. 

* Objetivo 2: Realizar el escalamiento en nube de la aplicación monolítica, siguiente algún patrón de arquitectura de escalamiento de apps monolíticas en AWS. La aplicación debe ser escalada utilizando Máquinas Virtuales (VM) con autoescalamiento, base de datos aparte Administrada o si es implementada con VM con Alta Disponibilidad, y Archivos compartidos vía NFS (como un servicio o una VM con NFS con Alta Disponibilidad).

* Objetivo 3: En el objetivo 3, se conservará mucho de lo desarrollado en el objetivo 2, pero en vez se utilizar máquinas virtuales en autoescalamiento, se utilizará un clúster de kubernetes.
Escalar la app monolitica en Kubernetes con Docker Swarm, en vez de contenedores son pods en un cluster y que se conecten externamente a la base de datos.

## 1.2 Aspectos NO cumplidos o desarrollados
Hasta el momento de la entrega, habíamos realizado los objetivos 1 y 2 de esta, sin embargo, al realizar un cambio en el código de los instance-templates lo cual daño todo nuestro progreso y que no permitio progesar al objetivo 3. Quedamos con el profesor que terminariamos todo lo que nos falta y que nos comunicaremos con él mediante el correo de interactiva para que pueda volver a revisar el proyecto completo y revalorar nuestra calificación.

## 2. Información general del proyecto

### Arquitectura del sistema
#### 1. Cliente:

* Interfaz web basada en HTML/CSS con Bootstrap 5.3.2

* Interactúa con el servidor a través de formularios y solicitudes HTTP


#### 2. Servidor Web:

* Flask (framework web de Python)

* Gestiona las solicitudes HTTP y renderiza las plantillas

*Configurado para ejecutarse en Docker dentro de un contenedor


#### 3. Controladores (Blueprints):

* **auth_controller:** Gestión de autenticación (login, registro, logout)

* **book_controller:** Operaciones CRUD para libros

* **purchase_controller:** Gestión de compras de libros

* **payment_controller:** Procesamiento de pagos

* **delivery_controller:** Gestión de envíos

* **admin_controller:** Funciones administrativas


#### 4. Modelos de Datos:

* **User:** Gestión de usuarios y autenticación

* **Book:** Información de libros

* **Purchase:** Registros de compras

* **Payment:** Transacciones de pago

* **DeliveryProvider:** Proveedores de entrega

* **DeliveryAssignment:** Asignación de envíos


#### 5. Base de Datos:

* MySQL 8.0
  
* Almacena todos los datos de la aplicación

* Conectada a través de SQLAlchemy ORM


#### 6. Componentes de Soporte:

* **flask_login:** Gestión de sesiones y autenticación

* **werkzeug:** Utilidades HTTP y de seguridad

* **flask_sqlalchemy:** ORM para interactuar con la base de datos


#### 7. Contenedorización:

* Docker para encapsular la aplicación y sus dependencias

* Docker Compose para orquestar múltiples contenedores (aplicación y base de datos)

### Flujo de Datos

1. El usuario interactúa con la interfaz web (Vista)
 
2. Las solicitudes son procesadas por los controladores correspondientes (Controlador)
 
3. Los controladores interactúan con los modelos para acceder o modificar datos (Modelo)
 
4. SQLAlchemy traduce las operaciones de modelo a consultas SQL
    
5. La base de datos MySQL ejecuta las consultas y devuelve resultados
 
6. El controlador procesa los resultados y los pasa a la vista
    
7. La vista renderiza los datos en plantillas HTML que se devuelven al usuario

### Objetivo 1

### Objetivo 2

### Objetivo 3

### Estructura del proyecto

```
Bookstore-P02/
├── Bookstore-01/ # Carpeta con el objetivo 1 del proyecto
│   ├── controllers                   
│   ├── instance    
│   ├── models
│   ├── static
│   ├── templates
│   ├── app.py
│   ├── config.py
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── extensions.py
│   └── requirements.txt
├── Bookstore-02/ # Carpeta con el objetivo 2 del proyecto
│   ├── controllers                   
│   ├── instance    
│   ├── models
│   ├── static
│   ├── templates
│   ├── app.py
│   ├── config.py
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── extensions.py
│   └── requirements.txt
├── Bookstore-03/ # Carpeta con el objetivo 3 del proyecto
└── README.md
```

### Patrones implementados

## 3. Descripción del ambiente de desarrollo y técnico

### Lenguajes, librerías y tecnologías usadas

Frontend ->	Flask (Python)	

Bases de datos	(MySQL)	

Orquestación (Docker Swarm, Docker)

Contenedores (Docker Engine)

### Compilación y ejecución

Para esto se debe crear el entorno virtual primeramente en la carpeta raiz 

   ```bash
   python3 -m venv venv
   ```
Y luego encender el entorno virtual

```bash
   source venv/bin/activate
   ```

#### Usando Docker Compose (recomendado)

1. Clona el repositorio y navega hasta el directorio:
   ```bash
   git clone https://github.com/jdacunag/Bookstore-P02.git
   cd Bookstore-P02
   ```
2. Crear las imagenes y contenedores usando Docker Compose:
   ```bash
   docker-compose build
   ```
3. Ejecuta los servicios usando Docker Compose:
   ```bash
   docker-compose up -d
   ```

4. Para detener los servicios:
   ```bash
   docker-compose down
   ```

### Configuración de parámetros


## 4. Descripción del ambiente de EJECUCIÓN (en producción)

### Ambiente de ejecución

### Configuración en AWS

## Referencias
