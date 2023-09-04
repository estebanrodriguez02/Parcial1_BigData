from datetime import datetime
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


def test_get_url_tiempo():
    assert get_url_tiempo() == "https://www.eltiempo.com/"
