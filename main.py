import os
from dotenv import load_dotenv
from sqlalchemy import (
    create_engine, Column, Integer, String,
    Date, Float, Text, MetaData, Table
)

load_dotenv()

TABLE_NAME = "personas_yasleidy"

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
        Column("correo",           String(150), nullable=False),
        Column("fecha_nacimiento", Date,        nullable=False),
        Column("ciudad",           String(100), nullable=False),
        Column("telefono",         String(30),  nullable=False),
        Column("ocupacion",        String(100), nullable=False),
        Column("salario",          Float,       nullable=False),
    )

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

if __name__ == "__main__":
    main()