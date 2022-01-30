import pandas as pd
import os


normalized_list = ("cod_localidad",
                   "id_provincia",
                   "id_departamento",
                   "categoría",
                   "provincia",
                   "localidad",
                   "nombre",
                   "domicilio",
                   "código postal",
                   "número de teléfono",
                   "mail",
                   "web")


def extract_and_rename(ubicaciones, categories, new_names=normalized_list):
    """
    Extrae las columnas deseadas de los archivos csv, las combina y las renombra.
    :param new_names:
    :param ubicaciones:
    :param categories:
    :return:
    """
    tabla_base = pd.DataFrame(columns=new_names)
    for ubicacion in ubicaciones:
        df = pd.read_csv(ubicacion)
        cur_tabla = df[categories]
        for index, normalized in enumerate(new_names):
            cur_tabla.columns.values[index] = normalized
        tabla_base = pd.concat([tabla_base, cur_tabla])
    return tabla_base


def get_file_list(ruta_base):
    """
    Obtiene una lista de archivos de un directorio.
    :param ruta_base:
    :return:
    """
    lista_de_archivos = os.listdir(ruta_base)
    ans = list()
    for entry in lista_de_archivos:
        # creo ruta completa
        ruta_completa = os.path.join(ruta_base, entry)
        # si es una carpeta, llamo recursivamente a esta funcion
        if os.path.isdir(ruta_completa):
            ans = ans + get_file_list(ruta_completa)
        else:
            ans.append(ruta_completa)
    return ans


def process_data():
    """
    Genero las tablas pedidas a partir de los csv
    :return:
    """
    # Tabla de datos de bibliotecas
    columnas_biblio = ["Cod_Loc",
                       "IdProvincia",
                       "IdDepartamento",
                       "Categoría",
                       "Provincia",
                       "Localidad",
                       "Nombre",
                       "Domicilio",
                       "CP",
                       "Teléfono",
                       "Mail",
                       "Web"]
    ubicaciones_biblio = get_file_list("../csv_files/biblioteca_popular")
    normalized_table_biblio = extract_and_rename(ubicaciones_biblio, columnas_biblio)

    # Tabla de datos de museos
    columnas_museo = ["Cod_Loc",
                      "IdProvincia",
                      "IdDepartamento",
                      "categoria",
                      "provincia",
                      "localidad",
                      "nombre",
                      "direccion",
                      "CP",
                      "telefono",
                      "Mail",
                      "Web"]
    ubicaciones_museo = get_file_list("../csv_files/museo")
    normalized_table_museo = extract_and_rename(ubicaciones_museo, columnas_museo)

    # Tabla de datos de cines
    columnas_cine = ["Cod_Loc",
                     "IdProvincia",
                     "IdDepartamento",
                     "Categoría",
                     "Provincia",
                     "Localidad",
                     "Nombre",
                     "Dirección",
                     "CP",
                     "Teléfono",
                     "Mail",
                     "Web"]
    ubicaciones_cine = get_file_list("../csv_files/cine")
    normalized_table_cine = extract_and_rename(ubicaciones_cine, columnas_cine)

    # Concateno las tablas generadas anteriormente
    tabla_conjunta = pd.concat([normalized_table_museo, normalized_table_cine, normalized_table_biblio])

    # CREO PRIMERA TABLA

    # Filtro por categoría
    primera_tabla = tabla_conjunta["categoría"].value_counts().reset_index(name="Cantidad de registros")
    primera_tabla.rename(columns={"index": "Filtro"}, inplace=True)

    # Filtro por fuente
    largo_tabla = len(primera_tabla)
    primera_tabla.loc[largo_tabla] = ["Bibliotecas", len(normalized_table_biblio)]
    primera_tabla.loc[largo_tabla + 1] = ["Museos", len(normalized_table_museo)]
    primera_tabla.loc[largo_tabla + 2] = ["Cines", len(normalized_table_cine)]

    # Filtro de provincia + categoría
    agrupaciones = tabla_conjunta.groupby(["provincia", "categoría"]).size().reset_index(name="Cantidad de registros")
    agrupaciones["Filtro"] = agrupaciones["provincia"] + ": " + agrupaciones["categoría"]
    agrupaciones = agrupaciones.drop(columns=["categoría", "provincia"])
    primera_tabla = pd.concat([primera_tabla, agrupaciones])

    # CREO SEGUNDA TABLA

    columnas_originales = ["Provincia",
                           "Pantallas",
                           "Butacas",
                           "espacio_INCAA"]

    columnas_renombradas = ["Provincia",
                            "Cantidad de pantallas",
                            "Cantidad de butacas",
                            "Cantidad de espacios INCAA"]

    segunda_tabla = extract_and_rename(ubicaciones_cine, columnas_originales, columnas_renombradas)

    # Devuelvo las tablas
    return primera_tabla, segunda_tabla


if __name__ == '__main__':
    primera_tabla, segunda_tabla = process_data()
    print(primera_tabla.head())
    print(segunda_tabla.head())
