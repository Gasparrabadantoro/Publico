import sqlite3
# crear una base de datos en un archivo e insertar una tabla 
conexion=sqlite3.connect('db_proyecto.db')
# el objeto cursor permite a través del método execute ejecutar sentencias SQL 
cur=conexion.cursor()

#Crear las tablas

cur.execute(""" CREATE TABLE IF NOT EXISTS proyecto(
    id integer primary key autoincrement,
    nombre text,
    fecha_comienzo text,
    fecha_fin text
    )""")
    
cur.execute("""CREATE TABLE IF NOT EXISTS tarea(
    id integer primary key autoincrement,
    id_proyecto int,
    nombre text,
    prioridad text,
    estado text,
    fecha_comienzo text,
    fecha_fin text,
    FOREIGN KEY (id_proyecto) REFERENCES proyecto (id)
    )""")
conexion.commit()
conexion.close()