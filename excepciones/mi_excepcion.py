class ExceptionName(Exception):
    def __init__(self, ):
        super().__init__("Mi Excepcion de nombre")

    def validar_si_notas(self):
        try:
            return len(self.__notes__) > 0
        except:
            return False



    def mostrar_notas(self):
        try:
            for note in self.__notes__:
                if note!= None:
                    print("Nota:", note)
        except:
            print("No hay notas")


def validar_nombre(nombre):
    username_error= ExceptionName()
    if len(nombre) <= 5:
        username_error.add_note("El nombre debe ser mayor o igual a 3")
    if not nombre.isalpha():
        username_error.add_note("El nombre solo puede contener letras")
    if " " in nombre:
        username_error.add_note("El nombre no puede contener espacios")
    if username_error.validar_si_notas():
        raise username_error

    return True

try:
    nombre = "arsaab"
    validar_nombre(nombre)
except ExceptionName as e:
    print(e.mostrar_notas())
else:
    print("Validacion exitosa")







