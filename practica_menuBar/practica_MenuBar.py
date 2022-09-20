import tkinter

ventana= tkinter.Tk()
ventana.title("Practica MenuBar")
ventana.config(height=500,width=500)
barra_menu=tkinter.Menu()

menu_archivo=tkinter.Menu(barra_menu,tearoff=0)
menu_archivo.add_command(label="Nuevo")
menu_archivo.add_command(label="Guardar")
menu_archivo.add_command(label="Guardar como")
menu_archivo.add_separator()      
menu_archivo.add_command(label="Cerrar")
menu_archivo.add_command(label="Salir")

edicion_archivo=tkinter.Menu(barra_menu,tearoff=0)

herramienta_archivo=tkinter.Menu(barra_menu,tearoff=0)

ayuda_archivo=tkinter.Menu(barra_menu,tearoff=0)


barra_menu.add_cascade(label="Archivo",menu=menu_archivo)
barra_menu.add_cascade(label="Edicion",menu=edicion_archivo)
barra_menu.add_cascade(label="Herramientas",menu=herramienta_archivo)
barra_menu.add_cascade(label="Ayuda",menu=ayuda_archivo)
ventana.config(menu=barra_menu)
ventana.mainloop()

