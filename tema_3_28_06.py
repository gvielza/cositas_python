# Escribir una funcion que recibe una tabla de un campeonato
# de futbol representada como listas de tuplas estructuradas de
# la sig. forma (club, puntos, pg, pe, pp, gf, ge, dif, promedio) y
# devuelva la lista recibida ordenada de mayor a menor segun los 
# promedios de cada equipo.
def ordenar_por_promedio(tabla):
    n = len(tabla)
    for i in range(n):
        for j in range(0, n-i-1):
            if tabla[j][8] < tabla[j+1][8]:
                tabla[j], tabla[j+1] = tabla[j+1], tabla[j]
    return tabla

# Ejemplo de uso:
tabla = [
    ('Equipo A', 20, 6, 2, 2, 18, 10, 8, 2.0),
    ('Equipo B', 18, 5, 3, 2, 15, 9, 6, 1.8),
    ('Equipo C', 15, 4, 3, 3, 12, 11, 1, 1.5),
    ('Equipo D', 12, 3, 3, 4, 10, 12, -2, 1.2),
    ('Equipo E', 10, 2, 4, 4, 8, 10, -2, 1.0)
]

tabla_ordenada = ordenar_por_promedio(tabla)
for equipo in tabla_ordenada:
    print(equipo)


def ordenar_por_promedios(promedios):
    pass

# Escribir una funcion que recibe una tabla de promedios de un 
# campeonato de futbol representada como listas de tuplas, las cuales 
# estan estructuradas de la sig. forma (club, puntos, pg, pe, pp, gf, 
# ge, dif, promedio) y devuelve la tupla del equipo que desciende cual 
# es el del menor promedio. Si hubiera equipos con el mismo promedio
# se coincidera como menor al que tenga menos puntos. 
# Conciderar que los datos de los equipos no estan ordenados.
def equipo_que_desciende(tabla):
    menor_promedio = float('inf')
    equipo_desciende = None
    puntos_equipo_desciende = float('inf')

    for equipo in tabla:
        nombre_equipo, puntos, _, _, _, _, _, _, promedio = equipo

        if promedio < menor_promedio or (promedio == menor_promedio and puntos < puntos_equipo_desciende):
            menor_promedio = promedio
            equipo_desciende = equipo
            puntos_equipo_desciende = puntos

    return equipo_desciende

equipo_desciende = equipo_que_desciende(tabla)
print("Equipo que desciende:", equipo_desciende[0])


def obtener_equipo_que_desciende(promedios):
    pass


# Utilizando las funciones del ejercicio anterior, escribir un programa
# que le permita al usuario ingresar el nombre del club, puntos, pg, pe, 
# pp, gf, ge, dif y promedio de 20 clubes. Informe cual es el equipo
# cuales son los 3 equipos de que descienden por quedar ultimos 
# en la tabla de promedios y muestra la info de los equipos de la sig.
# forma "club|promedio".
def ingresar_datos_clubes(tabla):
    for _ in range(5):
        nombre = input("Ingrese el nombre del club: ")
        puntos = int(input("Ingrese los puntos del club: "))
        pg = int(input("Ingrese los partidos ganados: "))
        pe = int(input("Ingrese los partidos empatados: "))
        pp = int(input("Ingrese los partidos perdidos: "))
        gf = int(input("Ingrese los goles a favor: "))
        ge = int(input("Ingrese los goles en contra: "))
        dif = gf - ge
        promedio = (puntos / 5) / 3
        tabla.append((nombre, puntos, pg, pe, pp, gf, ge, dif, promedio))

# Ingresar datos de los clubes
tabla = []
ingresar_datos_clubes(tabla)

# Determinar los equipos que descienden
equipos_descienden = []
for _ in range(3):
    equipo_desciende = equipo_que_desciende(tabla)
    equipos_descienden.append(equipo_desciende)
    tabla.remove(equipo_desciende)

# Mostrar la información de los equipos que descienden
print("Los 3 equipos que descienden son:")
for equipo in equipos_descienden:
    print(f"{equipo[0]} | Promedio: {equipo[8]}")

def obtener_equipos(tabla):
    equipos = [equipo[0] for equipo in tabla]
    return equipos
print("\nEquipos en la tabla:")
for equipo in obtener_equipos(tabla):
    print(equipo)


def main():
    pass

main()