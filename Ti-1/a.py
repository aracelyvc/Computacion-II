from Tkinter import *

def funcion():
   v0 = Tk()
   v0.geometry("1400x700")
   v0.title("Imagenes de PERRITOS")
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

   imagen1=PhotoImage(file="122.gif")
   label1 = Button(v0, image=imagen1)
   label1.grid(row=2,column=1)

   imagen2=PhotoImage(file="123.gif")
   label2 = Button(v0, image=imagen2)
   label2.grid(row=2,column=2)

   imagen3=PhotoImage(file="124.gif")
   label3 = Button(v0, image=imagen3)
   label3.grid(row=3,column=1)

   imagen4=PhotoImage(file="125.gif")
   label4 = Button(v0, image=imagen4)
   label4.grid(row=3,column=2)

   imagen5=PhotoImage(file="126.gif")
   label5 = Button(v1, image=imagen5)
   label5.grid(row=2,column=1)

   imagen6=PhotoImage(file="127.gif")
   label6 = Button(v1, image=imagen6)
   label6.grid(row=2,column=2)

   imagen7=PhotoImage(file="128.gif")
   label7 = Button(v1, image=imagen7)
   label7.grid(row=3,column=1)

   imagen8=PhotoImage(file="121.gif")
   label8 = Button(v1, image=imagen8)
   label8.grid(row=3,column=2)

   v1.withdraw()
   v0.mainloop()


def funcion2():
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

   imagen1=PhotoImage(file="111.gif")
   label1 = Button(v0, image=imagen1)
   label1.grid(row=2,column=1)

   imagen2=PhotoImage(file="112.gif")
   label2 = Button(v0, image=imagen2)
   label2.grid(row=2,column=2)

   imagen3=PhotoImage(file="113.gif")
   label3 = Button(v0, image=imagen3)
   label3.grid(row=3,column=1)

   imagen4=PhotoImage(file="114.gif")
   label4 = Button(v0, image=imagen4)
   label4.grid(row=3,column=2)

   imagen5=PhotoImage(file="115.gif")
   label5 = Button(v1, image=imagen5)
   label5.grid(row=2,column=1)

   imagen6=PhotoImage(file="116.gif")
   label6 = Button(v1, image=imagen6)
   label6.grid(row=2,column=2)

   imagen7=PhotoImage(file="117.gif")
   label7 = Button(v1, image=imagen7)
   label7.grid(row=3,column=1)

   imagen8=PhotoImage(file="118.gif")
   label8 = Button(v1, image=imagen8)
   label8.grid(row=3,column=2)

   v1.withdraw()
   v0.mainloop()


def funcion3(busqueda):
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

   imagen1=PhotoImage(file="131.gif")
   label1 = Button(v0, image=imagen1)
   label1.grid(row=2,column=1)

   imagen2=PhotoImage(file="132.gif")
   label2 = Button(v0, image=imagen2)
   label2.grid(row=2,column=2)

   imagen3=PhotoImage(file="133.gif")
   label3 = Button(v0, image=imagen3)
   label3.grid(row=3,column=1)

   imagen4=PhotoImage(file="134.gif")
   label4 = Button(v0, image=imagen4)
   label4.grid(row=3,column=2)

   imagen5=PhotoImage(file="135.gif")
   label5 = Button(v1, image=imagen5)
   label5.grid(row=2,column=1)

   imagen6=PhotoImage(file="136.gif")
   label6 = Button(v1, image=imagen6)
   label6.grid(row=2,column=2)

   v1.withdraw()
   v0.mainloop()


ventana=Tk()
ventana.geometry("400x130")
ventana.title('Imagenes')
label1=Label(ventana,text="Buscar en imagenes : ")
label1.grid(row=1,column=1)
variable_string = StringVar()

boton1 = Button(ventana,text="Perritos", command=funcion)
boton1.grid(row=8,column=9)

boton2 = Button(ventana,text="Flores", command=funcion2)
boton2.grid(row=9,column=10)

boton3 = Button(ventana,text="Bebes", command=funcion3)
boton3.grid(row=10,column=11)

ventana.mainloop()
