import sqlite3
conexion=sqlite3.connect('db_proyecto.db')
cur=conexion.cursor()

cur.execute("""INSERT INTO escuela
            (nombre, direccion,municipio,id_escuela) VALUES ();
                             """)

escuela_id=cur.lastrowid

cur.execute(''' INSERT INTO profesor(DNI_alumno,fecha_nacimiento,departamento,experiencia)
 VALUES (?,?,?,?)''',(escuela_id,"Levantar cimientos",
"Alta","Concluida","04/04/2011","06/05/2011"))  

conexion.comit()
conexion.close()