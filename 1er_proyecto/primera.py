import tkinter
from turtle import right

ventana=tkinter.Tk()

ventana.title("Ventana de pruebas")

##ventana.resizable(0,0)  no deja ajustar el tamaño 

##ventana.iconbitmap("cualquiercosa.ico")   asi se puede cambiar el icono de la aplicacion :d

ventana.geometry("500x300")

ventana.config(bg="black")

miframe=tkinter.Frame()

miframe.pack(fill="both",expand="true")

miframe.config(bg="white")

miframe.config(width="800",height="200")

miframe.config(bd=35)

miframe.config(relief="sunken")

miframe.config(cursor="pirate")

ventana=tkinter.mainloop()

##cambiar el .py por .pyw para que salga solo la ventana de la aplicacion