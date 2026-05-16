import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

def get_engine():
    user     = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host     = os.getenv("DB_HOST", "localhost")
    port     = os.getenv("DB_PORT", "3306")
    db_name  = os.getenv("DB_NAME")

    connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}"
    engine = create_engine(connection_string, echo=False)
    return engine

def main():
    print("Conectando a MySQL...")
    engine = get_engine()
    with engine.connect() as conn:
        print("Conexion exitosa ✓")

if __name__ == "__main__":
    main()