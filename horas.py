# App para recoger h trabajadas
#importar libreria sqlite3.
from os.path import isfile
import sqlite3
import os
#conectar a la base de datos si no existe la creacion
sqlite3.connect("bd/base_datos.db")
ruta = "bd/base_datos.db"


def existe_archivo(ruta):
  if os.path.isfile(ruta):
    print("existe el archivo")
  else:
    print("no existe el archivo")


#existe_archivo(ruta)
