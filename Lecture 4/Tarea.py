import pandas as pd
import numpy as np
# Ejercicio 1
inicio=int(input('introduce el año inicial '))
final=int(input('introduce el año final '))
ventas={}
for i in range(inicio,final+1):
    ventas[i]=float(input(f'introduce las ventas del año {i} '))
print(ventas)
s=pd.Series(ventas)

#Ejercicio 2
def notas_alumnos(s):
    Datos=[s.min(),s.max(),s.mean(),s.std()]
    indices=['min','Max','Media','Desviacion tipica']
    a=pd.Series(Datos,index=indices)
    return a
print(notas_alumnos(s))

#Ejercicio 3
def notas_de_los_alumnos():
    
















