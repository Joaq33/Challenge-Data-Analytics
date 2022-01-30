from sqlalchemy import create_engine, text
from decouple import AutoConfig


def db_create_tables():
    """
    Crea tablas en la base de datos
    :return:
    """
    # selecciono carpeta raiz del proyecto para variables de entorno
    config = AutoConfig(search_path='../')

    configuraciones_db = {
        'user': config("USER"),
        'password': config("PASSWORD"),
        'host': config("HOST"),
        'port': config("PORT")
    }

    # creo uri de conexion
    uri_base = "postgresql://{user}:{password}@{host}:{port}/{database}"

    uri_conexion_db = (uri_base.format(
        database='postgres',
        **configuraciones_db))

    # conexion a la base de datos
    engine = create_engine(uri_conexion_db)

    with engine.connect() as con:
        file = open("../scripts/db_creation.sql")
        query = text(file.read())
        con.execute(query)

    return engine
