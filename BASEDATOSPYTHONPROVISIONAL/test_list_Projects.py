# Insertar filas en una tabla
import sqlite3
conexion = sqlite3.connect('db_proyecto.db')

cur = conexion.cursor()
# crear las tablas
cur.execute("""CREATE TABLE IF NOT EXISTS proyecto (
                            id integer primary key autoincrement,
                            nombre text,
                            fecha_comienzo text,	
                            fecha_fin text
                    )""")

cur.execute("""CREATE TABLE IF NOT EXISTS tarea (
                            id integer primary key autoincrement,
                            id_proyecto int,                            
                            nombre text,
                            prioridad text,
                            estado text,
                            fecha_comienzo text,	
                            fecha_fin text,
                            FOREIGN KEY (id_proyecto) REFERENCES proyecto (id)
                    )""")

cur.execute("""INSERT INTO proyecto
            (nombre, fecha_comienzo,fecha_fin) VALUES ("Edificio1", "04/04/2011", "04/06/2012");                              
                            """)
proy_edif1__id = 1
proy_canaliz = 2

cur.execute(' INSERT INTO tarea (id_proyecto,nombre, prioridad, estado, fecha_comienzo,fecha_fin) VALUES (?,?,?,?,?,?)', (proy_edif1__id, "Levantar cimientos",
            "Alta", "Concluida", "04/04/2011", "06/05/2011"))

cur.execute(' INSERT INTO tarea (id_proyecto,nombre, prioridad, estado, fecha_comienzo,fecha_fin) VALUES (?,?,?,?,?,?)', (proy_edif1__id, "Levantar paredes",
            "Media", "Concluida", "07/05/2011", "06/12/2011"))
cur.execute(' INSERT INTO tarea (id_proyecto,nombre, prioridad, estado, fecha_comienzo,fecha_fin) VALUES (?,?,?,?,?,?)', (proy_edif1__id, "Poner techo",
            "Alta", "Concluida", "07/12/2011", "04/06/2011"))

cur.execute(' INSERT INTO tarea (id_proyecto,nombre, prioridad, estado, fecha_comienzo,fecha_fin) VALUES (?,?,?,?,?,?)', (proy_canaliz, "Abrir zanja",
            "Alta", "Concluida", "01/10/2015", "01/12/2015"))

cur.execute(' INSERT INTO tarea (id_proyecto,nombre, prioridad, estado, fecha_comienzo,fecha_fin) VALUES (?,?,?,?,?,?)', (proy_canaliz, "Color conductos",
            "Alta", "Concluida", "01/13/2015", "02/01/2015"))
# except sqlite3.OperationalError:
#     print("Error")


def read_from_db():
    cur.execute('SELECT * FROM tarea')
    data = cur.fetchall()
    # print(data)
    for row in data:
        print(row)


read_from_db()

cur.execute(''' SELECT p.nombre, t.nombre FROM proyecto p, tarea t WHERE t.id_proyecto =p.id''')
data=cur.fetchall()
for row in data:
        print(row)

conexion.commit()
conexion.close()