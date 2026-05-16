import os
import random
from dotenv import load_dotenv
from sqlalchemy import (
    create_engine, Column, Integer, String,
    Date, Float, Text, MetaData, Table
)
from faker import Faker

load_dotenv()

TABLE_NAME = "personas_yasleidy"
BATCH_SIZE = 5000
TOTAL_RECORDS = 100000

CIUDADES_COLOMBIA = [
    "Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena",
    "Cúcuta", "Bucaramanga", "Pereira", "Santa Marta", "Ibagué",
    "Pasto", "Manizales", "Neiva", "Villavicencio", "Armenia",
    "Valledupar", "Montería", "Sincelejo", "Popayán", "Tunja"
]

def get_engine():
    user     = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host     = os.getenv("DB_HOST", "localhost")
    port     = os.getenv("DB_PORT", "3306")
    db_name  = os.getenv("DB_NAME")

    connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}"
    engine = create_engine(connection_string, echo=False)
    return engine

def get_table(metadata):
    return Table(
        TABLE_NAME,
        metadata,
        Column("id",               Integer, primary_key=True, autoincrement=True),
        Column("nombre",           String(100), nullable=False),
        Column("apellido",         String(100), nullable=False),
        Column("correo",           String(150), nullable=False),
        Column("fecha_nacimiento", Date,        nullable=False),
        Column("ciudad",           String(100), nullable=False),
        Column("telefono",         String(30),  nullable=False),
        Column("ocupacion",        String(100), nullable=False),
        Column("salario",          Float,       nullable=False)
    )

def generate_batch(faker, size):
    batch = []
    for _ in range(size):
        batch.append({
            "nombre":           faker.first_name(),
            "apellido":         faker.last_name(),
            "correo":           faker.unique.email(),
            "fecha_nacimiento": faker.date_of_birth(minimum_age=18, maximum_age=80),
            "ciudad":           random.choice(CIUDADES_COLOMBIA),
            "telefono":         faker.phone_number()[:30],
            "ocupacion":        faker.job()[:100],
            "salario":          round(faker.pyfloat(min_value=400, max_value=15000, right_digits=2), 2)
        })
    return batch

def main():
    print("Conectando a MySQL...")
    engine = get_engine()
    with engine.connect() as conn:
        print("Conexion exitosa ✓")

    print(f"Creando tabla '{TABLE_NAME}' si no existe...")
    metadata = MetaData()
    table = get_table(metadata)
    metadata.create_all(engine)
    print("Tabla lista ✓")

    print(f"Insertando {TOTAL_RECORDS:,} registros en lotes de {BATCH_SIZE:,}...")
    faker = Faker("es_CO")
    inserted = 0

    with engine.begin() as conn:
        while inserted < TOTAL_RECORDS:
            current_batch = min(BATCH_SIZE, TOTAL_RECORDS - inserted)
            batch = generate_batch(faker, current_batch)
            conn.execute(table.insert(), batch)
            inserted += current_batch
            pct = (inserted / TOTAL_RECORDS) * 100
            print(f"  {inserted:>7,} / {TOTAL_RECORDS:,} ({pct:.1f}%)")

    print("\n¡Insercion completada exitosamente!")

if __name__ == "__main__":
    main()