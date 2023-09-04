import boto3
from datetime import datetime
from bs4 import BeautifulSoup
primer_titular = ""  # Declarar primer_titular como una variable global
def pagina():
    global primer_titular  # Acceder a la variable global primer_titular
    nombre = str(datetime.today().strftime('%Y-%m-%d'))
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('parcial1bdf1')
    obj_tiempo = bucket.Object(str("news/raw/" +
                                   "eltiempo-" + nombre +
                                   ".html"))
    body_tiempo = obj_tiempo.get()['Body'].read()

    html_tiempo = BeautifulSoup(body_tiempo, 'html.parser')
    primer_titular = html_tiempo.find('a', class_='title page-link').text
    data_noticias_tiempo = html_tiempo.find_all('article')
    csv_tiempo = ""
    for i in range(len(data_noticias_tiempo)):
        link = "eltiempo.com" + \
               data_noticias_tiempo[i].find('a',
                                            class_='title page-link')['href']
        name = data_noticias_tiempo[i]['data-name'].replace(",", "")
        category = data_noticias_tiempo[i]['data-seccion']
        csv_tiempo += category + ";" + \
            name + ";" + \
            link + \
            "\n"

    boto3.client('s3').put_object(Body=csv_tiempo,
                                  Bucket='parcial1bdf2',
                                  Key=str('headlines/final' +
                                          '/periodico=eltiempo/year=' +
                                          nombre[:4]+'-month=' +
                                          nombre[5:7]+'-day=' +
                                          nombre[8:]+'-eltiempo.csv'))
    pagina()

def get_titularNoticias():
    global primer_titular  # Acceder a la variable global primer_titular
    return primer_titular

