from tkinter import *

root=Tk()
root.title("Ventana Principal")
root.geometry("300x300")

def envia_boton():
    ventana_nueva=Toplevel()
    ventana_nueva.title("Ventana Secundaria")
    ventana_nueva.geometry("300x300")
    valor_entrada=entrada.get()
    etiqueta=Label(ventana_nueva,text=" "+ valor_entrada)
    etiqueta.grid(row=0,column=0)
    ventana_nueva.mainloop()

entrada=Entry(root,width=20)
entrada.grid(row=0,column=0)

envia=Button(root,text="Enviar",command=envia_boton)
envia.grid(row=1,column=0)

root.mainloop()