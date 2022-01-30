CREATE TABLE IF NOT EXISTS public.tabla_conjunta
(
    "Filtro" character varying(50),
    "Cantidad de registros" integer,
    "Fecha de carga" date,
    PRIMARY KEY ("Filtro")
);

CREATE TABLE IF NOT EXISTS public.datos_cine
(
    "Provincia" character varying(40),
    "Cantidad de pantallas" integer,
    "Cantidad de butacas" integer,
    "Cantidad de espacios INCAA" integer,
    "Fecha de carga" date,
    PRIMARY KEY ("Provincia")
)