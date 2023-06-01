"""# listas vacias matrices
matriz_A = []
matriz_B = []
matriz_C = []
#pedir datos a usario
filas_A = int(input("Hola, ingresa el número de filas de matriz A: "))
columnas_A = int(input("Hola, ingresa el número de columnas de matriz A: "))
filas_B = int(input("Hola, ingresa el número de filas de matriz B: "))
columnas_B = int(input("Hola, ingresa el número de columnas de matriz B: "))

#regla de multiplicacion de matrices tienen que tener la misma dimensiones

if columnas_A != filas_B:
    print("no tiene solucion")
else:
    print ("_________matriZ a ********** ")
    for i in range(filas_A):
        matriz_A.append([0]*columnas_A)
    for f in range(filas_A):
        for c in range(columnas_A):
            matriz_A[f][c] = int(input("elemento %d,%d"%(f,c)))


    print ("_________matriZ b ********** ")
    for i in range():
        matriz_B.append([0]*columnas_B)
    for f in range(filas_A):
        for c in range(columnas_B):
            matriz_B[f][c] = int(input("elemento %d,%d"%(f,c)))

    print "*****matrices****\n"
    print "matriz_A\n"
    print("matriz_B")"""
from siempreprueba import mostrar
print("ingrese el orden de la matriz A:")
filasA, columnaA = int(input()), int(input()) #doble input no se para que jajaja
print("ingrese el orden de la matriz B:")
filasB, columnaB = int(input()), int(input())
#crear la matriz A con el tamaño de las filasA* colummnas B

if columnaA == filasB :
    
    #rellenando la matrizA
    matrizA = []
    for i in range (filasA): 
        matrizA.append([0]*columnaA) #es una linea comun para crear una matriz multiplicar un cero dentro de una lista con un elemento externo 
        #ejemplo : [0]*2 =[[0,0][0,0]]
     
     #rellenando la matrizB   
    matrizB = []
    for i in range (filasB): 
        matrizB.append([0]*columnaB)
    #rellenado de matriz A
    print("ingrese la matriz A")
    for filas in range(filasA):
        for columnas  in range(columnaA):
            matrizA[filas][columnas] = float(input(f"Ingresa  la posiscion numero {filas},{columnas} de la matrizA"))
            #rellenado de matriz B
    print("ingrese la matriz B")
    for filas in range(filasB):
        for columnas  in range(columnaB):
            matrizB[filas][columnas] = float(input(f"Ingresa  la posiscion numero {filas},{columnas} de la matrizB"))
            
    #    Creando la matriz resultante de tamaño filasA * columnasB

    matrizC = []
    for i in range(filasA):
        matrizC.append([0] * columnaB)
    # Efectuando la multiplicación entre las matrices A y B (esta es la clave aqui)
    for i in range(filasA):
        for j in range(columnaB):
            for k in range(filasB):
                matrizC[i][j] = matrizC[i][j] + (matrizA[i][k] * matrizB[k][j])

        # Mostrar la matriz resultante
    mostrar(matrizC)
else:
    print("ni maiz bro")