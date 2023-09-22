# App para recoger h trabajadas
#importar libreria sqlite3.
from datetime import datetime
from os.path import isfile
import sqlite3
import os
#conectar a la base de datos si no existe la creacion
coneccion=sqlite3.connect("bd/base_datos.db")
#ruta de mi base de datos
ruta = "bd/base_datos.db"
#cursor para manipular mi base de datos
cursor=coneccion.cursor()
def existe_archivo(ruta):
  if os.path.isfile(ruta):
    print("existe el archivo")
  else:
    print("no existe el archivo")

#existe_archivo(ruta)

#Funcion para crear la tabla
def crear_tabla():
  # Crear la tabla clases
  cursor.execute('''
      CREATE TABLE clases (
          nombre TEXT,
          hora_inicio TEXT,
          hora_fin TEXT,
          alumno TEXT
      )
  ''')
#crear_tabla()
#funcion para elimnar la tabla
def eliminar_tabla(Tabla):
  cursor.execute(f'DROP TABLE {Tabla}')
#eliminar_tabla("clasesEJ")
nombre="PHP"
alumno="Damian"

hora_inicio=str(datetime.now())
hora_fin=str(datetime.now())

cursor.execute(f'INSERT INTO clases(nombre, hora_inicio, hora_fin, alumno) VALUES(?, ?, ?, ?)', (nombre, hora_inicio, hora_fin, alumno))

coneccion.commit()


coneccion.close()