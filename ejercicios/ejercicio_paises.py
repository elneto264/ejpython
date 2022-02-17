
paises=[]
temp=[]
prom=[]

for x in range(4):
    nom=input("Ingrese el nombre del pais:")
    paises.append(nom)
    temp1=int(input("primera temperatura:"))
    temp2=int(input(" segunda temperatura:"))
    temp3=int(input(" tercer temperatura:"))
    temp.append([temp1, temp2, temp3])

print("Paises y temperaturas medias ")
for x in range(4):
    print(paises[x],temp[x][0],temp[x][1],temp[x][2])

for x in range(4):
    pro=(temp[x][0]+temp[x][1]+temp[x][2])//3
    prom.append(pro)

print("medias trimestrales")
for x in range(4):
    print(paises[x],prom[x])
           
posmayor=0
for x in range(1,4):
    if prom[x]>prom[posmayor]:
        posmayor=x
print(" media trimestral mayor:", paises[posmayor])
