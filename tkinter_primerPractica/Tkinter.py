##NO SE PUEDE LLAMAR UN PROYECTO tkinter con minuscula 

from itertools import tee
from pickle import TRUE
from struct import pack
import tkinter
from tkinter.tix import TEXT
from turtle import right
from typing import TextIO

ventana=tkinter.Tk()   ##creacion de la ventana
ventana.geometry("600x600")  ##cambiar tamaño de la ventana

"""" 
##LABEL
etiqueta=tkinter.Label(ventana,text="Hola mundo",bg="red")
etiqueta.pack()  ##hace que se muestre la etiqueta


etiqueta2=tkinter.Label(ventana)
etiqueta2.pack()


##BUTTON
def saludo(name):
    print(f"Saludos {name}")

boton1=tkinter.Button(ventana,text="Dale Click",padx=20,pady=10,command= lambda: saludo("desconocido"))
boton1.pack()

##TEXT BOX

def recibirtexto():
   texto=textbox.get()
   etiqueta2["text"]=texto
   print(texto)

textbox=tkinter.Entry(ventana,font="Helvetica 10")
textbox.pack()

button2=tkinter.Button(ventana,text="Presiona Aqui",command=recibirtexto)
button2.pack()

"""

######################################################
##APLICANDO METODO GRID##

boton2=tkinter.Button(ventana,text="bonton 2")
boton3=tkinter.Button(ventana,text="bonton 3")
boton4=tkinter.Button(ventana,text="bonton 4")
boton5=tkinter.Button(ventana,text="bonton 5")

boton2.grid(row=0,column=0)
boton3.grid(row=0,column=1)
boton4.grid(row=0,column=2)
boton5.grid(row=1,column=1)

ventana.mainloop()