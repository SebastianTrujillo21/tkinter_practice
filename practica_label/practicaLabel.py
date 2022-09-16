import tkinter

ventana=tkinter.Tk()

miFrame=tkinter.Frame(ventana,width=500,height=500)

miFrame.pack()

miImagen=tkinter.PhotoImage(file="imagen.png")       ##con el formato .jpg no funciona

label=tkinter.Label(miFrame,image=miImagen)

label.pack()


ventana.mainloop()