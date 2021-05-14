import tkinter as tk
import time
import random
import os
from tkinter.constants import ACTIVE, DISABLED, TOP, TRUE
from PIL import Image ,ImageTk

matriz = [" "] * 9
ganador=0


#DibujoSimbolos

def DibujarX():

    global Frame2

    global Pos

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
    

def DibujarC():

    global Frame2

    global Pos

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

        areaDeDibujo = tk.Canvas(Frame2,width=80,height=80)
        areaDeDibujo.create_oval(0,0,80,80,width=4)
        areaDeDibujo.place(x=x,y=y)
        BotonX.config(state=ACTIVE)
        BotonC.config(state=DISABLED)
        BotonReinicio.config(state=ACTIVE)

    
    else:
        print("Casilla no valida.")

    Pos.set("")

# Definir finales de partida

def Reinicio():

    for i in range (1,9) :

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


# Movimientos

def movimiento_jugador():
	while True:
		posiciones = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		casilla = int(Pos.get())
		if casilla not in posiciones:
			print("Casilla no disponible")

		else:
			if matriz[casilla-1] == " ":
				matriz[casilla-1] = persona
				break
			else:
				print("Casilla no disponible")

def movimiento_computador():
	posiciones = [0, 1, 2, 3, 4, 5, 6, 7, 8]
	casilla = 9
	parar = False

	for i in posiciones:
		copia = list(matriz)
		if copia[i] == " ":
			copia[i] = computador
			if ganar(copia) == True:
				casilla = i

	if casilla == 9:
		for j in posiciones:
			if copia[j] == " ":
				copia[j] = persona
				if ganar(copia) == True:
					casilla = j

	if casilla == 9:
		while(not parar):
			casilla = random.randint(0, 8)
			if matriz[casilla] == " ":
				parar = True
	matriz[casilla] = computador

#Ventana

Ventana=tk.Tk()
Ventana.title("Proyecto Concurso")
Ventana.geometry("550x700")
Ventana.resizable(0,0)

#Frame

Frame1=tk.Frame(Ventana)
Frame1.pack()

Frame2=tk.Frame(Ventana)
Frame2.pack()

Frame3=tk.Frame(Ventana)
Frame3.pack()

#Titulo

Texto=tk.Label(Frame1,text="Juego Tres en Raya")
Texto.config(fg="red")
Texto.pack(side=tk.TOP)


TextoPosicion=tk.Label(Frame3,text="Escoja la posicion")
TextoPosicion.pack(side=tk.TOP)

#Fondo

Foto=tk.PhotoImage(file="MiChi.png")
Imagen=tk.Label(Frame2,image=Foto)
Imagen.grid(row=0,column=0,columnspan=3)

#Botones

BotonX = tk.Button(Frame3,text="Presionar para X",command= lambda: DibujarX(),padx=5,pady=5)
BotonX.pack(side=tk.LEFT)

BotonC = tk.Button(Frame3,text="Presionar para Circulo",command= lambda: DibujarC(),padx=5,pady=5)
BotonC.pack(side=tk.RIGHT)

BotonReinicio = tk.Button(Frame3,text="Reiniciar",command=lambda:Reinicio(),padx=5,pady=5,state=DISABLED)
BotonReinicio.pack(side=tk.BOTTOM)

#CuadroPosicion

Pos=tk.StringVar()

Posicion = tk.Entry(Frame3,textvariable=Pos)
Posicion.pack(side=tk.TOP,after=TextoPosicion)

Ventana.mainloop()