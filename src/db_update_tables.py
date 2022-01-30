from datetime import datetime


def db_update_tables(tabla1, tabla2, engine):
    """
    Funcion que actualiza las tablas de la base de datos.
    :param tabla1:
    :param tabla2:
    :param engine:
    :return:
    """
    tabla1["Fecha de carga"] = tabla2["Fecha de carga"] = datetime.now()

    tabla1.to_sql("tabla_conjunta", con=engine, if_exists='replace', index=False)

    tabla2.to_sql("datos_cine", con=engine, if_exists='replace', index=False)
