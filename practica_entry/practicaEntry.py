import tkinter
from tokenize import String

ventana=tkinter.Tk()

miFrame=tkinter.Frame(ventana,width=1200,height=600)
miFrame.pack()

minombre=tkinter.StringVar()

cuadroNombre=tkinter.Entry(miFrame,textvariable=minombre)
cuadroNombre.grid(row=0,column=1,padx=10,pady=10)
cuadroNombre.config(fg="blue", justify="center", font=("ariel",10))

cuadroApellido=tkinter.Entry(miFrame)
cuadroApellido.grid(row=1,column=1,padx=10,pady=10)

cuadroPassword=tkinter.Entry(miFrame)
cuadroPassword.grid(row=2,column=1,padx=10,pady=10)
cuadroPassword.config(show="*")

cuadroDireccion=tkinter.Entry(miFrame)
cuadroDireccion.grid(row=3,column=1,padx=10,pady=10)

cuadroComentario=tkinter.Text(miFrame,width=20,height=10)
cuadroComentario.grid(row=4,column=1,padx=10,pady=10)

scrollbar=tkinter.Scrollbar(miFrame,command=cuadroComentario.yview)
scrollbar.grid(row=4,column=2,sticky="nsew",padx=10,pady=10)

cuadroComentario.config(yscrollcommand=scrollbar.set)


nombreLabel=tkinter.Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)   ##sticky para saber en que parte esta el texto, se hace con los puntos cardinales

ApellidoLabel=tkinter.Label(miFrame, text="Apellido:")
ApellidoLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

PasswordLabel=tkinter.Label(miFrame, text="Password:")
PasswordLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

DireccionLabel=tkinter.Label(miFrame, text="Direccion:")
DireccionLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

ComentarioLabel=tkinter.Label(miFrame, text="Comentario:")
ComentarioLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

def codigoBoton():
    minombre.set("Sebastian")


BotonEnvio=tkinter.Button(ventana,text="Enviar",command=codigoBoton)
BotonEnvio.pack()

ventana.mainloop()