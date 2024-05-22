from excepciones import MisExcepcionesGroup1, MisExcepcionesGroup2, MisExcepcionesGroup3
try:
    #numero1=5
    #numero2="geo"
    numeros=[0,2,3,4]
    result=(numeros[3]/numeros[1])

except Exception as error:
    print("Lo sentimos, no se pudo realizar la operacion, estamos usando la clase padre, independientemente del error")
    print(error)
except ZeroDivisionError  as error:
    print("No se puede dividir por cero")
    print(error)
except NameError as error:
    print("Variable no definida")
    print(error)
except TypeError as error:
    print("Tipo de dato incorrecto")
    print(error)
except IndexError as error:
    print("Indice fuera de rango")
    print(error)
else:
    print("El resultado de la division es:",result)
finally:
    print("Programa finalizado")

print("*********Excepciones en grupo personalizadas*********")
try:
    raise ExceptionGroup('Un grupo de excepciones.',
                         [MisExcepcionesGroup1(), MisExcepcionesGroup2(), MisExcepcionesGroup3()]
                         )
except *MisExcepcionesGroup1:
    print("Se produjo un error de tipo MisExcepcionesGroup1")
except *MisExcepcionesGroup2:
    print("Se produjo un error de tipo MisExcepcionesGroup2")
except *MisExcepcionesGroup3:
    print("Se produjo un error de tipo MisExcepcionesGroup3")

