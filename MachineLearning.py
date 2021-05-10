import tkinter as tk
from PIL import Image ,ImageTk

def DibujarX():

    global Frame2

    global Pos
    x=int(Pos.get())

    if x<10 :
        if x<4 :
            x=0
        elif x<7:
            x=1
        else:
            x=2

    y=int(Pos.get())-1

    areaDeDibujo1 = tk.Canvas(Frame2,width=100,height=100)
    areaDeDibujo1.create_line(10, 10, 80, 80,width=4)
    areaDeDibujo1.create_line(10, 80, 80, 10,width=4)
    areaDeDibujo1.grid(row=x,column=y)


def DibujarC():

    global Frame2

    global Pos
    x=int(Pos.get())

    if x<10 :
        if x<4 :
            x=0
        elif x<7:
            x=1
        else:
            x=2

    y=int(Pos.get())-1

    areaDeDibujo = tk.Canvas(Frame2,width=100,height=100)
    areaDeDibujo.create_oval(0,0,100,100,width=4)
    areaDeDibujo.grid(row=x,column=y)


#Ventana

Ventana=tk.Tk()
Ventana.title("Proyecto Concurso")
Ventana.geometry("550x700")
Ventana.resizable(0,0)

#Frame
Frame1=tk.Frame(Ventana)
Frame1.grid(row=0,column=0)

Frame2=tk.Frame(Ventana)
Frame2.grid(row=1,column=0)

Frame3=tk.Frame(Ventana)
Frame3.grid(row=2,column=0)
#Titulo

Texto=tk.Label(Frame1,text="Juego Tres en Raya")
Texto.grid(row=0,column=0,columnspan=3)
Texto.config(fg="red")
TextoPosicion=tk.Label(Frame3,text="Escoja la posicion")
TextoPosicion.grid(row=0,column=0,columnspan=3)

#Fondo

Foto=tk.PhotoImage(file="MiChi.png")
Imagen=tk.Label(Frame2,image=Foto)
Imagen.grid(row=0,column=0,columnspan=3)

#Botones

BotonX = tk.Button(Frame3,text="Presionar para X",command= lambda: DibujarX(),padx=15,pady=15)
BotonX.grid(row=2,column=0)

BotonC = tk.Button(Frame3,text="Presionar para Circulo",command= lambda: DibujarC(),padx=15,pady=15)
BotonC.grid(row=2,column=2)

#CuadroPosicion

Pos=tk.StringVar()

Posicion = tk.Entry(Frame3,textvariable=Pos)
Posicion.grid(row=1,column=0,columnspan=3)

Ventana.mainloop()