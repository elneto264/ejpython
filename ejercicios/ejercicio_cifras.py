num=int(input("dime un numero"))
if num<10:
    print("Tiene una cifra")
else:
    if num<100:
        print("Tiene dos cifra")
    else:
        if num<1000:
            print("Tiene tres cifra")
        else:
            print("Error con las cifras, muy grande tio")
