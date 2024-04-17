import numpy as sp
#1 crear un arreglo de 10 zeros
print(sp.zeros(10))
print('------------------------------------------------------------------')
#2 crear un arreglo de 10 unos
print(sp.ones(10))
print('------------------------------------------------------------------')
#3 crear un arreglo de 10 cincos
print(sp.ones(10)*5)
print('------------------------------------------------------------------')
#4 crear un arreglo con numeros enteros del 10 al 50
print(sp.arange(start=10,stop=50,step=1))
print('------------------------------------------------------------------')
#5 crear un arreglo con numeros pares del 10 al 50
print(sp.arange(start=10,stop=50,step=2))
print('------------------------------------------------------------------')
#6 crear una matrix 3x3 del 0 al 8
print(sp.arange(9).reshape(3,3))
print('------------------------------------------------------------------')
#7 crear una matrix de identidad de 3x3
print(sp.eye(3))
print('------------------------------------------------------------------')
#8 crear un numero aleatorio entre 0 y 1
print(sp.random.rand(1))
#9 Utilizar numpy para generar un arreglo de 25 numeros aleatorioas con una distribucion normal
print('------------------------------------------------------------------')
print(sp.random.randn(25))
#11 Crear la siguiente matriz
print(sp.arange(1,101).reshape(10,10)/100)
print('------------------------------------------------------------------')
#12 Crear un arreglo de 20 valores lineales entre 0 y 1
print(sp.linspace(0,1,20)) 
print('------------------------------------------------------------------')
mat = sp.arange(1,26).reshape(5,5)
print(mat)
print('------------------------------------------------------------------')
# Este codigo es para imprimir la fila y columna de una 
# matrix,el primer valor es la fila y el segundo la columna(Debo escribirlo con dos puntos al finalizar (:) 
# cada numero de filas y de columnas)
print(mat[3:,0:])
print('------------------------------------------------------------------')
print(mat[3,4])
print('------------------------------------------------------------------')
# Este codigo se utiliza para imprimir la fila y la columna de una matrix
# El primer numero se utiliza para seleccionar la fila,el segundo la columna y el tercero para espesificar
# hasta donde termina
print(mat[:3,1:2])
print('------------------------------------------------------------------')
print(mat[4,:])
print('------------------------------------------------------------------')
print(mat[3:5,:])
print('------------------------------------------------------------------')
print(mat.sum())#Este comando es para sumar todos los numeros del array
print('------------------------------------------------------------------')
print(mat.std())
print('------------------------------------------------------------------')
print(mat.sum(axis=0))
print('------------------------------------------------------------------')
