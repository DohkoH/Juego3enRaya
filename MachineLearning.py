import tkinter as tk

def Michi(Frame):

    Foto=tk.PhotoImage(file="MiChi.png")
    Imagen=tk.Label(Frame,image=Foto)

def Interface():

    Ventana=tk.Tk()

    Ventana.title("Proyecto concurso")

    Frame1=tk.Frame(Ventana)
    Frame1.grid(row=0,column=0)

    Michi(Frame1)

    Ventana.mainloop()


Interface()
