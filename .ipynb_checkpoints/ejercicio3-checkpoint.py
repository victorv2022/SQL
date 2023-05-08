import sqlite3

conexion=sqlite3.connect("bd1.db")
try:
    conexion.execute(""create table articulos (
                            codigo integer primary key autoincrment,
                            descripcion text,
                            precio real
                        )""")
    print("se creo la tabla articulos")
except sqlite3.OperationalError:
    print("La tabla articulos ya existe")
conexion.close