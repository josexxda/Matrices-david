#for i in range(1,7):#matriz vertical pero si agregamos end es horizonta
#    print(i, end= " ")
"""efectivamente en el código anterior se están imprimiendo parejas ordenadas de valores, pero no son tuplas ya que no se están
utilizando paréntesis 
para definirlas. En realidad se están utilizando 
expresiones de interpolación de cadenas (f-strings) para imprimir dos variables separadas por una coma
y entre paréntesis, lo cual produce una apariencia similar a la de una tupla. 
Pero en realidad se está imprimiendo una cadena de texto. Por lo tanto, en el código 
anterior se están imprimiendo cadenas de texto que parecen tuplas.
"""
for i in range(1,7):
    #ciclo for aninado por iteracion de i el segundo ciclo hace una ronde completa de n a 7
     for j in  range(1,7):
         print(i , end='  ') 
     print(' ')

for i in range(1,7):
    #ciclo for aninado por iteracion de i el segundo ciclo hace una ronde completa de n a 7
     for j in  range(1,7):
        print(f'({i},{j})', end =' ')
     print(' ') 


print('')
for i in range(1,7):
    #ciclo for aninado por iteracion de i el segundo ciclo hace una ronde completa de n a 7
     for j in  range(1,7):
        if (i==j):
             print(1 , end= ('  '))
        else:
         print(0 , end='  ')
     print(' ') 
     