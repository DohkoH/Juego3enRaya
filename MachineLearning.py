import tkinter as tk
from tkinter.constants import ACTIVE, DISABLED, TOP
from PIL import Image ,ImageTk

def DibujarX():

    global Frame2

    global Pos
    x=int(Pos.get())

    if x<10 :
        if x<4 :
            y=50
        elif x<7:
            y=230
        else:
            y=400

    if x<10 :
        if x==1 or x==4 or x ==7 :
            x=50
        elif x==2 or x==5 or x ==8:
            x=230
        else:
            x=400


    areaDeDibujo1 = tk.Canvas(Frame2,width=80,height=80)
    areaDeDibujo1.create_line(10, 10, 80, 80,width=4)
    areaDeDibujo1.create_line(10, 80, 80, 10,width=4)
    areaDeDibujo1.place(x=x,y=y)

    Pos.set("")

    BotonC.config(state=ACTIVE)
    BotonX.config(state=DISABLED)



def DibujarC():

    global Frame2

    global Pos
    x=int(Pos.get())

    if x<10 :
        if x<4 :
            y=50
        elif x<7:
            y=230
        else:
            y=400

    if x<10 :
        if x==1 or x==4 or x ==7 :
            x=50
        elif x==2 or x==5 or x ==8:
            x=230
        else:
            x=400

    areaDeDibujo = tk.Canvas(Frame2,width=80,height=80)
    areaDeDibujo.create_oval(0,0,80,80,width=5)
    areaDeDibujo.place(x=x,y=y)

    Pos.set("")

    BotonX.config(state=ACTIVE)
    BotonC.config(state=DISABLED)



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
#Texto.place(x=30,y=10)
Texto.config(fg="red")
Texto.pack(side=tk.TOP)


TextoPosicion=tk.Label(Frame3,text="Escoja la posicion")
#TextoPosicion.place(x=30,y=600)
TextoPosicion.pack(side=tk.TOP)

#Fondo

Foto=tk.PhotoImage(file="MiChi.png")
Imagen=tk.Label(Frame2,image=Foto)
Imagen.grid(row=0,column=0,columnspan=3)

#Botones

BotonX = tk.Button(Frame3,text="Presionar para X",command= lambda: DibujarX(),padx=5,pady=5)
#BotonX.place(x=0,y=650)
BotonX.pack(side=tk.LEFT)

BotonC = tk.Button(Frame3,text="Presionar para Circulo",command= lambda: DibujarC(),padx=5,pady=5)
#BotonC.place(x=50,y=650)
BotonC.pack(side=tk.RIGHT)

#CuadroPosicion

Pos=tk.StringVar()

Posicion = tk.Entry(Frame3,textvariable=Pos)
#Posicion.place(x=30,y=620)
Posicion.pack(side=tk.TOP,after=TextoPosicion)

Ventana.mainloop()