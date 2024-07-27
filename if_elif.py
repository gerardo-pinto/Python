edad = int(input("Ingrese edad:"))
if edad <16 :
    print("no puedes conducir")
elif edad<18 :
    print("puede conducir con permiso de los padres")
elif edad<70 :
    print("puede conducir con licencia estandar")
else: 
    print("Requiere una licencia especial")