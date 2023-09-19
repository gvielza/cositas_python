import requests

# URL del archivo Python en GitHub
url = "https://raw.githubusercontent.com/gvielza/ej1-ob/master/main.py"

# Descargar el archivo
response = requests.get(url)
code = response.content.decode()

# Corregir el error en el código descargado
code = code.replace('false', 'False')

# Ejecutar el código corregido
exec(code)

