nomb=[]
notas=[]
for x in range(4):
    nom=input("nombre: ")
    nomb.append(nom)
    no=int(input("nota: "))
    notas.append(no)

cantidad=0
for x in range(4):
    print(nomb[x])
    print(notas[x])
    if notas[x]>=8:
        print("vale")
        cantidad=cantidad+1
    else:
        if notas[x]>=4:
            print("bueno...")
        else:
            print("vete a dormir")

print("los que medio controlan son", cantidad)
