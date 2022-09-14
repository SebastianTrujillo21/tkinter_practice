from statistics import correlation
from tkinter import *
from tkinter import messagebox
import json

class juego:
    def __init__(self):
        self.preguntas_no=0
        self.ventana_titulo()
        self.ventana_pregunta()
        self.opcion_selecionada=IntVar()
        self.opts=self.radio_botones()
        self.ventana_opciones()
        self.botones()
        self.total_preguntas=len(pregunta)
        self.correctas=0

    def ventana_resultado(self):
        contador_incorrectas=self.total_preguntas-self.correctas
        correctas= f"correctas:{self.correctas}"
        incorrectas= f"incorrectas:{contador_incorrectas}"
        puntaje=int(self.correctas/self.total_preguntas * 100) 
        resultado=f"puntaje:{puntaje}%"
        messagebox.showinfo("resultado",f"{resultado}\n{correctas}\n{incorrectas}")

    def verificar_respuesta(self,preguntas_no):
        if self.opcion_selecionada.get()==respuesta[preguntas_no]:
            return True
    def siguiente_boton(self):
        if self.verificar_respuesta(self.preguntas_no):
            self.correctas+=1
        self.preguntas_no+=1
