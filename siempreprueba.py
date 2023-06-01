#Recorrer una matriz sin funciones y  ademas imprime en vertical
"""persona = [ [1,2,3],[4,5,6],[7,8,9] ]
for fila in persona :
    for columna in fila:
        print(columna, end=" ")
    print()"""

"""
#matriz crea una matriz identidad cambiando el numero 0 por 1 usando las posiciones
matrix_EVOLUTION = [] #creamos una lista vacia
for i in range (3):#un ciclo for para crear las filas que van a ser 3
    matrix_EVOLUTION.append( [0]*4)#agregamos con append las filas y multiplcamos 6*0 para rellenar elementos
    #en este caso son 60
matrix_EVOLUTION[0][0] = 1
matrix_EVOLUTION[1][1] = 1
matrix_EVOLUTION[2][3] = 1 """



"""#CON ESTA FUNCION PUEDO RECORRER UNA MATRIZ (FUNCION SIN RETURN)
def mostrar (matrix):
    for m in matrix:
        print(m)
#mostrar(persona)

from random import randint
lista = []

for i in range (77):
    lista.append(['-']*88)
 
for i in lista:
    pos = randint(1,80)
    i [pos] = 'x'
for i  in lista:
    print(' '.join(i))"""


#print(matrix_EVOLUTION)

#funcion que recorre una matriz aunque todavia no se como hace los saltos de linea
#def mostrar (elemento):
    #for x in elemento:
        #print(x)
#mostrar(matrix_EVOLUTION)
#len(matrix_EVOLUTION[0])

#funcion que recorre una matriz pero esta vez imprime de manera vertical y sin los corchetes
"""def imprimir_matriz(matriz):
    for fila in matriz:
        for columna in fila:
            print(columna, end=" ")
        print()"""
