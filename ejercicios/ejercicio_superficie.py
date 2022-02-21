def ret_sup(l1,l2):
    supe=l1*l2
    return supe


# bloque principal

print("1er rectangulo------------")
l1=int(input("lado menor del rectangulo: "))
l2=int(input("lado mayor del rectangulo: "))
print("2do rectangulo------------")
l3=int(input("lado menor del rectangulo:"))
l4=int(input("lado mayor del rectangulo:"))
if ret_sup(l1,l2)==ret_sup(l3,l4):
    print("tienen la misma superficie")
else:
    if ret_sup(l1,l2)>ret_sup(l3,l4):
        print("1er rectangulo tiene una superficie mayor")
    else:
        print("2ndo rectangulo tiene una superficie mayor")