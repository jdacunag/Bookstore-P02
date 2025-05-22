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
Desplegar la aplicación BookStore Monolítica en una Máquina Virtual en AWS, con un dominio propio, certificado SSL y Proxy inverso en NGINX. 

#### Diagrama de la Arquitectura


### Objetivo 2
Realizar el escalamiento en nube de la aplicación monolítica, siguiente algún patrón de arquitectura de escalamiento de apps monolíticas en AWS. La aplicación debe ser escalada utilizando Máquinas Virtuales (VM) con autoescalamiento, base de datos aparte Administrada o si es implementada con VM con Alta Disponibilidad, y Archivos compartidos vía NFS (como un servicio o una VM con NFS con Alta Disponibilidad).

```
cat > deploy_bookstore_final.sh << 'EOF'
#!/bin/bash
# Script corregido final para desplegar BookStore completo con RDS

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
#### Diagrama de la Arquitectura

### Objetivo 3
En el objetivo 3, se conservará mucho de lo desarrollado en el objetivo 2, pero en vez se utilizar máquinas virtuales en autoescalamiento, se utilizará un clúster.
Escalar la app monolitica en Kubernetes o Docker Swarm (en este caso usamos Docker Swarm), en vez de contenedores son pods en un cluster y que se conecten externamente a la base de datos.

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
#### Diagrama de la Arquitectura

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

### Ambiente de ejecución (OBJETIVO 3)
#### Despliegue en Docker Swarm


## Referencias
