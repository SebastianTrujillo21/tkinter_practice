import tkinter

ventana=tkinter.Tk()    
frame =tkinter.Frame(ventana)
frame.pack()

varOpciones=tkinter.IntVar()

def imprimir():
    if varOpciones.get()==1:
        etiqueta2.config(text="Has elegido masculino")
    elif varOpciones.get()==2:
        etiqueta2.config(text="Has elegido femenino")
    else:
        etiqueta2.config(text="Has elegido otro")

etiqueta=tkinter.Label(frame,text="Genero:")
etiqueta.pack()

radioButton1=tkinter.Radiobutton(frame,text="Masculino",variable=varOpciones,value=1,command=imprimir)
radioButton1.pack()

radioButton2=tkinter.Radiobutton(frame,text="Femenino",variable=varOpciones,value=2,command=imprimir)
radioButton2.pack()


radioButton3=tkinter.Radiobutton(frame,text="Otras Opciones",variable=varOpciones,value=3,command=imprimir)
radioButton3.pack()

etiqueta2=tkinter.Label(frame)
etiqueta2.pack()

ventana.mainloop()
