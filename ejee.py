def diferentes_caracteres(palabra1, palabra2):
    if len(palabra1) != len(palabra2):
        return "las palabras no tienen la misma cantidad de caracteres"

    result = []

    for i in range(len(palabra1)):
        if palabra1[i] != palabra2[i]:
            result.append(palabra1[i])
    return result


palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

print(diferentes_caracteres(palabra1, palabra2))
