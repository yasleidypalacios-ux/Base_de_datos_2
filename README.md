# Base de Datos con SQLAlchemy y Faker

Proyecto de la materia **Bases de Datos **.  
Este script en Python crea y llena automáticamente una base de datos MySQL con 100.000 registros de datos falsos usando Faker.

## ¿Qué hace?
- Se conecta a MySQL usando SQLAlchemy
- Crea automáticamente la tabla `personas_yasleidy` si no existe
- Genera e inserta 100.000 registros de colombianos en lotes de 5.000 para mayor eficiencia 

## Requisitos
- Python 3.11 o superiores
- MySQL en ejecucion local 

## Instalación de dependencias

1. Clona el repositorio:
```bash
git clone https://github.com/yasleidypalacios-ux/Base_de_datos_2.git
cd Base_de_datos_2
```

2. Crea y activa el entorno virtual:
```bash
py -m venv .venv
.venv\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```
## Configuración del entorno (.env)
4. Crear el archivo .env tomando como base el archivo .env.example. Este debe abrirse en un editor de texto (por ejemplo, Notepad) y configurarse con los datos de conexión correspondientes:
DB_USER=root
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=3306
DB_NAME=nombre_de_tu_base_de_datos

5. Antes de ejecutar el proyecto, asegúrate de haber creado la base de datos en MySQL. 
## Ejecución
Para ejecutar el script:
```bash
py main.py