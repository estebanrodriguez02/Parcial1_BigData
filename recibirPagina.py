# import boto3
# from datetime import datetime
# from bs4 import BeautifulSoup


# def pagina():
#     nombre = str(datetime.today().strftime('%Y-%m-%d'))
#     s3 = boto3.resource('s3')
#     bucket = s3.Bucket('parcial1bigdata')
#     obj_tiempo = bucket.Object(str("news/raw/" +
#                                    "eltiempo-" + nombre +
#                                    ".html"))
#     body_tiempo = obj_tiempo.get()['Body'].read()

#     html_tiempo = BeautifulSoup(body_tiempo, 'html.parser')
#     data_noticias_tiempo = html_tiempo.find_all('article')
#     csv_tiempo = ""
#     linea_0 = "Nombre; Categoria; Link\n"
#     for i in range(len(data_noticias_tiempo)):
#         link = "eltiempo.com" + \
#                data_noticias_tiempo[i].find('a',
#                                             class_='title page-link')['href']
#         name = data_noticias_tiempo[i]['data-name'].replace(",", "")
#         category = data_noticias_tiempo[i]['data-seccion']
#         csv_tiempo += category + ";" + \
#             name + ";" + \
#             link + \
#             "\n"

#     boto3.client('s3').put_object(Body=csv_tiempo,
#                                   Bucket='parcial1bigdata',
#                                   Key=str('headlines/final' +
#                                           '/periodico=eltiempo/year=' +
#                                           nombre[:4]+'-month=' +
#                                           nombre[5:7]+'-day=' +
#                                           nombre[8:]+'-eltiempo.csv'))


# pagina()


import boto3
from datetime import datetime
from bs4 import BeautifulSoup


def pagina():
    nombre = str(datetime.today().strftime('%Y-%m-%d'))
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('parcial1bigdata')
    bucket_name = 'parcial1bigdata'
    
    # Check if a CSV file exists in the bucket
    existing_objects = s3.meta.client.list_objects_v2(Bucket=bucket_name, Prefix='headlines/final/')
    for obj in existing_objects.get('Contents', []):
        if obj['Key'].endswith('-eltiempo.csv'):
            s3.Object(bucket_name, obj['Key']).delete()

    
    obj_tiempo = bucket.Object(str("news/raw/" +
                                   "eltiempo-" + nombre +
                                   ".html"))
    body_tiempo = obj_tiempo.get()['Body'].read()

    html_tiempo = BeautifulSoup(body_tiempo, 'html.parser')
    data_noticias_tiempo = html_tiempo.find_all('article')
    csv_tiempo = ""
    linea_0 = "Nombre; Categoria; Link\n"

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

    if not csv_tiempo.startswith(linea_0):
        csv_tiempo = linea_0 + csv_tiempo

    boto3.client('s3').put_object(Body=csv_tiempo,
                                  Bucket='parcial1bigdata',
                                  Key=str('headlines/final' +
                                          '/periodico=eltiempo/year=' +
                                          nombre[:4]+'-month=' +
                                          nombre[5:7]+'-day=' +
                                          nombre[8:]+'-eltiempo.csv'))


pagina()

