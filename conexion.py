import mysql.connector

conexion = mysql.connector.connect(
    user="root", 
    password="", 
    host="localhost", 
    database="python", 
    port="3306"
) 
cursor=conexion.cursor()
#cursor.execute("show tables")
#for base in cursor:
#    print(base)
#conexion.close()

#sql="insert into clientes (nombre, direccion) values (%s,%s)"
datos=("pedro", "las ardillas 23, rengo")
cursor.execute(sql, datos)
datos=("miguel", "los mantos 31337")
cursor.execute(sql, datos)
datos=("alejandro", "Soy feliz 23, rancagua")
cursor.execute(sql, datos)
conexion.commit()
conexion.close() 