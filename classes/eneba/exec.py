
# Importar librerías
import time
from bs4 import BeautifulSoup
import requests
import logging
from eneba import Eneba

# Establecer nivel de depuración
logging.basicConfig(level=logging.DEBUG)

# Inicializar variables
eneba = Eneba()

# Iniciar bucle
while True:
    error_count = 0
    # Depurar URL
    logging.debug(f"Obteniendo registros de: {eneba.get_url()}")
    logging.debug(f"Página actual: {eneba.get_page()}")
    # Realizar petición
    request = requests.get(eneba.get_url())
    # Validar respuesta
    if request.status_code == 200:
        # Obtener contenido HTML
        soup = BeautifulSoup(request.text, "html.parser")
        # Obtener registros
        s = soup.find_all("div", class_="pFaGHa WpvaUk")
        # Validar registros
        if not s:
            logging.debug("No se encontraron registros")
            break
        # Iterar sobre registros
        for games in s:
            # Obtener nombre
            name = games.find(eneba.get_coordinates().get('name').get('type'), class_=eneba.get_coordinates().get('name').get('class')).text
            # Obtener precio
            price = games.find(eneba.get_coordinates().get('price').get('type'), class_=eneba.get_coordinates().get('name').get('class')).text
            # Obtener región
            region = games.find(eneba.get_coordinates().get('region').get('type'), class_=eneba.get_coordinates().get('region').get('class')).text
            # Imprimir resultados
            logging.debug(f"Nombre: {name}, Precio: {price}, Región: {region}")
    else:
        # Incrementar contador de errores
        error_count += 1
        # Imprimir error
        logging.error(f"Error {request.status_code}: {request.reason}")
        # Esperar 5 segundos antes de reintentar
        time.sleep(5)
        # Si se alcanza el máximo de intentos, finalizar bucle
        if error_count == 5:
            break
    # Incrementar página
    eneba.set_page(eneba.get_page() + 1)