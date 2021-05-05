import tkinter as tk
from PIL import Image ,ImageTk

def DibujarX(x,y):

    global Frame2

    X=Image.open('X.png')
    X=ImageTk.PhotoImage(X)
    X=tk.Label(Frame2,image=X)
    X.grid(row=x,column=y)

def DibujarC(x,y):

    global Frame2

    X=Image.open('Circulo.jpg')
    X=ImageTk.PhotoImage(X)
    X=tk.Label(Frame2,image=X)
    X.grid(row=x,column=y)

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

#Fondo

Foto=tk.PhotoImage(file="MiChi.png")
Imagen=tk.Label(Frame2,image=Foto)
Imagen.grid(row=0,column=0,columnspan=3)

#Botones

BotonX = tk.Button(Frame3,text="Presionar para X",command= lambda: DibujarX(0,0),padx=15,pady=15)
BotonX.grid(row=0,column=0)

BotonC = tk.Button(Frame3,text="Presionar para Circulo",command= lambda: DibujarC(0,1),padx=15,pady=15)
BotonC.grid(row=0,column=1)

Ventana.mainloop()