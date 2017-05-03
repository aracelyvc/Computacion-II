#Aracely Velazquez Calderon
#Laboratorio 2
#Caesar Cipher

TAM_MAX_CLAVE = 100

def Mensaje():
    print('Ingresa el mensaje que deseas encriptar:')
    return input()

def Clave():
    clave = 0
    while True:
        print('Ingresa el número de clave (1-%s)' % (TAM_MAX_CLAVE))
        clave = int(input())
        if (clave >= 1 and clave <= TAM_MAX_CLAVE):
            return clave

def Codigo(encriptar, mensaje, clave):
    if encriptar[0] == 'e':
        clave= clave
    traduccion = ''

    for simbolo in mensaje:
        if simbolo.isalpha():
            num = ord(simbolo)
            num += clave

            if simbolo.isupper():
                if num > ord('Z'):
                    num -= 100
                elif num < ord('A'):
                    num += 100
            elif simbolo.islower():
                if num > ord('z'):
                    num -= 100
                elif num < ord('a'):
                    num += 100

            traduccion += chr(num)
        else:
            traduccion += simbolo
    return traduccion

encriptar = Mensaje()
mensaje = Mensaje()
clave = Clave()

print('Tu texto traducido es:')
print(Codigo(encriptar, mensaje, clave))
