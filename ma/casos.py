def leer_productos():
    nombres = []
    precios = []

    while True:
        nombre = input("Ingrese el nombre del producto (FIN para terminar): ").upper()
        if nombre == "FIN":
            break
        elif nombre == "":
            print("No se ingresaron datos. Finalizando el programa.")
            return [], []

        precio = float(input("Ingrese el precio del producto: "))
        while precio <= 0:
            print("El precio no puede ser negativo o igual a cero.")
            precio = float(input("Ingrese el precio del producto: "))

        nombres.append(nombre)
        precios.append(precio)

    return nombres, precios

def mostrar_productos(nombres, precios):
    if not nombres:
        print("No hay productos para mostrar.")
    else:
        print("Lista de productos:")
        for i in range(len(nombres)):
            print(f"Producto: {nombres[i]}, Precio: {precios[i]}")
        print()



def producto_menor_precio(nombres, precios):
    indice = precios.index(min(precios))
    print(f"El producto con el precio más bajo es: {nombres[indice]}")

def promedio_precios_superiores_10000(precios):
    precios_superiores = [precio for precio in precios if precio > 10000]
    if len(precios_superiores) == 0:
        print("No hay productos con precios superiores a 10000.")
        return 0
    else:
        promedio = sum(precios_superiores) / len(precios_superiores)
        print(f"El promedio de los precios de los productos superiores a 10000 es: {promedio}")
        return promedio

def eliminar_precios_superiores_al_promedio(nombres, precios, promedio):
    nuevos_nombres = []
    nuevos_precios = []
    for nombre, precio in zip(nombres, precios):
        if precio <= promedio:
            nuevos_nombres.append(nombre)
            nuevos_precios.append(precio)
    return nuevos_nombres, nuevos_precios

def insertar_prueba_multiplo_de_tres(nombres, precios):
    nuevo_nombre = "PRUEBA"
    nuevo_precio = 999

    # Encontrar la posición del primer precio múltiplo de 3
    indice_insertar = next((i for i, precio in enumerate(precios) if precio % 3 == 0), None)

    if indice_insertar is not None:
        nombres.insert(indice_insertar + 1, nuevo_nombre)
        precios.insert(indice_insertar + 1, nuevo_precio)
    else:
        print("No se encontró ningún precio múltiplo de 3.")

    return nombres, precios

def ordenar_productos(nombres, precios, criterio):
    if criterio == "nombre":
        nombres.sort()
        precios = [precio for _, precio in sorted(zip(nombres, precios))]
    elif criterio == "precio":
        precios.sort()
        nombres = [nombre for _, nombre in sorted(zip(precios, nombres))]
    else:
        print("Criterio de ordenación no válido.")

    return nombres, precios

# Función principal
def main():
    nombres, precios = leer_productos()
    mostrar_productos(nombres, precios)

    producto_menor_precio(nombres, precios)

    promedio = promedio_precios_superiores_10000(precios)

    nombres, precios = eliminar_precios_superiores_al_promedio(nombres, precios, promedio)
    mostrar_productos(nombres, precios)

    nombres, precios = insertar_prueba_multiplo_de_tres(nombres, precios)
    mostrar_productos(nombres, precios)

    criterio = input("Ingrese el criterio de ordenación (nombre/precio): ").lower()
    nombres, precios = ordenar_productos(nombres, precios, criterio)
    mostrar_productos(nombres, precios)

if __name__ == "__main__":
    main()
