import tkinter

ventana= tkinter.Tk()
ventana.title("Practica CheckButton")

playa=tkinter.IntVar()
montaña=tkinter.IntVar()
turismoRural=tkinter.IntVar()

def opcionesViaje():
    opcionEscogida=""
    if playa.get()==1:
        opcionEscogida+=" playa"
    if montaña.get()==1:
        opcionEscogida+=" montaña"
    if turismoRural.get()==1:
        opcionEscogida+=" turismoRural"

    textoFinal.config(text=opcionEscogida)


avion=tkinter.PhotoImage(file="avion.png")
avionLabel=tkinter.Label(ventana, image=avion)
avionLabel.pack()

frame= tkinter.Frame(ventana)
frame.pack()

Label2=tkinter.Label(frame, text="Elige Destino:",width=100)
Label2.pack()

chechButton1=tkinter.Checkbutton(frame,text="Playa",variable=playa,onvalue=1,offvalue=0,command=opcionesViaje)
chechButton1.pack()

chechButton2=tkinter.Checkbutton(frame,text="Montaña",variable=montaña,onvalue=1,offvalue=0,command=opcionesViaje)
chechButton2.pack()

chechButton3=tkinter.Checkbutton(frame,text="Turismo Rural",variable=turismoRural,onvalue=1,offvalue=0,command=opcionesViaje)
chechButton3.pack()

textoFinal=tkinter.Label(frame)
textoFinal.pack()

ventana.mainloop()