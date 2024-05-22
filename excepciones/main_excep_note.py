from excepciones import MisExcepcionesGroup1, MisExcepcionesGroup2, MisExcepcionesGroup3
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
