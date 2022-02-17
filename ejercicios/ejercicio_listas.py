
x=1
suma1=0
suma2=0
print("lista 1")
while x<=15:
    valor=int(input("valor 1: "))
    suma1=suma1+valor
    x=x+1
print("lista 2")
x = 1
while x<=15:
    valor=int(input("valor 2: "))
    suma2=suma2+valor
    x=x+1
if suma1>suma2:
    print("Lista 1 es mayor")
else:
    if suma2>suma1:
        print("Lista 1 es mayor")
    else:
        print("Listas iguales")