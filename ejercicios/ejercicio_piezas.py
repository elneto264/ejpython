cantidad=0
x=1
n=int(input("cuantas piezas "))
while x<=n:
    largo=float(input("diga la medida:"))
    if largo>=1.2 and largo<=1.3:
        cantidad=cantidad+1
    x=x+1
print("la cantidad son")
print(cantidad)