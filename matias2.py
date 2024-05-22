import csv

def obtener_email_por_nombre(ruta_archivo_csv, nombre):
    try:
        with open(ruta_archivo_csv, mode='r') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)
            for linea in lector_csv:
                if linea['nombre'] == nombre:
                    email = linea.get('email', None)
                    if email and '@' in email:  # Verificar si hay correo y si el carácter '@' está presente
                        return email
                    else:
                        print("El correo electrónico no es válido o no está presente.")
                        return None
            print("El nombre no fue encontrado en el archivo CSV.")
            return None
    except FileNotFoundError:
        print("El archivo CSV no fue encontrado.")
        return None
    except Exception as e:
        print(f"Error al procesar el archivo CSV: {e}")
        return None

# Ejemplo de uso
ruta = 'datos.csv'
nombre_buscar = 'geo'
email_obtenido = obtener_email_por_nombre(ruta, nombre_buscar)
if email_obtenido:
    print(f"Correo electrónico de {nombre_buscar}: {email_obtenido}")
