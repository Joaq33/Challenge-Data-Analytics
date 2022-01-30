from datetime import datetime
import logging


def db_update_tables(tabla1, tabla2, engine):
    """
    Funcion que actualiza las tablas de la base de datos.
    :param tabla1:
    :param tabla2:
    :param engine:
    :return:
    """
    # Agrego la columna de fecha de carga
    tabla1["Fecha de carga"] = tabla2["Fecha de carga"] = datetime.now()
    try:
        tabla1.to_sql("tabla_conjunta", con=engine, if_exists='replace', index=False)

        tabla2.to_sql("datos_cine", con=engine, if_exists='replace', index=False)
    except Exception as e:
        logging.error("Error al actualizar base de datos: {}".format(e))
