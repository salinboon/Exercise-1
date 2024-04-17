#Creacion de Series en libreria Pandas
#1
import pandas as pd
lista=['matematicas','ingles','español']
serie= pd.Series(data=lista,dtype='string')
print(serie)

#2
print(serie[2])

#3
dicc={'Matematica':6.0,'Ingles':8.0,'Economia':5.0}
serie=pd.Series(data=dicc)
print(serie['Ingles'])
print(serie['Matematica'])
#5
print(serie.size)
print(serie.dtype)
#6
print(serie[['Matematica','Ingles','Economia']])#sabaer nota de matematica de economia y de ingles
#7









