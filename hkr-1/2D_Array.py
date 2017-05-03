#Aracely Velazquez Calderon
#Laboratorio 2
#2D Array - DS

M= [[1,4,9,3,2,7],[0,0,0,0,0,0],[1,1,1,1,1,1],[1,2,3,4,5,6],[7,8,9,1,2,3],[4,5,6,7,8,9]]
a=0
for i in  range(0,4):
    for n in  range (0,4):
        suma=0
        for b in  range(n,n+3):
            suma= suma + M[i][b] + M[i+2][b]
        suma = suma+ M[i+1][n+1]
        if a<suma:
            a=suma
        suma=0

print (a)
