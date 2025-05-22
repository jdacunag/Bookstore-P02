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
[Link del Video](https://youtu.be/_TKlc1hrPTs)

## 1. Descripción de la actividad
A partir de una aplicación monolítica "BookStore" la cual corre en una sola máquina, con docker, un docker para la base de datos y otro docker para la aplicación; implementar lo siguiente:

* Objetivo 1: Desplegar la aplicación BookStore Monolítica en una Máquina Virtual en AWS, con un dominio propio, certificado SSL y Proxy inverso en NGINX. 

* Objetivo 2: Realizar el escalamiento en nube de la aplicación monolítica, siguiente algún patrón de arquitectura de escalamiento de apps monolíticas en AWS. La aplicación debe ser escalada utilizando Máquinas Virtuales (VM) con autoescalamiento, base de datos aparte Administrada o si es implementada con VM con Alta Disponibilidad, y Archivos compartidos vía NFS (como un servicio o una VM con NFS con Alta Disponibilidad).

* Objetivo 3: En el objetivo 3, se conservará mucho de lo desarrollado en el objetivo 2, pero en vez se utilizar máquinas virtuales en autoescalamiento, se utilizará un clúster de kubernetes.
Escalar la app monolitica en Kubernetes con Docker Swarm, en vez de contenedores son pods en un cluster y que se conecten externamente a la base de datos.

## 1.2 Aspectos NO cumplidos o desarrollados
No implementamos kubernetes para el objetivo 3.

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

## Objetivo 1

## ¿Qué implementamos?

**Aplicación BookStore desplegada en una sola máquina virtual EC2 con:**

### Infraestructura base:
- 1 instancia EC2 (t2.micro) con Amazon Linux 2023
- IP elástica para acceso consistente desde Internet
- Grupo de seguridad configurado para HTTP (80), HTTPS (443) y SSH (22)

### Componentes de software:
- **Nginx:** Servidor web y proxy inverso que maneja las conexiones HTTPS y redirige al contenedor de la aplicación
- **Docker y Docker Compose:** Para containerización y orquestación de servicios
- **Aplicación Flask:** API monolítica que maneja todas las funcionalidades (autenticación, catálogo, compras, pagos, entregas)
- **Base de datos MySQL:** Almacenamiento de datos en contenedor con volumen persistente

### Seguridad y dominio:
- Dominio propio configurado (proyecto2.dominio.tld)
- Certificado SSL de Let's Encrypt para conexiones HTTPS seguras
- Renovación automática de certificados

### Funcionalidades de la aplicación:
- Registro y autenticación de usuarios
- Catálogo de libros con visualización
- Sistema de compras con gestión de stock
- Procesamiento de pagos (simulado)
- Gestión de entregas con múltiples proveedores
- Panel administrativo para gestión de usuarios

### Características técnicas:
- **Arquitectura:** Monolítica (toda la lógica en una sola aplicación)
- **Base de datos:** MySQL en contenedor Docker
- **Proxy inverso:** Nginx redirige de puerto 80/443 a puerto 5000
- **Persistencia:** Volumen Docker para datos de la base de datos
- **Escalabilidad:** Limitada (vertical únicamente)

### Diagrama de la Arquitectura

![Captura de pantalla 2025-05-21 221544](https://github.com/user-attachments/assets/880a66a2-13ee-4ffd-ba1e-5682929bd473)

### Objetivo 2
Realizar el escalamiento en nube de la aplicación monolítica, siguiente algún patrón de arquitectura de escalamiento de apps monolíticas en AWS. La aplicación debe ser escalada utilizando Máquinas Virtuales (VM) con autoescalamiento, base de datos aparte Administrada o si es implementada con VM con Alta Disponibilidad, y Archivos compartidos vía NFS (como un servicio o una VM con NFS con Alta Disponibilidad).

## ¿Qué implementamos?
**Aplicación BookStore con arquitectura escalable y servicios administrados de AWS:**

### Infraestructura base:

* Múltiples instancias EC2 (t2.micro) gestionadas por Auto Scaling Group (mín: 2, máx: 4, deseado: 2)

* Application Load Balancer (ALB) para distribución de tráfico y alta disponibilidad

* Base de datos MySQL RDS (db.t4g.micro) externa para persistencia centralizada

* Sistema de archivos EFS para almacenamiento compartido entre instancias

* AMI personalizada (bookstore-app-ami) para despliegue consistente de aplicaciones

* Launch Template para configuración estandarizada de nuevas instancias

* Múltiples zonas de disponibilidad para redundancia geográfica

### Componentes de software:

* Application Load Balancer: Distribuye tráfico HTTP/HTTPS entre múltiples instancias y maneja terminación SSL

* Auto Scaling Group: Gestiona automáticamente el número de instancias según demanda

* Docker y Docker Compose: Containerización de la aplicación con inicio automático en cada instancia

* Aplicación Flask: API monolítica replicada en múltiples instancias para alta disponibilidad

* MySQL RDS: Base de datos administrada por AWS con backups automáticos y alta disponibilidad

* Amazon EFS: Sistema de archivos distribuido para compartir datos entre instancias

* AWS Certificate Manager: Gestión automática de certificados SSL/TLS

### Seguridad y redes:

* Grupos de seguridad especializados (app-sg, db-sg, efs-sg) con acceso mínimo necesario

* Base de datos RDS en subredes privadas, no accesible desde Internet

* Certificados SSL gestionados automáticamente por AWS Certificate Manager

* Comunicación segura entre componentes a través de grupos de seguridad específicos

### Funcionalidades de la aplicación:

* Registro y autenticación de usuarios con sesiones distribuidas

* Catálogo de libros con alta disponibilidad (sin interrupciones por fallos)

* Sistema de compras con gestión de stock sincronizada entre instancias

* Procesamiento de pagos (simulado) con tolerancia a fallos

* Gestión de entregas con múltiples proveedores

* Panel administrativo accesible desde cualquier instancia

* Continuidad del servicio: La aplicación permanece disponible durante fallos de instancias individuales

### Características técnicas:

* Arquitectura: Monolítica replicada con balanceador de carga para alta disponibilidad

* Base de datos: MySQL RDS externa, compartida por todas las instancias

* Load Balancing: ALB distribuye tráfico automáticamente entre instancias saludables

* Persistencia: RDS para datos transaccionales + EFS para archivos compartidos

* Escalabilidad: Horizontal automática basada en métricas de CPU (2-4 instancias)

* Alta disponibilidad: Multi-AZ deployment con recuperación automática ante fallos

* Monitoreo: CloudWatch para métricas de rendimiento y salud de instancias

### Auto-escalamiento y recuperación:

* Scaling automático: Nuevas instancias se lanzan cuando CPU > 70% por 2 minutos consecutivos

* Health checks: ALB verifica constantemente la salud de las instancias (cada 30s)

* Self-healing: Instancias no saludables son terminadas y reemplazadas automáticamente

* Zero-downtime deployments: Actualizaciones sin interrupciones usando rolling deployments

* Disaster recovery: Respaldo automático de RDS y recuperación en múltiples AZs

### Servicios administrados de AWS:


* RDS: Eliminates gestión manual de base de datos (backups, patches, escalamiento)

* EFS: Almacenamiento elástico que escala automáticamente según necesidades

* ALB: Balanceador gestionado con alta disponibilidad incorporada

* Auto Scaling: Gestión automática de capacidad sin intervención manual

* CloudWatch: Monitoreo y alertas integradas para todos los componentes
  
#### Diagrama de la Arquitectura

![Image](https://github.com/user-attachments/assets/f90424b3-349f-4162-98b3-8a81376b1f4a)

## Objetivo 3
En el objetivo 3, se conservará mucho de lo desarrollado en el objetivo 2, pero en vez se utilizar máquinas virtuales en autoescalamiento, se utilizará un clúster.
Escalar la app monolitica en Kubernetes o Docker Swarm (en este caso usamos Docker Swarm), en vez de contenedores son pods en un cluster y que se conecten externamente a la base de datos.

## ¿Qué implementamos?
**Aplicación BookStore desplegada en un clúster Docker Swarm con alta disponibilidad:**

### Infraestructura base:
* 3 instancias EC2 (t2.micro) con Amazon Linux 2023:

  * 1 nodo Manager (con IP elástica para acceso desde Internet
  
  * 2 nodos Worker para distribución de cargas


* Clúster Docker Swarm configurado para orquestación automática
  
* Grupo de seguridad configurado para HTTP (80), HTTPS (443), SSH (22) y comunicación Swarm (2377, 7946, 4789)
  
* Base de datos MySQL RDS externa para persistencia centralizada
  
### Componentes de software:

* Nginx: Servidor web y proxy inverso desplegado en el nodo Manager, maneja conexiones HTTPS y balancea carga hacia las réplicas de la aplicación

* Docker Swarm: Orquestador nativo de Docker para gestión automática de contenedores, distribución de cargas y alta disponibilidad

* Aplicación Flask: API monolítica desplegada en 3 réplicas distribuidas automáticamente entre los nodos Worker

* MySQL RDS: Base de datos externa gestionada por AWS, accesible desde todas las réplicas de la aplicación

* Docker Visualizer: Herramienta de monitoreo para visualizar el estado del clúster Swarm

### Funcionalidades de la aplicación:
* Registro y autenticación de usuarios

* Catálogo de libros con visualización

* Sistema de compras con gestión de stock distribuido

* Procesamiento de pagos (simulado)

* Gestión de entregas con múltiples proveedores

* Panel administrativo para gestión de usuarios

* Alta disponibilidad: La aplicación permanece disponible aunque falle uno de los nodos

### Características técnicas:
* Arquitectura: Monolítica replicada en múltiples contenedores para alta disponibilidad

* Base de datos: MySQL RDS externa, compartida por todas las réplicas

* Load Balancer: Docker Swarm distribuye automáticamente las peticiones entre las 3 réplicas

* Proxy inverso: Nginx redirige de puerto 80/443 hacia el servicio interno del clúster

* Persistencia: Base de datos externa RDS para datos persistentes y consistentes

* Escalabilidad: Horizontal automática (se pueden agregar/quitar réplicas dinámicamente)

* Tolerancia a fallos: Si un nodo falla, Swarm redistribuye automáticamente los contenedores

* Service Discovery: Resolución automática de nombres de servicios dentro del clúster

### Seguridad y dominio:
* Dominio propio configurado (proyecto3.libritosedwin.site)

* Certificado SSL de Let's Encrypt para conexiones HTTPS seguras

* Renovación automática de certificados programada

* Red overlay segura para comunicación entre contenedores

### Diagrama de la Arquitectura
![Image](https://github.com/user-attachments/assets/e15fd3c6-1853-49e9-b6c9-5cc7fe039bb1)


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
│   ├── controllers                   
│   ├── instance    
│   ├── models
│   ├── static
│   ├── templates
│   ├── nginx
│   ├── app.py
│   ├── config.py
│   ├── docker-compose.yml
│   ├── docker-stack.yml
│   ├── Dockerfile
│   ├── extensions.py
│   └── requirements.txt
└── README.md
```


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

**NOTA:** El ambiente de desarrollo a nivel local solamente fue usado para probar la aplicación y poder implementar los objetivos.



## 4. Descripción del ambiente de EJECUCIÓN (en producción)

### Ambiente de ejecución (OBJETIVO 1)

### 1. Configurar el par de claves en AWS

1. **Crear un par de claves en AWS**
   - En la consola AWS, ve a EC2 > "Key Pairs" > "Create key pair"
   - Nombre: `bookstore-key`
   - Tipo de clave: RSA
   - Formato: .pem (para OpenSSH)
   - Haz clic en "Create key pair"
   - El archivo .pem se descargará automáticamente. Guárdalo en un lugar seguro.

2. **Configurar permisos del archivo de clave**
   ```bash
   chmod 400 ruta/a/bookstore-key.pem
   ```

### 2. Crear una instancia EC2

1. **Lanza una nueva instancia**
   - En la consola AWS, ve a EC2 > "Instances" > "Launch instances"
   - Nombre: `bookstore-monolith`
   - AMI: Amazon Linux 2023
   - Tipo de instancia: t2.micro
   - Par de claves: Selecciona `bookstore-key`

2. **Configuración de red:**
   - Grupo de seguridad: Crea uno nuevo llamado `bookstore-sg`
   - Reglas de entrada:
     - HTTP (80) desde cualquier lugar (0.0.0.0/0)
     - HTTPS (443) desde cualquier lugar (0.0.0.0/0)
     - SSH (22) desde tu IP

3. **Almacenamiento:** 20 GB gp2

4. **Haz clic en "Launch instance"**

5. **Asigna una IP elástica**
   - En EC2, ve a "Elastic IPs" > "Allocate Elastic IP address"
   - Selecciona la nueva IP > "Actions" > "Associate Elastic IP address"
   - Selecciona tu instancia `bookstore-monolith`
   - Anota la IP elástica asignada: _________

### 3. Configurar tu dominio en GoDaddy (o tu proveedor DNS)

1. **Accede a la gestión DNS de tu dominio**
   - Inicia sesión en GoDaddy
   - Ve a "Mis productos" y selecciona tu dominio
   - Haz clic en "DNS" o "Administrar DNS"

2. **Configura el registro A para el dominio raíz**
   - Busca el registro tipo A con nombre "@" (o crea uno nuevo)
   - Establece el valor a la IP elástica de tu instancia EC2
   - TTL: 600 segundos o 1 hora

3. **Configura el registro CNAME para www**
   - Busca o crea un registro tipo CNAME
   - Nombre: "www"
   - Valor: "proyecto2.tudominio.tld." (incluye el punto al final)
   - TTL: 1 hora

### 4. Conectarse a la instancia y configurar el entorno

1. **Conéctate a la instancia usando SSH**
   ```bash
   ssh -i ruta/a/bookstore-key.pem ec2-user@[tu-ip-elastica]
   ```

2. **Actualiza el sistema e instala dependencias**
   ```bash
   sudo dnf update -y
   sudo dnf install -y docker git python3-pip nginx
   sudo systemctl enable docker
   sudo systemctl start docker
   sudo usermod -aG docker ec2-user
   ```

3. **Cierra la sesión y reconéctate para que los cambios de grupo tengan efecto**
   ```bash
   exit
   ssh -i ruta/a/bookstore-key.pem ec2-user@[tu-ip-elastica]
   ```

4. **Instala Docker Compose**
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 5. Configurar Nginx como proxy inverso

1. **Crea la configuración de Nginx**
   ```bash
   sudo mkdir -p /etc/nginx/conf.d
   sudo nano /etc/nginx/conf.d/bookstore.conf
   ```

2. **Añade la siguiente configuración mejorada para HTTP que incluye soporte para la validación de Certbot**
   ```nginx
   server {
       listen 80;
       server_name proyecto2.tudominio.tld www.proyecto2.tudominio.tld;

       # Esta ubicación es crucial para Let's Encrypt
       location /.well-known/acme-challenge/ {
           root /var/www/html;
           try_files $uri =404;
       }

       location / {
           proxy_pass http://localhost:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```

3. **Verifica y reinicia Nginx**
   ```bash
   sudo nginx -t
   sudo systemctl enable nginx
   sudo systemctl restart nginx
   ```

4. **Crea el directorio necesario para la validación de Certbot**
   ```bash
   sudo mkdir -p /var/www/html/.well-known/acme-challenge
   sudo chmod -R 755 /var/www/html
   ```

### 6. Desplegar la aplicación BookStore

1. **Clona el repositorio y navega a la carpeta del Objetivo 1**
   ```bash
   mkdir -p ~/bookstore
   cd ~/bookstore
   git clone https://github.com/st0263eafit/st0263-251/blob/main/proyecto2/BookStore.zip .
   unzip BookStore.zip
   cd BookStore
   ```

2. **Asegúrate de que el archivo config.py esté correctamente configurado**
   ```bash
   nano config.py
   ```

   Verifica que la configuración sea similar a:
   ```python
   import os

   SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bookstore_user:bookstore_pass@db/bookstore'
   SECRET_KEY = 'secretkey'
   SQLALCHEMY_TRACK_MODIFICATIONS = False
   ```

3. **Inicia los contenedores con Docker Compose**
   ```bash
   docker-compose up -d
   ```

4. **Verifica que los contenedores estén funcionando**
   ```bash
   docker-compose ps
   ```

   Deberías ver dos contenedores activos: `bookstore_db_1` y `bookstore_flaskapp_1`

5. **Revisa los logs si hay algún problema**
   ```bash
   docker-compose logs -f
   ```

### 7. Configurar SSL con Certbot (Let's Encrypt)

1. **Instala Certbot y el plugin para Nginx**
   ```bash
   sudo dnf install -y certbot python3-certbot-nginx
   ```

2. **Obtén un certificado SSL para tu dominio**
   ```bash
   sudo certbot --nginx -d proyecto2.tudominio.tld -d www.proyecto2.tudominio.tld
   ```

3. **Si encuentras problemas con la validación HTTP, prueba el modo standalone**
   ```bash
   # Detén Nginx temporalmente
   sudo systemctl stop nginx

   # Ejecuta Certbot en modo standalone
   sudo certbot certonly --standalone -d proyecto2.tudominio.tld -d www.proyecto2.tudominio.tld

   # Reinicia Nginx
   sudo systemctl start nginx
   ```

4. **Alternativa: Si el modo standalone también falla, prueba con validación DNS**
   ```bash
   sudo certbot certonly --manual --preferred-challenges dns -d proyecto2.tudominio.tld -d www.proyecto2.tudominio.tld
   ```
   
   Certbot te proporcionará instrucciones para crear registros TXT específicos en tu configuración DNS de GoDaddy. Sigue esas instrucciones y espera a que se propaguen los cambios antes de continuar.

5. **Después de obtener el certificado, configura Nginx para usar HTTPS**
   ```bash
   sudo nano /etc/nginx/conf.d/bookstore.conf
   ```

   Añade la configuración para HTTPS:
   ```nginx
   server {
       listen 80;
       server_name proyecto2.tudominio.tld www.proyecto2.tudominio.tld;
       return 301 https://$host$request_uri;
   }

   server {
       listen 443 ssl;
       server_name proyecto2.tudominio.tld www.proyecto2.tudominio.tld;

       ssl_certificate /etc/letsencrypt/live/proyecto2.tudominio.tld/fullchain.pem;
       ssl_certificate_key /etc/letsencrypt/live/proyecto2.tudominio.tld/privkey.pem;

       # Otras configuraciones SSL recomendadas
       ssl_protocols TLSv1.2 TLSv1.3;
       ssl_prefer_server_ciphers on;
       ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512:ECDHE-RSA-AES256-GCM-SHA384;
       ssl_session_timeout 1d;
       ssl_session_cache shared:SSL:10m;
       ssl_session_tickets off;

       location / {
           proxy_pass http://localhost:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```

6. **Verifica la renovación automática de los certificados**
   ```bash
   sudo systemctl status certbot-renew.timer
   ```

7. **Prueba la renovación manualmente**
   ```bash
   sudo certbot renew --dry-run
   ```

8. **Verifica tu sitio**
   - Abre un navegador y navega a `https://proyecto2.tudominio.tld`
   - La aplicación BookStore debería estar funcionando con HTTPS

### Ambiente de ejecución (OBJETIVO 2)

### Creación de las Instancias

### 1. Configurar grupos de seguridad detallados

En AWS debemos configurar los siguientes "Security Groups" para cada uno de las instancias/modelos que vamos a utilizar

1. **Grupo de seguridad para la base de datos** (`bookstore-db-sg`)
   * ID: sg-0859664aeeb8bcb33
   * Reglas de entrada: MySQL/Aurora (3306) desde las instancias de la aplicación
   * VPC: vpc-0251ee5f51637233e

2. **Grupo de seguridad para las instancias de la aplicación** (`bookstore-app-sg`)
   * ID: sg-0573a0f8b5ba931dc
   * Reglas de entrada:
     * HTTP (80) para el balanceador
     * SSH (22) para acceso
     * NFS (2049) para sistema de archivos EFS
   * Reglas de salida: Todo el tráfico
   * VPC: vpc-0251ee5f51637233e

3. **Grupo de seguridad para EFS** (`bookstore-efs-sg`)
   * ID: sg-0b4cb9276fa5e8683
   * Reglas de entrada: NFS (2049) desde `bookstore-app-sg`
   * VPC: vpc-0251ee5f51637233e

### 2. Base de datos RDS y sistema de archivos EFS

1. **Base de datos RDS** (`bookstore-db`):
   * Endpoint: bookstore-db.cv48yui8kfd3.us-east-1.rds.amazonaws.com
   * Usuario: bookstore_user
   * Contraseña: juandiego123
   * Estado: Disponible
   * Clase: db.t4g.micro

2. **Sistema de archivos EFS** (`bookstore-efs`):
   * ID: fs-0cbe8950e6f8fe03b
   * Estado: Disponible
   * DNS: fs-0cbe8950e6f8fe03b.efs.us-east-1.amazonaws.com
  
### 3. Configurar la instancia para crear la AMI

Ya has configurado exitosamente una instancia con el script `deploy_bookstore_final.sh` que creamos juntos. Ahora la documentaremos formalmente como parte del Objetivo 2:

1. **Crear y configurar una instancia EC2 para la AMI**:
   * AMI: Amazon Linux 2023
   * Tipo: t2.micro
   * Grupo de seguridad: `bookstore-app-sg` (sg-0573a0f8b5ba931dc)
   * Almacenamiento: 8 GB gp2

2. **Conectarse a la instancia por SSH**

3. **Crear el script de configuración**:
   ```bash
   nano deploy_bookstore_final.sh 
   ```

   **Y copiar lo siguiente en el archivo:**

    ```bash
   #!/bin/bash
  
   echo "=== Iniciando despliegue final de BookStore con RDS ==="
   
   # 0. Detener todos los contenedores Docker
   echo "=== Deteniendo contenedores existentes ==="
   docker stop $(docker ps -aq) || true
   
   # 1. Crear directorio para la aplicación
   cd ~
   rm -rf bookstore_final  # Eliminar directorio si existe
   mkdir -p bookstore_final
   cd bookstore_final
   
   # 2. Descargar y descomprimir BookStore
   echo "=== Descargando BookStore ==="
   curl -L -o BookStore.zip https://github.com/st0263eafit/st0263-251/raw/main/proyecto2/BookStore.zip
   unzip -o BookStore.zip
   rm BookStore.zip
   
   # 3. Mover los archivos al directorio actual
   echo "=== Reorganizando archivos ==="
   mv BookStore-monolith/* .
   rm -rf BookStore-monolith __MACOSX
   
   # 4. Configurar la aplicación para usar RDS
   echo "=== Configurando conexión a RDS ==="
   cat > config.py << 'EOL'
   import os
   
   SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bookstore_user:juandiego123@bookstore-db.cv48yui8kfd3.us-east-1.rds.amazonaws.com/bookstore'
   SECRET_KEY = 'secretkey'
   SQLALCHEMY_TRACK_MODIFICATIONS = False
   EOL
   
   # 5. Modificar docker-compose.yml para usar puerto 5002
   echo "=== Configurando Docker Compose con puerto 5002 ==="
   cat > docker-compose.yml << 'EOL'
   services:
     flaskapp:
       build: .
       restart: always
       environment:
         - FLASK_ENV=production
       ports:
         - "5002:5000"
   EOL
   
   # 6. Confirmar que Dockerfile existe
   echo "=== Verificando archivos críticos ==="
   if [ ! -f "Dockerfile" ]; then
     echo "❌ Error: Dockerfile no encontrado"
     ls -la
     exit 1
   fi
   
   # 7. Configurar Nginx
   echo "=== Configurando Nginx ==="
   sudo bash -c 'cat > /etc/nginx/conf.d/bookstore.conf << EOL
   server {
       listen 80;
       server_name proyecto2.tudominio.tld www.proyecto2.tudominio.tld;
       
       location / {
           proxy_pass http://localhost:5002;
           proxy_set_header Host \$host;
           proxy_set_header X-Real-IP \$remote_addr;
           proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto \$scheme;
       }
       
       location /.well-known/acme-challenge/ {
           root /var/www/html;
           try_files \$uri =404;
       }
   }
   EOL'
   
   # 8. Reiniciar Nginx
   echo "=== Reiniciando Nginx ==="
   sudo nginx -t && sudo systemctl restart nginx
   
   # 9. Construir e iniciar la aplicación
   echo "=== Construyendo e iniciando la aplicación ==="
   docker-compose down || true
   docker-compose up -d
   
   # 10. Configurar inicio automático en el arranque
   echo "=== Configurando inicio automático ==="
   cat > ~/start-bookstore.sh << 'EOL'
   #!/bin/bash
   cd ~/bookstore_final
   docker-compose up -d
   EOL
   chmod +x ~/start-bookstore.sh
   
   # Añadir al crontab para inicio automático
   (crontab -l 2>/dev/null || echo "") | grep -v "start-bookstore.sh" | echo "@reboot ~/start-bookstore.sh" - | crontab -
   
   echo "=== Despliegue de BookStore completado ==="
   echo "La aplicación ahora está disponible en: http://proyecto2.tudominio.tld"
   echo "Para ver los logs en tiempo real: docker-compose logs -f"
   EOF
   ```

 4. **Hacer el script ejecutable y ejecutarlo**:
   ```bash
   chmod +x deploy_bookstore_final.sh
   ./deploy_bookstore_final.sh
   ```

### 4. Crear una AMI de la aplicación

1. **En la consola de AWS > EC2 > Instances**:
   * Selecciona tu instancia actual (i-00b0ea8ffab1cd0d1)
   * Haz clic en "Actions" > "Image and templates" > "Create image"
   * Nombre: `bookstore-app-ami`
   * Descripción: "AMI de BookStore con RDS configurado para auto-escalamiento"
   * Haz clic en "Create image"
   * Anotar el ID de la AMI cuando se termine de crear

### 5. Crear una plantilla de lanzamiento

1. **En la consola EC2, ve a "Launch Templates"**:
   * Haz clic en "Create launch template"
   * Nombre: `bookstore-launch-template`
   * AMI: Selecciona la AMI que acabas de crear (`bookstore-app-ami`)
   * Tipo de instancia: t2.micro
   * Par de claves: Selecciona tu par de claves existente
   * Grupo de seguridad: `bookstore-app-sg` (sg-0573a0f8b5ba931dc)
   * Datos de usuario (opcional): Añade un script para iniciar la aplicación automáticamente:
     
     ```bash
     #!/bin/bash
     cd /home/ec2-user/bookstore_final
     docker-compose up -d
     ```
   * Hacer clic en "Create launch template"

### 6. Configurar balanceador de carga

1. **Crea un Application Load Balancer**:
   * En EC2 > "Load Balancers" > "Create Load Balancer"
   * Selecciona "Application Load Balancer"
   * Nombre: `bookstore-alb`
   * Esquema: Internet-facing
   * Mapeos: Selecciona todas las zonas de disponibilidad en tu región
   * Grupo de seguridad: Crea uno nuevo o usa el existente para el balanceador
   * Configura un listener HTTP (puerto 80)
   * Crea un grupo objetivo:
     * Nombre: `bookstore-target`
     * Tipo: Instances
     * Protocolo: HTTP
     * Puerto: 80
     * Comprobaciones de estado:
       * Ruta: /
       * Puerto: 5002 (el puerto que configuramos en nuestra aplicación)
       * Intervalo: 30 segundos
       * Tiempo de espera: 5 segundos
       * Umbral: 2 verificaciones consecutivas
   * Haz clic en "Create load balancer"

2. **Configura HTTPS en el balanceador**:
   * Se debe solicitar un certificado en AWS Certificate Manager para tu dominio
   * Una vez emitido, añadir un listener HTTPS (puerto 443) que use este certificado
   * Configurar la redirección de HTTP a HTTPS

### 7. Configurar grupo de Auto Scaling

1. **Crea un grupo de Auto Scaling**:
   * En EC2 > "Auto Scaling Groups" > "Create Auto Scaling group"
   * Nombre: `bookstore-asg`
   * Plantilla de lanzamiento: `bookstore-launch-template`
   * VPC y zonas: Selecciona tu VPC (vpc-0251ee5f51637233e) y todas las zonas disponibles
   * Adjuntar al balanceador de carga existente, seleccionando `bookstore-target`
   * Tamaño del grupo:
     * Capacidad deseada: 2
     * Capacidad mínima: 2
     * Capacidad máxima: 4
   * Políticas de escalado:
     * Tipo: Target tracking scaling
     * Métrica: CPU utilization
     * Valor objetivo: 70%
   * Hacer clic en "Create Auto Scaling group"
  
### 8. Actualizar DNS para apuntar al balanceador de carga

1. **Actualizar el dominio en GoDaddy**:
   * Obtener el DNS del balanceador de carga (algo como bookstore-alb-123456789.us-east-1.elb.amazonaws.com)
   * En GoDaddy, ir a DNS Management para proyecto2.libritosedwin.site
   * Modifica el registro A existente para que apunte al balanceador de carga:
     * Si el balanceador tiene una IP fija, usar un registro A
     * Si tiene un nombre DNS, usar un registro CNAME

2. **Verifica el despliegue escalable**:
   * Accede al dominio (`https://proyecto2.libritosedwin.site`)
   * Verificar que la aplicación funciona correctamente
   * Se puede monitorearlo desde la consola de AWS:
     * EC2 > Load Balancers > selecciona tu balanceador > pestaña "Monitoring"
     * EC2 > Auto Scaling Groups > selecciona tu grupo > pestaña "Monitoring"


## Ambiente de ejecución (OBJETIVO 3)
Para el Objetivo 3, implementaremos la aplicación BookStore monolítica en un clúster de Docker Swarm, manteniendo la misma funcionalidad pero aprovechando las capacidades de orquestación de contenedores.

### 1. Configuración de instancias para Docker Swarm  
#### 1.1. Crear tres instancias EC2 (Nodos)

Se necesitan 3 instancias EC2: 1 para el nodo manager y 2 para los nodos worker.

**Configuración de cada instancia:**
- AMI: Amazon Linux 2023
- Tipo: t2.micro o t3.micro
- Almacenamiento: 20 GB gp2
- Grupo de seguridad: Crea uno nuevo llamado `bookstore-swarm-sg` con las siguientes reglas:
  - SSH (22) desde tu IP
  - TCP (2377) para gestión del clúster Swarm
  - TCP/UDP (7946) para comunicación entre nodos
  - UDP (4789) para tráfico de red overlay (VXLAN)
  - HTTP (80) desde cualquier lugar
  - HTTPS (443) desde cualquier lugar

**Nombres sugeridos para identificar mejor las instancias:**
- `bookstore-swarm-manager`
- `bookstore-swarm-worker1`
- `bookstore-swarm-worker2`

  #### 1.2. Asignar IP elástica al nodo manager

1. En la consola AWS, ve a EC2 > Elastic IPs > Allocate Elastic IP address
2. Asocia la IP elástica a la instancia `bookstore-swarm-manager`
3. Anota la IP elástica: (en este caso nuestra IP Elástica es > 18.210.125.85) 

### 2. Instalación y configuración de Docker en todas las instancias

Conéctate a cada una de las tres instancias y ejecuta los siguientes comandos (EN CADA UNA DE LAS INSTANCIAS):

```bash
# Actualizar el sistema
sudo dnf update -y

# Instalar Docker
sudo dnf install -y docker

# Iniciar y habilitar Docker
sudo systemctl enable docker
sudo systemctl start docker

# Añadir el usuario ec2-user al grupo docker
sudo usermod -aG docker ec2-user

# Salir de la sesión SSH para que los cambios de grupo tengan efecto
exit
```

Vuelve a conectarte a cada instancia después de salir.

### 3. Inicializar Docker Swarm en el nodo manager (Despliegue en Docker Swarm)

Conéctate a la instancia `bookstore-swarm-manager` vía SSH:


Inicializar Swarm:

```bash
docker swarm init --advertise-addr <IP-PRIVADA-INSTANCIA-MANAGER>
```

El comando anterior generará un token de unión para los nodos worker. Copia este token ya que lo necesitarás para los siguientes pasos. El comando se verá algo así:

```bash
docker swarm join --token SWMTKN-1-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx $PRIVATE_IP:2377
```

### 4. Unir los nodos worker al Swarm

Conéctate a cada una de las instancias worker (`bookstore-swarm-worker1` y `bookstore-swarm-worker2`) y ejecuta (pega) el comando de unión que obtuviste en el paso anterior:

```bash
docker swarm join --token SWMTKN-1-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx [IP_PRIVADA_MANAGER]:2377
```

### 5. Verificar el Clúster Swarm

Vuelve a la instancia `bookstore-swarm-manager` y verifica que todos los nodos se hayan unido correctamente:

```bash
docker node ls
```

Deberías ver los tres nodos (1 manager con un asterisco y 2 workers), todos con estado "Ready".

### 6. Configurar Docker Hub

1. Registra una cuenta en https://hub.docker.com/repositories/jdacunag si no tienes una
2. En la instancia manager, inicia sesión en Docker Hub:

```bash
docker login
```

3. Ingresa tu nombre de usuario y contraseña cuando se te solicite
   
4. Debería aparecer un mensaje de que el inicio de sesión se realizó con éxito.

### 7. Crear y subir la imagen Docker de BookStore

En la instancia `bookstore-swarm-manager`:

Crear directorio para la aplicación:

```bash
mkdir -p ~/bookstore
cd ~/bookstore
```
Clonar el repositorio de BookStore:

```bash
sudo dnf install -y git

git clone https://github.com/jdacunag/Bookstore-P02.git

cd BookStore-P02/Bookstore-03
```

Modificar config.py para usar la base de datos RDS:
```bash
nano config.py
```

```bash
import os

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bookstore_user:juandiego123@bookstore-db.cv48yui8kfd3.us-east-1.rds.amazonaws.com/bookstore'
SECRET_KEY = 'secretkey'
SQLALCHEMY_TRACK_MODIFICATIONS = False
```
Editar el Dockerfile para que use "curl" (En el github ya esta implementado):

```bash
# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Ensure application health checks are available
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
  CMD curl -f http://localhost:5000/ || exit 1

# Comando para correr la app
CMD ["python", "app.py"]
```

**NOTA:** Se debe agregar una "Regla de entrada" (con MySQL/Aurora (3306)) en la base de datos RDS (en este caso la misma para el objetivo 2), donde se pueda conectar el security group asociado a los nodos manager y worker o directamente la conectar el nodo manager a dicha base de datos RDS.

Construir la imagen Docker

```bash
docker build -t bookstore:latest .

# Etiquetar la imagen para tu repositorio de Docker Hub
docker tag bookstore:latest jdacunag/bookstore-03:latest 

# Subir la imagen a Docker Hub
docker push jdacunag/bookstore-03:latest
```
### 8. Crear y configurar el archivo docker-stack.yml

En la instancia `bookstore-swarm-manager`:

Crear el archivo docker-stack.yml:

```bash
nano docker-stack.yml
```
Copiar lo siguiente en el archivo:

```bash
version: '3.8'

services:
  bookstore:
    # Usa la imagen que subiste a Docker Hub o ECR
    image: jdacunag/bookstore-03:latest
    deploy:
      replicas: 3
      update_config:
        parallelism: 1
        delay: 10s
        order: start-first
      restart_policy:
        condition: on-failure
        max_attempts: 3
      placement:
        constraints: [node.role == worker]
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.1'
          memory: 128M
    environment:
      - FLASK_ENV=production
       - DATABASE_URI=mysql+pymysql://bookstore_user:juandiego123@bookstore-db.cv48yui8kfd3.us-east-1.rds.amazonaws.com/bookstore
      - SECRET_KEY=secretkey
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    networks:
      - bookstore-network

  visualizer:
    image: dockersamples/visualizer:latest
    ports:
      - "8080:8080"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    deploy:
      placement:
        constraints: [node.role == manager]
    networks:
      - bookstore-network

  proxy:
    image: nginx:latest
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/conf.d:/etc/nginx/conf.d
      - ./nginx/ssl:/etc/nginx/ssl
    deploy:
      placement:
        constraints: [node.role == manager]
      replicas: 1
    networks:
      - bookstore-network

networks:
  bookstore-network:
    driver: overlay
    attachable: true
```
### 9. Configurar Nginx como proxy inverso

Crear la estructura de directorios para nginx:

```bash
mkdir -p nginx/conf.d
mkdir -p nginx/html
mkdir -p nginx/ssl
```
Crear la configuración inicial de nginx para HTTP:

```bash
cd nginx/conf.d
nano bookstore.conf
```
Copiar lo siguiente en el archivo:

```bash
server {
    listen 80;
    server_name proyecto3.libritosedwin.site;
    
    location / {
        proxy_pass http://bookstore-03_bookstore:5000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
    
    # Para validación Let's Encrypt
    location /.well-known/acme-challenge/ {
        root /usr/share/nginx/html;
        try_files \$uri =404;
    }
}
```

Crear una página HTML básica para pruebas:
```bash
cd nginx/html
nano index.html
```

```bash
<!DOCTYPE html>
<html>
<head>
    <title>Bookstore Docker Swarm Test</title>
</head>
<body>
    <h1>Bookstore Docker Swarm</h1>
    <p>Nginx proxy está funcionando correctamente!</p>
</body>
</html>
```

Establecer permisos correctos:

```bash
chmod -R 755 nginx/
```

### 10. Desplegar el stack en Docker Swarm

```bash
cd ~/Bookstore-03
docker stack deploy -c docker-stack.yml bookstore-03
```

### 11. Verificar el despliegue del stack

```bash
# Ver los servicios desplegados
docker stack services bookstore-03

# Ver las tareas (contenedores) en ejecución
docker stack ps bookstore-03

# Ver los servicios en detalle
docker service ls
```

Todos los servicios deberían mostrar el estado "Running" y el número correcto de réplicas.

### 12. Configurar DNS para apuntar al nodo manager

#### Actualizar registro DNS en GoDaddy

1. En GoDaddy o tu proveedor DNS, crea un registro A para "proyecto3" que apunte a la IP elástica del nodo manager:
   - **Tipo**: A
   - **Nombre**: proyecto3
   - **Valor**: [IP-ELÁSTICA-DEL-NODO-MANAGER]
   - **TTL**: 600 segundos

2. Espera a que se propague el DNS (puede tomar unos minutos)

#### Verificar la propagación DNS

```bash
nslookup proyecto3.libritosedwin.site
```

Deberías ver que apunta a la IP elástica de tu nodo manager.

## 13. Configurar SSL con Certbot

Instalar Certbot: 

```bash
Instalar Certbot
sudo dnf install -y certbot
```

Obtener certificado usando el modo standalone:

```bash
# (Detendremos temporalmente Nginx para esto)
docker service scale bookstore-03_proxy=0
sudo certbot certonly --standalone -d proyecto3.libritosedwin.site
# Aquí se debe ingresar un correo electrónico para recibir el certificado
```

Copiar certificados al directorio de Nginx:

```bash
sudo cp /etc/letsencrypt/live/proyecto3.libritosedwin.site/fullchain.pem ~bookstore/Bookstore-P02/Bookstore-03/nginx/ssl/
sudo cp /etc/letsencrypt/live/proyecto3.libritosedwin.site/privkey.pem ~bookstore/Bookstore-P02/Bookstore-03/nginx/ssl/
sudo chown ec2-user:ec2-user ~bookstore/Bookstore-P02/Bookstore-03/nginx/ssl/*.pem
```
Asegurarse de que los permisos sean correctos:

```bash
chmod 644 ~/Bookstore-03/nginx/ssl/*.pem
```

Actualizar la configuración de Nginx para habilitar HTTPS:

```bash
cd nginx/conf.d
nano bookstore.conf
```
Añadir el server para que use HTTPS a la configuración:

```bash
server {
    listen 80;
    server_name proyecto3.libritosedwin.site;
    
    # Redirige HTTP a HTTPS
    return 301 https://\$host\$request_uri;
    
    location /.well-known/acme-challenge/ {
        root /usr/share/nginx/html;
        try_files \$uri =404;
    }
}

server {
    listen 443 ssl;
    server_name proyecto3.libritosedwin.site;

    ssl_certificate /etc/nginx/ssl/fullchain.pem;
    ssl_certificate_key /etc/nginx/ssl/privkey.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512:ECDHE-RSA-AES256-GCM-SHA384;
    ssl_session_timeout 1d;
    ssl_session_cache shared:SSL:10m;
    ssl_session_tickets off;

    location / {
        proxy_pass http://bookstore-03_bookstore:5000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
```


Reiniciar el servicio proxy:

```bash
docker service scale bookstore-03_proxy=1
```

Verifica que todo funcione correctamente:

```bash
# Espera a que el servicio se inicie
sleep 10

# Verifica el estado del servicio
docker service ps bookstore-03_proxy

# Comprueba los logs
docker service logs bookstore-03_proxy
```


### 14. Probar el escalamiento de servicios

```bash
# Escalar el servicio de bookstore a 5 réplicas
docker service scale bookstore-03_bookstore=5

# Verificar que el escalamiento funcionó
docker service ls
docker stack ps bookstore-03
```

### 15. Configurar monitorización básica

```bash
# Verificar el dashboard de visualizer
echo "Visualizer disponible en: http://$(curl -s ifconfig.me):8080"
```

### 16. Verificar el despliegue

1. Abre tu navegador y navega a `https://proyecto3.libritosedwin.site`
2. Deberías estar la aplicación BookStore funcionando correctamente con HTTPS


## Referencias

* https://claude.ai/public/artifacts/688a7e93-3dd1-43a6-a232-33f21f976b99

* https://hub.docker.com/repository/docker/jdacunag/bookstore-03/general
  
* https://claude.ai/public/artifacts/037e9bd2-5ddb-41dd-b0e9-64811ecadb37 
  
  
