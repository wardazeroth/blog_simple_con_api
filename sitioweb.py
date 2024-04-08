import requests
import json
from html_maker import make_col3
from html_maker import crear_html

url = 'https://jsonplaceholder.typicode.com/photos'
response = requests.get(url)
# print(response.text)

#2. Transformar el resultado
photos = json.loads(response.text)

#3. Acortamos la lista 
photos = photos[0:8]

#4 Armamos el texto que contiene cols_3
cols_3 = make_col3(photos)

#4. Armamos el texto que contiene todas las col_3
cuerpo_html = crear_html(cols_3) 
    
def crear_html():
    with open('index.html', 'w', encoding='utf-8') as f:
        return f.write(cuerpo_html)
crear_html()
