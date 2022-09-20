import imp
import tkinter
from tkinter import messagebox


ventana= tkinter.Tk()

def abrirVentana():
    ventana.withdraw()
    win=tkinter.Toplevel()
    win.title("Ventana nueva")
    win.geometry("300x300")
    boton1=tkinter.Button(win,text="HOLA")
    boton1.pack()


def infoAdicional():
    messagebox.showinfo("Procesador de Juan", "Procesador de texto version 2019")

def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")
ventana.title("Practica MenuBar")

def salirAplicacion():
    valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
    if valor=="yes":
        ventana.destroy()


ventana.config(height=500,width=500)
barra_menu=tkinter.Menu()

menu_archivo=tkinter.Menu(barra_menu,tearoff=0)
menu_archivo.add_command(label="Nuevo")
menu_archivo.add_command(label="Guardar")
menu_archivo.add_command(label="Guardar como")
menu_archivo.add_separator()      
menu_archivo.add_command(label="Cerrar")
menu_archivo.add_command(label="Salir",command=salirAplicacion)

edicion_archivo=tkinter.Menu(barra_menu,tearoff=0)
edicion_archivo.add_command(label="Copiar")
edicion_archivo.add_command(label="Cortar")
edicion_archivo.add_command(label="Pegar")

herramienta_archivo=tkinter.Menu(barra_menu,tearoff=0)

ayuda_archivo=tkinter.Menu(barra_menu,tearoff=0)
ayuda_archivo.add_command(label="Licencia",command=avisoLicencia) 
ayuda_archivo.add_command(label="Acerca de...",command=infoAdicional)
ayuda_archivo.add_command(label="Ayuda")

barra_menu.add_cascade(label="Archivo",menu=menu_archivo)
barra_menu.add_cascade(label="Edicion",menu=edicion_archivo)
barra_menu.add_cascade(label="Herramientas",menu=herramienta_archivo)
barra_menu.add_cascade(label="Ayuda",menu=ayuda_archivo)
ventana.config(menu=barra_menu)

boton2=tkinter.Button(ventana,text="Abrir ventana",command=abrirVentana)
boton2.pack()



ventana.mainloop()

