entrada=input("escribe algo entre 10 y 20 letras o lo que sea: ")
if len(entrada)>=10 and len(entrada)<=20:
    print("correcto, escribiste:  " , entrada)
else:
    print(" incorrecto, escribiste:  " , entrada)