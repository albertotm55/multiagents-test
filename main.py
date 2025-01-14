import requests
from bs4 import BeautifulSoup

# URL del sitio web
url = 'https://www.bbva.com/'

# Realiza la solicitud HTTP
response = requests.get(url)

# Verifica que la solicitud fue exitosa
if response.status_code == 200:
    # Parsea el contenido HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Aquí puedes extraer información específica
    # Por ejemplo, obtener el título de la página
    title = soup.title.string
    print('Título de la página:', title)
else:
    print('Error al realizar la solicitud:', response.status_code)