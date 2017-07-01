import Proyecto1 as LB

from Tkinter import *

import Image, ImageTk, os

def funcion(Imagen):
    self.etiqueta=a
    v0 = Tk()
    v0.geometry("1400x700")
    v0.title("Imagenes de PERRITOS")
    v0.config(bg="black")
    v1=Toplevel(v0)

    def mostrar(ventana): ventana.deiconify()
    def ocultar(ventana):ventana.withdraw()
    def ejecutar(f): v0.after(200,f)

    b1=Button(v0,text="VER MAS",command=lambda: ejecutar(mostrar(v1)))
    b1.grid(row=1,column=1)
    b2=Button(v1,text="VER MENOS",command=lambda: ejecutar(ocultar(v1)))
    b2.grid(row=1,column=1)

     for i,j=0 in imagenes:
         imagen = PhotoImage(file=LB.Imagen.a(i))
         label8 = Button(v1, image=imagen)
         label8.grid(row=j,colum=i)
         if i % 4 = 0:
             j += 1

    v1.withdraw()
    v0.mainloop()


def funcion2(Imagen):
    self.etiqueta=a
    v0 = Tk()
    v0.geometry("1400x700")
    v0.title("Imagenes de FLORES")
    v1=Toplevel(v0)

    def mostrar(ventana): ventana.deiconify()
    def ocultar(ventana):ventana.withdraw()
    def ejecutar(f): v0.after(200,f)

    v0.config(bg="black")
    v0.geometry("500x500")

    b1=Button(v0,text="VER MAS",command=lambda: ejecutar(mostrar(v1)))
    b1.grid(row=1,column=1)
    b2=Button(v1,text="VER MENOS",command=lambda: ejecutar(ocultar(v1)))
    b2.grid(row=1,column=1)

     for i,j=0 in imagenes:
         imagen = PhotoImage(file=LB.imagen.a(i))
         label8 = Button(v1, image=imagen)
         label8.grid(row=j,colum=i)
         if i % 4 = 0:
             j += 1

    v1.withdraw()
    v0.mainloop()



def funcion3(Imagen):
    self.etiqueta=a
    v0 = Tk()
    v0.geometry("1400x700")
    v0.title("Imagenes de BEBES")
    v1=Toplevel(v0)

    def mostrar(ventana): ventana.deiconify()
    def ocultar(ventana):ventana.withdraw()
    def ejecutar(f): v0.after(200,f)

    v0.config(bg="black")
    v0.geometry("500x500")

    b1=Button(v0,text="VER MAS",command=lambda: ejecutar(mostrar(v1)))
    b1.grid(row=1,column=1)
    b2=Button(v1,text="VER MENOS",command=lambda: ejecutar(ocultar(v1)))
    b2.grid(row=1,column=1)

    for i,j=0 in imagenes:
        imagen = PhotoImage(file=LB.Imagen.a(i))
        label8 = Button(v1, image=imagen)
        label8.grid(row=j,colum=i)
        if i % 4 = 0:
            j += 1


    v1.withdraw()
    v0.mainloop()


ventana=Tk()
ventana.geometry("400x130")
ventana.title('Imagenes')
label1=Label(ventana,text="Buscar en imagenes : ")
label1.grid(row=1,column=1)
variable_string = StringVar()

boton1 = Button(ventana,text="Perritos", command=lambda v=ventana, s = variable_string:funcion(s))
boton1.grid(row=8,column=9)

boton2 = Button(ventana,text="Flores", command=lambda v=ventana, s = variable_string:funcion2(s))
boton2.grid(row=9,column=10)

boton3 = Button(ventana,text="Bebes", command=lambda v=ventana, s = variable_string:funcion3(s))
boton3.grid(row=10,column=11)

ventana.mainloop()
