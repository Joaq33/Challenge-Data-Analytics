from sqlalchemy import create_engine, text
from decouple import AutoConfig
import logging


def db_create_tables():
    """
    Crea tablas en la base de datos
    :return:
    """
    # selecciono carpeta raiz del proyecto para variables de entorno
    config = AutoConfig(search_path='../')

    try:
        configuraciones_db = {
            'user': config("USER"),
            'password': config("PASSWORD"),
            'host': config("HOST"),
            'port': config("PORT")
        }
    except Exception as e:
        logging.error("No se pudo leer el archivo de configuraciones: {}".format(e))

    # creo uri de conexion
    uri_base = "postgresql://{user}:{password}@{host}:{port}/{database}"

    uri_conexion_db = (uri_base.format(
        database='postgres',
        **configuraciones_db))

    # conexion a la base de datos
    engine = create_engine(uri_conexion_db)

    try:
        with engine.connect() as con:
            file = open("../scripts/db_creation.sql")
            query = text(file.read())
            con.execute(query)
    except Exception as e:
        logging.error("No se pudo crear las tablas: {}".format(e))

    return engine
