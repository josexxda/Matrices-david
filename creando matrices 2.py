#CREANDO MATRICES DESDE CERO CON CICLOS FOR FOR
matriz = []

for i in range(0,6):
    matriz.append([0]*6)
#print(matriz)
    
#matriz = []

#for i in range(0,6):
#    matriz.append([0]*6)

#print(matriz)

#funcion que recorre una matriz pero esta vez imprime de manera vertical y sin los corchetes
def imprimir_matriz(matriz):
    for fila in matriz:
        for columna in fila:
            print(columna, end=" ")
        print()
        
"""def mostrar (elemento):
    for x in elemento:
        print(x)"""
    
imprimir_matriz(matriz)

