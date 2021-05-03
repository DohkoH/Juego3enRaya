import tkinter as tk

def Suma(x,y):

    return x+y

def Interface():

    Ventana=tk.Tk()

    Ventana.title("Proyecto concurso")

    Frame1=tk.Frame(Ventana)

    Texto=tk.Label(Frame1,text=Suma(4,5))

    Ventana.mainloop()

Interface()
