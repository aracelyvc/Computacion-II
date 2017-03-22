#Aracely Velazquez Calderon
#Laboratorio 2
#CamelCase

x=input("ingresa el mensaje(ej. holaQueTal): ")
def abcd(x):
    final = ''
    for item in x:
        if item.isupper():
            final += "_"+item.lower()
        else:
            final += item
    if final[0] == "_":
        final = final[1:]
    return final

a= abcd(x)

def contar(a):
    contador = 1
    for i in a:
        if i == "_":
            contador = contador + 1
    return(contador)

print(contar(a))
