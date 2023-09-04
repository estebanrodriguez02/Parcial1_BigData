from recibirPagina import get_titularNoticias
from leerPagina import get_url_tiempo
import requests
from bs4 import BeautifulSoup


def test_get_titularNoticias():

    get = get_titularNoticias()
    url = "https://www.eltiempo.com/"
    # Realizar una solicitud GET a la página
    response = requests.get(url)
    # Parsear el contenido HTML de la página
    soup = BeautifulSoup(response.text, 'html.parser')
    # Encontrar el primer titular
    primer_titular = soup.find('a', class_='title page-link').text
    assert get == primer_titular

def test_contenedoresHTML():
    # Realizar una solicitud GET a la página "eltiempo.com"
    url = get_url_tiempo()
    response = requests.get(url)
    html_tiempo = BeautifulSoup(response.text, 'html.parser')
    # Verificar si hay al menos una etiqueta <a> en la página
    a_tags = html_tiempo.find_all('a')
    assert len(a_tags) > 0, "No se encontraron etiquetas <a> en la página"
    # Verificar si hay al menos una etiqueta <h1> en la página
    h1_tags = html_tiempo.find_all('h1')
    assert len(h1_tags) > 0, "No se encontraron etiquetas <h1> en la página"
    # Verificar si hay al menos una etiqueta <p> en la página
    p_tags = html_tiempo.find_all('p')
    assert len(p_tags) > 0, "No se encontraron etiquetas <p> en la página"
    
