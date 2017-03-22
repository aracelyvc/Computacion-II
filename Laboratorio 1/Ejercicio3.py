#Aracely Velazquez Calderon
#Laboratorio 2
#Sumatoria

a = []

for i in range(6):
     a.append([])
     for j in range(6):
             a[i].append(i+j)
b=[]
z=([[fila[i]for fila in a]for i in [0,1,2,3,4,5]])
b.append(z)

c=[]
for i in b:
    for o in i:
        c.append(o)
        for u in c:
            suma=0
            suma=sum(u)
        print (suma)
