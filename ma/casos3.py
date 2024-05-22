def cargar_productos():
    modelos = []
    precios = []

    for _ in range(253):
        modelo = input("Ingrese el modelo de banqueta (BASTA para terminar): ").lower()
        if modelo == "basta" or modelo == "" or len(modelos) == 253:
            break

        precio = float(input("Ingrese el precio unitario: "))
        while precio <= 0:
            print("El precio no puede ser negativo o igual a cero.")
            precio = float(input("Ingrese el precio unitario: "))

        modelos.append(modelo)
        precios.append(precio)

    if not modelos:
        print("No se ingresaron datos. Finalizando el programa.")
        exit()

    return modelos, precios

def mostrar_modelos_y_precios(modelos, precios):
    print("Modelos y precios:")
    for i in range(len(modelos)):
        print(f"Modelo: {modelos[i]}, Precio: {precios[i]}")
    print()

def insertar_modelo_insertado(modelos, precios):
    medio = len(modelos) // 2
    modelos.insert(medio, "insertado")
    precios.insert(medio, 999)
def modelo_menor_precio2(modelos, precios):
    #menor_precio = float('inf')  # Inicializamos con un valor infinito para asegurarnos de que cualquier precio sea menor
    #indice_menor_precio = None
    menor_precio=precios[0]
    indice_menor_precio=0

    for i in range(len(precios)):
        if precios[i] < menor_precio:
            menor_precio = precios[i]
            indice_menor_precio = i

    if indice_menor_precio is not None:
        print(f"El modelo con el precio más bajo es: {modelos[indice_menor_precio]}")
    else:
        print("No hay modelos disponibles.")

def modelo_menor_precio(modelos, precios):
    indice_menor_precio = precios.index(min(precios))
    print(f"El modelo con el precio más bajo es: {modelos[indice_menor_precio]}")

def calcular_promedio(precios):
    promedio = sum(precios) / len(precios)
    print(f"El promedio de los precios es: {promedio}")
    return promedio

def eliminar_precios_superiores_al_promedio(modelos, precios, promedio):
    nuevos_modelos = []
    nuevos_precios = []
    for i in range(len(modelos)):
        if precios[i] <= promedio:
            nuevos_modelos.append(modelos[i])
            nuevos_precios.append(precios[i])
    return nuevos_modelos, nuevos_precios
def eliminar_precios_superiores_al_promedio2(modelos, precios, promedio):
    i = 0
    while i < len(precios):
        if precios[i] > promedio:
            modelos.pop(i)
            precios.pop(i)
        else:
            i += 1

    return modelos, precios

def insertar_triplo_despues_de_multiplos_de_tres(modelos, precios):
    for i in range(len(precios)):
        if precios[i] % 3 == 0:
            modelos.insert(i + 1, "agregado")
            precios.insert(i + 1, precios[i] * 3)

def ordenar_vectores(modelos, precios, criterio):
    if criterio == "precio":
        precios, modelos = zip(*sorted(zip(precios, modelos)))
    elif criterio == "modelo":
        modelos.sort()
        precios = [precio for _, precio in sorted(zip(modelos, precios))]
    else:
        print("Criterio de ordenación no válido.")

    return modelos, precios
def ordenamiento_burbuja(modelos, precios):
    n = len(precios)
    for i in range(n):
        for j in range(0, n-i-1):
            if precios[j] > precios[j+1]:
                # Intercambiar precios
                precios[j], precios[j+1] = precios[j+1], precios[j]
                # Intercambiar modelos
                modelos[j], modelos[j+1] = modelos[j+1], modelos[j]

# Ejemplo de uso
modelos = ["Modelo2", "Modelo4", "Modelo1", "Modelo3"]
precios = [15, 12, 10, 9]

orden = input("Ingrese el criterio de ordenación (precio/nombre): ").lower()

if orden == "precio":
    ordenamiento_burbuja(precios, modelos)
elif orden == "nombre":
    precios, modelos = zip(*sorted(zip(precios, modelos)))
else:
    print("Criterio de ordenación no válido.")

print("Modelos y precios ordenados:")
for modelo, precio in zip(modelos, precios):
    print(f"Modelo: {modelo}, Precio: {precio}")


def main():
    modelos, precios = cargar_productos()
    mostrar_modelos_y_precios(modelos, precios)

    insertar_modelo_insertado(modelos, precios)
    mostrar_modelos_y_precios(modelos, precios)

    #modelo_menor_precio(modelos, precios)
    modelo_menor_precio2(modelos, precios)

    promedio = calcular_promedio(precios)

    #modelos, precios = eliminar_precios_superiores_al_promedio(modelos, precios, promedio)
    #mostrar_modelos_y_precios(modelos, precios)

    #insertar_triplo_despues_de_multiplos_de_tres(modelos, precios)
    #mostrar_modelos_y_precios(modelos, precios)

    #criterio = input("Ingrese el criterio de ordenación (modelo/precio): ").lower()
    #modelos, precios = ordenar_vectores(modelos, precios, criterio)
    #mostrar_modelos_y_precios(modelos, precios)

if __name__ == "__main__":
    main()
