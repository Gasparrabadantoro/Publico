import sqlite3
conexion=sqlite3.connect('db_proyecto.db')
cur=conexion.cursor()

# try 

cur.execute("""INSERT INTO proyecto
            (nombre, fecha_comienzo,fecha_fin) VALUES (?,?,?);
                             """,  ("Edificio1","04/04/2011","04/06/2012")) 

proy_edif1_id=cur.lastrowid

cur.execute(''' INSERT INTO tarea(id_proyecto,nombre,prioridad,estado,fecha_comienzo,fecha_fin)
 VALUES (?,?,?,?,?,?)''',(proy_edif1_id,"Levantar cimientos",
"Alta","Concluida","04/04/2011","06/05/2011"))

conexion.commit()
conexion.close()