from Tkinter import *

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
