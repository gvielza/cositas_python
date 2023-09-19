
def obtener_palabras(cadena):
    with open(cadena+'.txt', 'r') as f:
        contenido = f.read()
        contenido = contenido.replace(',', ' ')
        palabras = contenido.split()
        return palabras

print(obtener_palabras("elementos_a_insertar"))
print(obtener_palabras("elementos_del_insert"))

def elementos_iguales(a,b):
    contador=0;
    list1=obtener_palabras(a)
    list2=obtener_palabras(b)
    while(contador<=len(list1)):
        if(a[contador]==b[contador]):
            return True
        else:
            return False
        contador+=1


print(elementos_iguales(obtener_palabras("elementos_a_insertar"),obtener_palabras("elementos_del_insert")))
