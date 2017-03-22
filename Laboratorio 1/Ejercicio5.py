#Aracely Velazquez Calderon
#Laboratorio 2
#The Power Sum

import math

y=int(input("ingresa un numero entero x tq 1<=x>=1000:  "))

x = math.sqrt(y)
a = int(x)
c=y-(pow(a,2))

d=math.sqrt(c)
e = int(d)
g=c-(pow(e,2))

h=math.sqrt(g)
i = int(h)
j=g-(pow(i,2))

k=math.sqrt(j)
l = int(k)
m=j-(pow(l,2))

n=math.sqrt(m)
o = int(n)
p=m-(pow(o,2))

print (y,'=',a,'(^2)+',e,'(^2)+',i,'(^2)+',l,'(^2)+',o,'(^2)')
