import os
import tkinter as tk

def buscar_palabra_en_archivos(directorio, palabra):
    resultados = []
    for raiz, directorios, archivos in os.walk(directorio):
        for archivo in archivos:
            ruta_completa = os.path.join(raiz, archivo)
            if os.path.isfile(ruta_completa):
                try:
                    with open(ruta_completa, 'r', encoding='utf-8') as f:
                        contenido = f.read()
                        if palabra in contenido:
                            resultados.append(ruta_completa)
                except Exception as e:
                    print(f"No se pudo leer el archivo {ruta_completa}: {e}")
    return resultados

def buscar_archivos_por_extension(directorio, extension):
    resultados = []
    for raiz, directorios, archivos in os.walk(directorio):
        for archivo in archivos:
            if archivo.endswith(extension):
                resultados.append(os.path.join(raiz, archivo))
    return resultados

# Ejemplo de uso
if __name__ == "__main__":
    directorio = input("Introduce el directorio a buscar: ")
    palabra = input("Introduce la palabra a buscar en los archivos: ")
    print("Buscando archivos que contienen la palabra '{}' en el directorio '{}'...".format(palabra, directorio))
    resultados_palabra = buscar_palabra_en_archivos(directorio, palabra)
    if resultados_palabra:
        print("Archivos encontrados:")
        for resultado in resultados_palabra:
            print(resultado)
    else:
        print("No se encontraron archivos que contengan la palabra '{}'.".format(palabra))

    extension = input("Introduce la extensión de archivo a buscar (por ejemplo, '.txt'): ")
    print("Buscando archivos con la extensión '{}' en el directorio '{}'...".format(extension, directorio))
    resultados_extension = buscar_archivos_por_extension(directorio, extension)
    if resultados_extension:
        print("Archivos encontrados:")
        for resultado in resultados_extension:
            print(resultado)
    else:
        print("No se encontraron archivos con la extensión '{}'.".format(extension))
