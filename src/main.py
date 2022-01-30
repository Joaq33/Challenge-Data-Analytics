from scrap_csv import scrap_csv
from process_data import process_data
from db_create_tables import db_create_tables
from db_update_tables import db_update_tables
import logging

# Establesco el nivel de logging
logging.basicConfig(level=logging.INFO)

# Archivos fuente
logging.info("Cargando archivos fuente")
urls = [
    "https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_4207def0-2ff7-41d5-9095-d42ae8207a5d",
    "https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_392ce1a8-ef11-4776-b280-6f1c7fae16ae",
    "https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_01c6c048-dbeb-44e0-8efa-6944f73715d7"]

scrap_csv(urls)

# Procesamiento de datos
logging.info("Procesando datos")
primera_tabla, segunda_tabla = process_data()

# Creación de tablas en la Base de datos
logging.info("Creando tablas en la Base de datos")
engine = db_create_tables()

# Actualización de la base de datos
logging.info("Actualizando tablas en la Base de datos")
db_update_tables(primera_tabla, segunda_tabla, engine)
