movimientos = []
for i in range (10):
    movimientos.append([0]*7)
a = 0
movimientos [0] = [1001,1,1,2003,8894,1500,"deposito"]
movimientos [1] = [1002,27,3,2003,6116,3500,"deposito"]
movimientos [2] = [1003,18,12,2003,4728,1200,"deposito"]
movimientos [3] = [1004,21,12,2003,8894,200,"extraccion"]
movimientos [4] = [1005,27,1,2004,4728,900,"extraccion"]
movimientos [5] = [1006,12,7,2004,9110,1100,"deposito"]
movimientos [6] = [1007,16,7,2004,6116,2500,"extraccion"]
movimientos [7] = [1008,16,7,2004,8894,3000,"deposito"]
movimientos [8] = [1009,18,12,2004,4728,100,"extraccion"]
movimientos [9] = [1010,12,1,2005,8894,1500,"deposito"]

def numero():
    a= 0
    for i in range (len(movimientos)):
        if movimientos [i][3]==2004:
            if movimientos [i][2]<=7:
                a += 1
    print ("El total de movimientos es: ",a)

def a2003():
    a =0
    b =0
    for i in range (len(movimientos)):
        if movimientos [i][3]==2003:
            if movimientos [i][6]=="deposito":
                a += movimientos [i][5]
            elif movimientos [i][6]=="extraccion":
                b += movimientos [i][5]
    print("depositado: ",a," extraido: ",b)

def saldo():
    a = 0
    for i in range (len(movimientos)):
        if movimientos [i][3]==2003:
            if movimientos [i][4]==8894:
                if movimientos [i][6] == "deposito":
                    a+= movimientos[i][5]
                elif movimientos [i][6] == "extraccion":
                    a-= movimientos[i][5]
    print("El saldo de la cuenta es: ",a)
while True:
    print ('Menú:')
    print ('1.-Depósitos del 01/01/2004 al 31/07/2004')
    print ('2.-Depositado y Extraido del 2003')
    print ('3.- Saldo de la cuenta 8894 en 2003')
    opcion = input("Inserta tu opción: ")
    if opcion=='1':
        numero()
    if opcion=='2':
        a2003()
    if opcion=='3':
        saldo()
