import datetime
import locale
from lxml import html
import requests
from pathlib import Path


def scrap_csv(urls):
    # Se obtiene la fecha y el nombre del mes en español
    locale.setlocale(locale.LC_TIME, 'es_ES.utf8')
    fecha = datetime.datetime.now()

    # Se generan los nombres de la ruta del archivo
    subcarpeta = fecha.strftime("//%Y-%B//")  # todo ver si se debe guardar en la carpeta actual
    sufijo_nombre = fecha.strftime("-%d-%m-%Y")

    for url in urls:
        # Teniendo en cuenta que el url del csv puede variar, se obtiene el url donde se
        # encuentra el archivo csv a partir del xpath en la url base
        page = requests.get(url)
        webpage = html.fromstring(page.content)
        csv_url = webpage.xpath('/html/body/div[1]/div[2]/div/div/div[3]/a[1]/@href')[0]

        # Se obtiene el nombre de la categoría
        categoria = csv_url.split('/')[-1].split('.')[0]

        # Se crea el directorio donde se guardará el archivo csv
        ubicacion = f".//{categoria}//{subcarpeta}//"
        Path(ubicacion).mkdir(parents=True, exist_ok=True)

        # Se obtiene el archivo csv del url y se lo guarda siguiendo el formato pedido
        req = requests.get(csv_url)
        url_content = req.content
        csv_file = open(ubicacion+categoria+sufijo_nombre+".csv", 'wb')
        csv_file.write(url_content)
        csv_file.close()


if __name__ == '__main__':
    test_urls = [
        "https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_4207def0-2ff7-41d5-9095-d42ae8207a5d",
        "https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_392ce1a8-ef11-4776-b280-6f1c7fae16ae",
        "https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_01c6c048-dbeb-44e0-8efa-6944f73715d7"]
    scrap_csv(test_urls)
