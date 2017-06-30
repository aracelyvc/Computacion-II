empleados = []
for i in range (30):
    empleados.append([0]*3)
empleados [0] = [8895,3,[['intendencia','trapear baños'],['centro de copiado','comprar hojas'],['atención al cliente','atender solicitudes']] ]
empleados [1] = [8896,3,[['intendencia','trapear oficina'],['centro de copiado','comprar tinta'],['atención al cliente','atender solicitudes']] ]
empleados [2] = [8897,2,[['intendencia','barrer pasillos'],['centro de copiado','comprar hojas']] ]
empleados [3] = [8898,2,[['intendencia','trapear baños'],['centro de copiado','comprar tinta']] ]
empleados [4] = [8899,2,[['intendencia','trapear oficina'],['centro de copiado','comprar hojas']] ]
empleados [5] = [8900,3,[['intendencia','barrer pasillos'],['centro de copiado','comprar tinta'],['atención al cliente','atender solicitudes']] ]
empleados [6] = [8901,3,[['intendencia','trapear baños'],['centro de copiado','comprar hojas'],['atención al cliente','atender solicitudes']] ]
empleados [7] = [8902,2,[['intendencia','trapear oficina'],['centro de copiado','comprar tinta']] ]
empleados [8] = [8903,2,[['intendencia','barrer pasillos'],['centro de copiado','comprar hojas']] ]
empleados [9] = [8904,2,[['intendencia','trapear baños'],['centro de copiado','comprar tinta']] ]
empleados [10] = [8905,2,[['intendencia','trapear oficina'],['centro de copiado','comprar hojas']] ]
empleados [11] = [8906,2,[['intendencia','barrer pasillos'],['centro de copiado','comprar tinta']] ]
empleados [12] = [8907,2,[['intendencia','trapear baños'],['centro de copiado','comprar hojas']] ]
empleados [13] = [8908,3,[['intendencia','trapear oficina'],['centro de copiado','comprar tinta'],['atención al cliente','atender solicitudes']] ]
empleados [14] = [8909,3,[['intendencia','barrer pasillos'],['centro de copiado','comprar hojas'],['atención al cliente','atender solicitudes']] ]
empleados [15] = [8910,3,[['intendencia','trapear baños'],['centro de copiado','comprar tinta'],['atención al cliente','atender solicitudes']] ]
empleados [16] = [8911,2,[['intendencia','trapear oficina'],['centro de copiado','comprar hojas']] ]
empleados [17] = [8912,2,[['intendencia','barrer pasillos'],['centro de copiado','comprar tinta']] ]
empleados [18] = [8913,2,[['intendencia','trapear baños'],['centro de copiado','comprar hojas']] ]
empleados [19] = [8914,2,[['intendencia','trapear oficina'],['centro de copiado','comprar tinta']] ]
empleados [20] = [8915,1,[['intendencia','barrer pasillos']] ]
empleados [21] = [8916,3,[['intendencia','trapear baños'],['centro de copiado','comprar hojas'],['atención al cliente','atender solicitudes']] ]
empleados [22] = [8917,3,[['intendencia','trapear oficina'],['centro de copiado','comprar tinta'],['atención al cliente','atender solicitudes']] ]
empleados [23] = [8918,2,[['intendencia','barrer pasillos'],['centro de copiado','comprar hojas']] ]
empleados [24] = [8919,2,[['intendencia','trapear baños'],['centro de copiado','comprar tinta']] ]
empleados [25] = [8920,2,[['intendencia','trapear oficina'],['centro de copiado','comprar hojas']] ]
empleados [26] = [8921,2,[['intendencia','barrer pasillos'],['centro de copiado','comprar tinta']] ]
empleados [27] = [8922,2,[['intendencia','trapear baños'],['centro de copiado','comprar hojas']] ]
empleados [28] = [8923,2,[['intendencia','trapear oficina'],['centro de copiado','comprar tinta']] ]
empleados [29] = [8922,2,[['intendencia','barrer pasillos'],['centro de copiado','comprar hojas']] ]



def tarea():
    a= empleados[0][1]
    b=0
    for i in range (len(empleados)):
        if empleados [i][1]<a:
            a=empleados [i][1]
            b = i
    c = input("inserta el area solicitante: ")
    d = input("inserta ls descripción: ")
    e =[c,d]
    empleados [b][2].append(e)
    empleados [b][1] += 1

def descartar():
    for i in range ((len (empleados))-14):
        print ('empleado ', i+15, ' :')
        a =empleados [i+14][1]
        for x in range (a):
            print(empleados [i+14][2][a-x-1])
            empleados [i+14][2].pop()
            empleados [i+14][1] -= 1

def mostrar():
    print(empleados)

while True:
    print ('Menú:')
    print ('1.-Agregar una tarea al que tiene menos')
    print ('2.-Mostrar y descartar tareas del empleado 15 al 30')
    print ('3.-Mostrar pila entera')
    opcion = input("Inserta tu opción: ")
    if opcion=='1':
        tarea()
    if opcion=='2':
        descartar()
    if opcion=='3':
        mostrar()
