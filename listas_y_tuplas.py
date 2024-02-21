"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física,
 Química, Historia y Lengua) en una lista y la muestre por pantalla."""
# Almacenar las asignaturas del curso en una lista
asignaturas = []

def ingresar_asignatura():
    try:
        while True:
            # Ingresar una asignatura por teclado
            asignatura = input("Ingresa una asignatura o '0' para terminar: ")
            if asignatura == '0':
                break
            if not asignatura.isalpha():
                raise ValueError

            # Agregar la asignatura a la lista
            asignaturas.append(asignatura)
            print(asignaturas)
    except ValueError:
        print("Ingresa solo letras")


ingresar_asignatura()
# Mostrar las asignaturas por pantalla
for asignatura in asignaturas:
    print(asignatura)

"""2-Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>,
 donde <asignatura> es cada una de las asignaturas de la lista."""
def mostrar_asignatura():
    cadena="Yo estudio "
    for asignatura in asignaturas:
        cadena=cadena+asignatura+", "

    print(cadena[:-2]+".")
mostrar_asignatura()
"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química,
 Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después 
 las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una 
 des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario."""

notas=[]
asignaturas_notas = []

def ingresar_notas():
    for asignatura in asignaturas:
        nota = input("En "+asignatura+" has sacado: ")
        notas.append(nota)
ingresar_notas()

def mostrar_notas_asignaturas():
    for asignatura in asignaturas:
        print("En "+asignatura+" has sacado "+notas[asignaturas.index(asignatura)])

#mostrar_notas_asignaturas()

def mostrar_notas_x_asignatura():
    cadena=""

    for asignatura in asignaturas:
        cadena+="En "+asignatura+" has sacado "+notas[asignaturas.index(asignatura)]+". "

    print(cadena)

mostrar_notas_x_asignatura()

#Tuplas
tupla = (1, 2, 3)
print(tupla) #(1, 2, 3) Son inmutables, lo que significa que no pueden ser modificadas una vez declaradas,
# y en vez de inicializarse con corchetes se hace con (). Dependiendo de lo que queramos hacer, las tuplas pueden ser más rápidas.
tupla = 1, 2, 3
print(type(tupla)) #<class 'tuple'>
print(tupla)       #(1, 2, 3)

tupla = 1, 2, ('a', 'b'), 3
print(tupla)       #(1, 2, ('a', 'b'), 3) anidada
print(tupla[2][0]) #a

lista = [1, 2, 3]
tupla = tuple(lista)
print(type(tupla)) #<class 'tuple'>
print(tupla)       #(1, 2, 3)

tupla = [1, 2, 3]
for t in tupla:
    print(t) #1, 2, 3
#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos tuplas y muestre por pantalla su producto escalar.
a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
for i in range(len(a)):
    product += a[i]*b[i]
print("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str(product)) 




