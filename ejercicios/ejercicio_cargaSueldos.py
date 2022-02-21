def l_sue():
    sue=[]
    for x in range(10):
        su=int(input("sueldo:"))
        sue.append(su)
    return sue


def imp_sue(sue):
    print("Listado ")
    for x in range(len(sue)):
        print(sue[x])


def sue_m(sue):
    cant=0
    for x in range(len(sue)):
        if sue[x]>4000:
            cant=cant+1
    print("empleados superior a 4000:",cant)    


def promedio(sue):
    suma=0
    for x in range(len(sue)):
        suma=suma+sue[x]
    promedio=suma//10
    return promedio

def sue_bajos(sue):
    pro=promedio(sue)
    print("promedio de la empresa:",pro)
    print("inferiores al promedio")
    for x in range(len(sue)):
        if sue[x]<pro:
            print(sue[x])




sue=l_sue()
imp_sue(sue)
sue_m(sue)
sue_bajos(sue)