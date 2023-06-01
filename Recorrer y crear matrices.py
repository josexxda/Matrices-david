#Recorrer una matriz sin funciones y  ademas imprime en vertical
"""persona = [ [1,2,3],[4,5,6],[7,8,9] ]
for fila in persona :
    for columna in fila:
        print(columna, end=" ")
    print()"""
    
"""#CON ESTA FUNCION PUEDO RECORRER UNA MATRIZ (FUNCION SIN RETURN)
def mostrar (matrix):
    for m in matrix:
        print(m)
#mostrar(persona)"""

#funcion que recorre una matriz pero esta vez imprime de manera vertical y sin los corchetes
def imprimir_matriz(matriz):
    for fila in matriz:
        for columna in fila:
            print(columna, end=" ")
        print()