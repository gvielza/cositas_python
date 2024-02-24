import csv


def obtener_mailxnombre(ruta_archivo_csv, nombre):
    try:
        with open(ruta_archivo_csv, mode="r") as archivo_csv:
            lecotr_csv = csv.DictReader(archivo_csv)
            for linea in lecotr_csv:
                if linea["nombre"] == nombre:
                    email = linea["email"]
                    if "@" in email:
                        return email
                    else:
                        print("El correo no es valido:")
                        return None
            print("No se encontro el nombre ")
            return None
    except FileNotFoundError as e:
        print("El archivo no fue encontrado")
    except Exception as e:
        print("Error al  procesar el csv")


ruta_archivo_csv = "mis_datos.csv"
nombre = "juan"

obtener_mailxnombre(ruta_archivo_csv, nombre)