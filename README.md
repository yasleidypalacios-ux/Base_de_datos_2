# Base de Datos con SQLAlchemy y Faker

Proyecto de la materia **Bases de Datos **.  
Script en Python que crea e ingresa automáticamente una base de datos
MySQL con 100.000 registros con datos falsos usando Faker.

## ¿Qué hace?
- Se conecta a MySQL usando SQLAlchemy
- Crea la tabla `personas_yasleidy` automáticamente si no existe
- Genera e inserta 100.000 registros de colombianos en bloques de 5.000

## Requisitos
- Python 3.11 
- MySQL corriendo localmente

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/yasleidypalacios-ux/Base_de_datos_2.git
cd Base_de_datos_2
```

2. Crea y activa el entorno virtual:
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Crea el archivo `.env` apartir de `.env.example` y se llena con tu informacion :
DB_USER=root
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=3306
DB_NAME=base_de_datos_faker
## Ejecución
```bash
python main.py