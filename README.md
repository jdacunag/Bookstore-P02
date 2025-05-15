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

## 1. Descripción de la actividad
A partir de una aplicación monolítica "BookStore" la cual corre en una sola máquina, con docker, un docker para la base de datos y otro docker para la aplicación; implementar lo siguiente:

* Objetivo 1: Desplegar la aplicación BookStore Monolítica en una Máquina Virtual en AWS, con un dominio propio, certificado SSL y Proxy inverso en NGINX. 

* Objetivo 2: Realizar el escalamiento en nube de la aplicación monolítica, siguiente algún patrón de arquitectura de escalamiento de apps monolíticas en AWS. La aplicación debe ser escalada utilizando Máquinas Virtuales (VM) con autoescalamiento, base de datos aparte Administrada o si es implementada con VM con Alta Disponibilidad, y Archivos compartidos vía NFS (como un servicio o una VM con NFS con Alta Disponibilidad).

* Objetivo 3: En el objetivo 3, se conservará mucho de lo desarrollado en el objetivo 2, pero en vez se utilizar máquinas virtuales en autoescalamiento, se utilizará un clúster de kubernetes.
Escalar la app monolitica en Kubernetes con Docker Swarm, en vez de contenedores son pods en un cluster y que se conecten externamente a la base de datos.

## 1.2 Aspectos NO cumplidos o desarrollados
Hasta el momento de la entrega, habíamos realizado los objetivos 1 y 2 de esta, sin embargo, al realizar un cambio en el código de los instance-templates lo cual daño todo nuestro progreso y que no permitio progesar al objetivo 3. Quedamos con el profesor que terminariamos todo lo que nos falta y que nos comunicaremos con él mediante el correo de interactiva para que pueda volver a revisar el proyecto completo y revalorar nuestra calificación.

## 2. Información general del proyecto

### Objetivo 1

### Objetivo 2

### Objetivo 3

### Arquitectura del Sistema

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
