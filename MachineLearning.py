import tkinter as tk
from tkinter import messagebox
import random
from tkinter.constants import ACTIVE, BOTTOM, DISABLED, RIGHT, SE, TOP, TRUE

matriz = [" "] * 9
ganador=0

seleccion=0

#DibujoSimbolos

def DibujarX():

    global Frame2

    global Pos

    global matriz

    TextoM.set("Turno de la ficha X.")

    P=int(Pos.get())

    if matriz[P-1] == " ":

        if P<10 :

            matriz[P-1]="X"

            if P<4 :
                y=50
            elif P<7:
                y=230
            else:
                y=400

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

            ganar(matriz,"X")

            empate(matriz)

            
            TextoM.set("Turno de la ficha O.")
        
        elif P <= 0 or P >10 or P == "":
            
            TextoM.set("Casilla no valida.")

    else:
        TextoM.set("Casilla no valida.")

    Pos.set("")

    

def DibujarC():

    global Frame2

    global Pos

    global matriz

    P=int(Pos.get())

    TextoM.set("Turno de la ficha O.")

    if matriz[P-1] == " ":

        if P<10 :
        
            matriz[P-1]="O"

            if P<4 :
                y=50
            elif P<7:
                y=230
            else:
                y=400

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

            ganar(matriz,"O")

            empate(matriz)
            
            TextoM.set("Turno de la ficha X.")


        else:

            TextoM.set("Casilla no valida.")

    else:

        TextoM.set("Casilla no valida.")

    Pos.set("")

    

# Definir finales de partida

def Reinicio(matriz):

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

        matriz[i-1]=" "

    TextoM.set("Seleccion de ficha.")

    BotonC.config(state=ACTIVE)
    BotonX.config(state=ACTIVE)
    BotonReinicio.config(state=DISABLED)

def empate(matriz):
	
    a=0

    for i in range(1,10):

        if matriz[i-1] !=  " ":

            a=a+1

    if a == 9:

        messagebox.showinfo(message="Empate.",title="Fin de la Partida.")

        Reinicio(matriz)


def ganar(matriz,i):


	if(matriz[0] == matriz[1] == matriz[2]!= " " or matriz[3] == matriz[4] == matriz[5]!= " " or matriz[6] == matriz[7] == matriz[8]!= " " 
		or matriz[0] == matriz[3] == matriz[6]!= " " or matriz[1] == matriz[4] == matriz[7]!= " " or matriz[2] == matriz[5] == matriz[8]!= " " or 
		matriz[0] == matriz[4] == matriz[8]!= " " or matriz[2] == matriz[4] == matriz[6]!= " "):
		            
            messagebox.showinfo(message="Ganador ficha "+ i ,title="Fin de la Partida.")
            
            Reinicio(matriz)

#MovimientoPc
def MovPc(a):

    P=random(1,9)

    if a==1:

        DibujarC()

    elif a==2:

        DibujarX()

#MovimientoPersona
def MovPersona(a):
    
    P=Pos.get()

    if a==1:

        DibujarX()

    elif a==2:

        DibujarC()
#Funciones de Seleccion
def PcvsJugador():
    seleccion=2
    VentanaS.destroy()

def PcvsPc():
    seleccion=1
    VentanaS.destroy()

def JugadorvsJugador():
    seleccion=0
    VentanaS.destroy()

#Ventana de Seleccion
VentanaS=tk.Tk()
VentanaS.title("Proyecto Concurso")
VentanaS.geometry("400x100")

Titu=tk.Label(VentanaS,text="Juego 3 en raya.",fg="Red")
Titu.place(x=150,y=0)

Preg=tk.Label(VentanaS,text="Seleccion de Jugadores: ")
Preg.place(x=10,y=30)

BotonPc=tk.Button(VentanaS,text="Jugador vs Jugador",command=JugadorvsJugador)
BotonPc.place(x=30,y=60)

BotonPc=tk.Button(VentanaS,text="Jugador vs PC",command=PcvsJugador)
BotonPc.place(x=165,y=60)

BotonPc=tk.Button(VentanaS,text="PC  vs  PC",command=PcvsPc)
BotonPc.place(x=280,y=60)

VentanaS.mainloop()

#VentanaPrincipal

Ventana=tk.Tk()
Ventana.title("Proyecto Concurso")
Ventana.geometry("550x660")
Ventana.resizable(0,0)


#Frame

Frame1=tk.Frame(Ventana)
Frame1.pack(fill="x")

Frame2=tk.Frame(Ventana)
Frame2.pack(fill="x")

Frame3=tk.Frame(Ventana,height=80)
Frame3.pack(fill="x")

Frame4=tk.Frame(Ventana,height=10)
Frame4.config(relief="groove",bd=1)
Frame4.pack(fill="x",side=BOTTOM)


#Texto

Titulo=tk.Label(Frame1,text="Juego Tres en Raya",font=50)
Titulo.config(fg="red")
Titulo.pack(side=tk.TOP)


TextoPosicion=tk.Label(Frame3,text="Posicion:")
TextoPosicion.place(x=220,y=0)

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

#Numero de Posiciones

for i in range (1,10) :

        if i<10 :
            if i<4 :
                y=30
            elif i<7:
                y=200
            else:
                y=370

        if i<10 :
            if i==1 or i==4 or i ==7 :
                x=30
            elif i==2 or i==5 or i ==8:
                x=200
            else:
                x=370


        Numero=tk.Label(Frame2,text=str(i),font=("50"))
        Numero.place(x=x,y=y)


#Botones

BotonX = tk.Button(Frame3,text="Presionar para X",command= lambda: DibujarX(),padx=5,pady=5,cursor="cross")
BotonX.place(x=50,y=30)

BotonC = tk.Button(Frame3,text="Presionar para Circulo",command= lambda: DibujarC(),padx=5,pady=5,cursor="circle")
BotonC.place(x=390,y=30)

BotonReinicio = tk.Button(Frame3,text="Reiniciar",command=lambda:Reinicio(matriz),padx=5,pady=5,state=DISABLED)
BotonReinicio.place(x=250,y=30)

#CuadroPosicion

Pos=tk.StringVar()

Posicion = tk.Entry(Frame3,textvariable=Pos,width=5)
Posicion.place(x=280,y=0)

Ventana.mainloop()