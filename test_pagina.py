from datetime import datetime
from leerPagina import get_url_tiempo, get_date

def test_get_date():
    dt = get_date()
    assert dt == datetime.today().strftime('%Y-%m-%d')

def test_get_url_tiempo():
    assert get_url_tiempo() == "https://www.eltiempo.com/"
