import tkinter as tk
from PIL import Image ,ImageTk

def DibujarX(x,y):

    global Frame2

    X=Image.open('X.png')
    X=ImageTk.PhotoImage(X)
    X=tk.Label(Frame2,image=X)
    X.grid(row=x,column=y)



Ventana=tk.Tk()
Ventana.title("Proyecto Concurso")
Ventana.geometry("550x700")
Ventana.resizable(0,0)

Frame1=tk.Frame(Ventana)
Frame1.grid(row=0,column=0)

Frame2=tk.Frame(Ventana)
Frame2.grid(row=1,column=0)

Frame3=tk.Frame(Ventana)
Frame3.grid(row=2,column=0)
#Titulo

Texto=tk.Label(Frame1,text="Juego Tres en Raya")
Texto.grid(row=0,column=0,columnspan=3)

#Fondo

Foto=tk.PhotoImage(file="MiChi.png")
Imagen=tk.Label(Frame2,image=Foto)
Imagen.grid(row=0,column=0,columnspan=3)

#Botones

BotonX = tk.Button(Frame3,text="X",command= lambda: DibujarX(0,0))
BotonX.pack()

Ventana.mainloop()