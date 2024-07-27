#suma=0
#for f in range(5):
#    valor=int(input("Ingrese valor:"))
#    suma=suma+valor
#print("La suma es")
#print(suma)
#promedio=suma/5
#print("El promedio es:")
#print(promedio)

mul3=0
mul5=0
for f in range(10):
    valor=int(input("Ingrese un valor:"))
    if valor%3==0:
        mul3=mul3+1
    if valor%5==0:
        mul5=mul5+1
print("Cantidad de valores ingresados múltiplos de 3")
print(mul3)
print("Cantidad de valores ingresados múltiplos de 5")
print(mul5)