emp=[]
suel=[]
cant=int(input(" emp de empresa:"))
for x in range(cant):
    nom=input(" nombre:")
    emp.append(nom)
    su=int(input("importe del sueldo:"))
    suel.append(su)

print("Listado completo de emp")
for x in range(len(suel)):
    print(emp[x],suel[x])

pos=0
while pos<len(suel):
    if suel[pos]>10000:
        suel.pop(pos)
        emp.pop(pos)
    else:
        pos=pos+1

print("empleados que cobran 10000 o menos")
for x in range(len(suel)):
    print(emp[x],suel[x])