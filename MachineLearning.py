import tkinter as tk
import time
import random
import os
from tkinter.constants import ACTIVE, BOTTOM, DISABLED, RIGHT, SE, TOP, TRUE
from PIL import Image ,ImageTk

matriz = [" "] * 9
ganador=0

turno=1

#DibujoSimbolos

def DibujarX():

    global Frame2

    global Pos

    global TextoM


<<<<<<< HEAD
    TextoM="Primer turno de X."
=======
    TextoM.set("Turno de la ficha X.")
>>>>>>> c50d277e1f3047f63ed15db3ef62a85f3f83a864

    P=int(Pos.get())

    if P<10 :
        if P<4 :
            y=50
        elif P<7:
            y=230
        else:
            y=400

    if P<10 :
        if P==1 or P==4 or P ==7 :
            x=50
        elif P==2 or P==5 or P ==8:
            x=230
        else:
            x=400

        areaDeDibujo1 = tk.Canvas(Frame2,width=80,height=80)
        areaDeDibujo1.create_line(10, 10, 80, 80,width=4)
        areaDeDibujo1.create_line(10, 80, 80, 10,width=4)
        areaDeDibujo1.place(x=x,y=y)

        BotonC.config(state=ACTIVE)
        BotonX.config(state=DISABLED)
        BotonReinicio.config(state=ACTIVE)

    
    elif P <= 0 or P >10 or P == "":
        print("Casilla no valida.")

    Pos.set("")

    TextoM.set("Turno de la ficha O.")
    

def DibujarC():

    global Frame2

    global Pos

    P=int(Pos.get())

    TextoM.set("Turno de la ficha O.")

    if P<10 :
        if P<4 :
            y=50
        elif P<7:
            y=230
        else:
            y=400

    if P<10 :
        if P==1 or P==4 or P ==7 :
            x=50
        elif P==2 or P==5 or P ==8:
            x=230
        else:
            x=400

        areaDeDibujo = tk.Canvas(Frame2,width=80,height=80)
        areaDeDibujo.create_oval(0,0,80,80,width=4)
        areaDeDibujo.place(x=x,y=y)
        BotonX.config(state=ACTIVE)
        BotonC.config(state=DISABLED)
        BotonReinicio.config(state=ACTIVE)

    
    else:
        print("Casilla no valida.")

    Pos.set("")

    TextoM.set("Turno de la ficha X.")

# Definir finales de partida

def Reinicio():

    TextoM.set("Reiniciando el juego.")

    for i in range (1,10) :

        if i<10 :
            if i<4 :
                y=50
            elif i<7:
                y=230
            else:
                y=400

        if i<10 :
            if i==1 or i==4 or i ==7 :
                x=50
            elif i==2 or i==5 or i ==8:
                x=230
            else:
                x=400


        areaDibujo = tk.Canvas(Frame2,width=80,height=80)
        areaDibujo.place(x=x,y=y)


    TextoM.set("Seleccion de ficha.")

    BotonC.config(state=ACTIVE)
    BotonX.config(state=ACTIVE)
    BotonReinicio.config(state=DISABLED)

def empate(matriz):
	empate = True
	i = 0
	while(empate == True and i < 9):
		if matriz[i] ==" ":
			empate = False
		i = i + 1

	return empate

def ganar(matriz):
	if(matriz[0] == matriz[1] == matriz[2]!= " " or matriz[3] == matriz[4] == matriz[5]!= " " or matriz[6] == matriz[7] == matriz[8]!= " " 
		or matriz[0] == matriz[3] == matriz[6]!= " " or matriz[1] == matriz[4] == matriz[7]!= " " or matriz[2] == matriz[5] == matriz[8]!= " " or 
		matriz[0] == matriz[4] == matriz[8]!= " " or matriz[2] == matriz[4] == matriz[6]!= " "):
		return True
	else:
		return False


#Ventana

Ventana=tk.Tk()
Ventana.title("Proyecto Concurso")
Ventana.geometry("550x660")
Ventana.resizable(0,0)

#Frame

Frame1=tk.Frame(Ventana)
Frame1.pack(fill="x")

Frame2=tk.Frame(Ventana)
Frame2.pack(fill="x")

Frame3=tk.Frame(Ventana)
Frame3.pack(fill="x")

Frame4=tk.Frame(Ventana)
Frame4.config(relief="ridge",bd=2)
Frame4.pack(fill="x")


#Texto

Titulo=tk.Label(Frame1,text="Juego Tres en Raya")
Titulo.config(fg="red")
Titulo.pack(side=tk.TOP)


TextoPosicion=tk.Label(Frame3,text="Escoja la posicion")
TextoPosicion.pack(side=tk.TOP)

TextoEstado=tk.Label(Frame4,text="El estado del juego :")
TextoEstado.pack(side=tk.LEFT)

TextoM=tk.StringVar()
TextoM.set("Selecion de ficha.")
TextoModificable=tk.Label(Frame4,text=TextoM)
TextoModificable.config(textvariable=TextoM)
TextoModificable.pack(side=tk.LEFT)

#Fondo

Foto=tk.PhotoImage(file="MiChi.png")
Imagen=tk.Label(Frame2,image=Foto)
Imagen.grid(row=0,column=0,columnspan=3)

#Botones

BotonX = tk.Button(Frame3,text="Presionar para X",command= lambda: DibujarX(),padx=5,pady=5,cursor="cross")
BotonX.pack(side=tk.LEFT)

BotonC = tk.Button(Frame3,text="Presionar para Circulo",command= lambda: DibujarC(),padx=5,pady=5,cursor="circle")
BotonC.pack(side=tk.RIGHT)

BotonReinicio = tk.Button(Frame3,text="Reiniciar",command=lambda:Reinicio(),padx=5,pady=5,state=DISABLED)
BotonReinicio.pack(side=tk.BOTTOM)

#CuadroPosicion

Pos=tk.StringVar()

Posicion = tk.Entry(Frame3,textvariable=Pos)
Posicion.pack(side=tk.TOP,after=TextoPosicion)

Ventana.mainloop()