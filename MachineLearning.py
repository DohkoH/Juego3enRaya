import tkinter as tk

Ventana=tk.Tk()
Ventana.title("Proyecto Concurso")
Ventana.geometry("600x600")
Ventana.resizable(0,0)

Frame1=tk.Frame(Ventana)
Frame1.pack()

Frame2=tk.Frame(Ventana)
Frame2.pack()

Texto=tk.Label(Frame1,text="Juego Tres en Raya")
Texto.grid(row=0,column=0)

Foto=tk.PhotoImage(file="MiChi.png")
Foto.subsample(4)
Imagen=tk.Label(Frame2,image=Foto)
Imagen.grid(row=0,column=0)

Ventana.mainloop()