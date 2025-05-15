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

## 2. Información general del proyecto

## 3. Descripción del ambiente de desarrollo y técnico

## 4. Descripción del ambiente de EJECUCIÓN (en producción)
