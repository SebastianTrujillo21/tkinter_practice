import tkinter
from turtle import right

ventana=tkinter.Tk()

miFrame=tkinter.Frame(ventana)
miFrame.pack()

#------------------------pantalla--------------------------------

numeroPantalla=tkinter.StringVar()

pantalla=tkinter.Entry(miFrame,textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
pantalla.config(bg="black",fg="white",justify="right")

#------------------------FuncionPantalla-------------------------

def numeroPulsado(num):
    numeroPantalla.set(numeroPantalla.get()+num)

#------------------------fila1--------------------------------

btn7=tkinter.Button(miFrame,text="7",width=3,command=lambda:numeroPulsado("7"))
btn7.grid(row=2,column=1)

btn8=tkinter.Button(miFrame,text="8",width=3,command=lambda:numeroPulsado("8"))
btn8.grid(row=2,column=2)

btn9=tkinter.Button(miFrame,text="9",width=3,command=lambda:numeroPulsado("9"))
btn9.grid(row=2,column=3)

btnDiv=tkinter.Button(miFrame,text="/",width=3)
btnDiv.grid(row=2,column=4)

#------------------------fila2--------------------------------

btn4=tkinter.Button(miFrame,text="4",width=3,command=lambda:numeroPulsado("4"))
btn4.grid(row=3,column=1)

btn5=tkinter.Button(miFrame,text="5",width=3,command=lambda:numeroPulsado("5"))
btn5.grid(row=3,column=2)

btn6=tkinter.Button(miFrame,text="6",width=3,command=lambda:numeroPulsado("6"))
btn6.grid(row=3,column=3)

btnMult=tkinter.Button(miFrame,text="x",width=3)
btnMult.grid(row=3,column=4)

#------------------------fila3--------------------------------

btn3=tkinter.Button(miFrame,text="3",width=3,command=lambda:numeroPulsado("3"))
btn3.grid(row=4,column=1)

btn2=tkinter.Button(miFrame,text="2",width=3,command=lambda:numeroPulsado("2"))
btn2.grid(row=4,column=2)

btn1=tkinter.Button(miFrame,text="1",width=3,command=lambda:numeroPulsado("1"))
btn1.grid(row=4,column=3)

btnRestar=tkinter.Button(miFrame,text="-",width=3)
btnRestar.grid(row=4,column=4)

#------------------------fila4--------------------------------

btn0=tkinter.Button(miFrame,text="0",width=3,command=lambda:numeroPulsado("0"))
btn0.grid(row=5,column=1)

btnComa=tkinter.Button(miFrame,text=",",width=3)
btnComa.grid(row=5,column=2)

btnIgual=tkinter.Button(miFrame,text="=",width=3)
btnIgual.grid(row=5,column=3)

btnSuma=tkinter.Button(miFrame,text="+",width=3)
btnSuma.grid(row=5,column=4)

ventana.mainloop()