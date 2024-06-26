
import csv

def escribir_csv(lista_tuplas, nombre_archivo):
    try:
        with open(nombre_archivo, mode='w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(['nombre', 'celular','email'])  # Escribir encabezados
            for tupla in lista_tuplas:
                escritor_csv.writerow(tupla)
        print(f"Se ha escrito el archivo CSV '{nombre_archivo}' correctamente.")
    except Exception as e:
        print(f"Error al escribir el archivo CSV: {e}")

def obtener_datos_usuario():
    nombre = input("Ingrese el nombre: ")
    celular = input("Ingrese el número de celular: ")
    email= input("Ingrese el correo: ")
    return nombre, celular,email

# Obtener datos del usuario
nombre, celular,email = obtener_datos_usuario()

# Escribir datos en un archivo CSV
datos_usuario = [(nombre, celular,email)]
nombre_archivo = 'datos.csv'
escribir_csv(datos_usuario, nombre_archivo)


