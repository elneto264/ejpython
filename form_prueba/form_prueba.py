#----------------Conexion BBDD----------------------------------
import sqlite3

print("se conecto a la bbdd clientes")
#-------------Ventana--------------
from tkinter import *
campo=Tk()
campo.geometry("650x350")
campo.config(bg="turquoise")
campo.title("Clientes")
mframe=Frame()
mframe.pack()
mframe.place(y=75,x=200)
mframe.config(width="150",height="100")
mframe.config(bg="turquoise")

Ennombre=StringVar()
Enapellido=StringVar()
Entelefono=StringVar()

Label(mframe, text="Gestión Clientes", bg="turquoise", fg="white", font=("Times",18,"bold")).grid(row=0, column=1, columnspan=3)
Label(mframe, text="Nombre:", bg="turquoise", fg="white", font=("Times",12,"bold")).grid(row=1, column=1, sticky="e")
Label(mframe, text="Apellido:", bg="turquoise", fg="white", font=("Times",12,"bold")).grid(row=2, column=1, sticky="e")
Label(mframe, text="Telefono:", bg="turquoise", fg="white", font=("Times",12,"bold")).grid(row=3, column=1, sticky="e")
Entry_nombre=Entry(mframe, fg="black", textvariable=Ennombre).grid(row=1, column=3, padx=10, pady=10)
Entry_apellido= Entry(mframe, fg="black", textvariable=Enapellido).grid(row=2, column=3, padx=10, pady=10)
Entry_telefono= Entry(mframe, fg="black", textvariable=Entelefono).grid(row=3, column=3, padx=10, pady=10)


#----------Funcion Tabla----------------

"""miconexion=sqlite3.connect("clientes.db")
miCursor=miconexion.cursor()
miCursor.execute('''
    CREATE TABLE clientes(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE VARCHAR(50),
    APELLIDO VARCHAR(50),
    TELEFONO VARCHAR(50))
    ''')
miconexion.commit()"""

#----------funcion limpiar--------------

def limpiarEntry():
    Ennombre.set("")
    Enapellido.set("")
    Entelefono.set("")
    Mensaje.config(text="Formulario Limpiado exitosamente")
#---------enviar---------------
def enviar():
    nombre = Ennombre.get()
    apellido = Enapellido.get()
    telefono = Entelefono.get()
    datos = nombre, apellido, telefono
    miconexion=sqlite3.connect("clientes.db")
    miCursor=miconexion.cursor()
    miCursor.execute("INSERT INTO clientes VALUES(NULL, '" + nombre +
        "','" + apellido +
        "','" + telefono + "')")

    #miCursor.execute("INSERT INTO clientes VALUES (NULL,?,?,?)", (datos))
    miconexion.commit()
    Mensaje.config(text="Registro Insertado exitosamente")
#-----------boton-------------------
botonenviar=Button(mframe,text="Enviar",width="14",command=enviar, padx=10, pady=10)
botonenviar.grid(row=5,column=1)
botonreset=Button(mframe,text="Limpiar",width="14", command=limpiarEntry, padx=10, pady=10)
botonreset.grid(row=5,column=3)
Mensaje=Label(mframe, fg="green", bg="turquoise", font=("Times",12,"bold"))
Mensaje.grid(row=6, column=1, columnspan=3, padx=10, pady=10)


campo.mainloop()