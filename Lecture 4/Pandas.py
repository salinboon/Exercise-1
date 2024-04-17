import  pandas as pa
import numpy as np
import datetime
"""Pandas dispone de dos estructuras de datos. Estas son de una dimension
 (Series) y de dos dimensiones(Data Frame) """
'''Nota: El data Frame nace de la combinacion de dos Series'''
#1
lista=['colombia','Venezuela','Estados unidos','Ecuador','Chile']
"""Aqui se establace el data y despues el tipo de dato"""
serie=pa.Series(data=lista,dtype='string')
print(serie)
#2
'Este comando se usa para acceder a un elemento de la serie'
print(serie[1]) 
#3
dicc={'Matematica':4.0,'Sociales':5.0,'Biologia':3.0,'Ingles':4.0}
print(dicc)
serie1=pa.Series(data=dicc)
print(serie1)
#4
print('-----------------------------------print(serie1[''Matematica''])------------------------------------------------------')
print(serie1['Matematica'])
print('-------------------------------------------print(serie1.count())------------------------------------------------------')
#5
print(serie1.count())#Esta funcion sirve para contar los valores claves de un diccionario convertido en un array
print('-----------------------------------------print(serie1[3])-------------------------------------------------------------')
#6
print(serie1[3])
print('-------------------------------------------print(serie1.dtype)--------------------------------------------------------')
#8
print(serie1.dtype)
print('-------------------------------------------print(serie1.cumsum())-----------------------------------------------------')
#9
print(serie1.cumsum())
#10
print('----------------------------------------print(serie1.max())-----------------------------------------------------------')
print(serie1.max())
#11
print('--------------------------------------print(serie1.min())-------------------------------------------------------------')
print(serie1.min())
#12
print('-----------------------------------------print(serie1.mean())---------------------------------------------------------')
print(serie1.mean())
#13
print('---------------------------------------print(serie1.sum())------------------------------------------------------------')
print(serie1.sum())
#14
#15
print('---------------------------------print(serie1.value_counts())---------------------------------------------------------')
print(serie1.value_counts())#Esta funcion sirve para contar los valores de un diccionario convertido en una serie o una serie directamente
#16
print('---------------------------------print(serie.mean())------------------------------------------------------------------')
print(serie1.mean())#Este comando se utiliza para devolver la media de un diccionario convertido en una serie o de una serie
#17
print('---------------------------------print(serie1.std())------------------------------------------------------------------')
print(serie1.std())#Este comando se utiliza hayar la desviacion tipica de un diccionario convertido en una serie o de una serie
#18
print('---------------------------------print(serie1.describe())-------------------------------------------------------------')
print(serie1.describe())#Este comando lo que hace es realizar un resumen descriptivo de los datos de la serie
'''Es decir este comando me entrega la media, la desviación estándar, los valores mínimo y máximo, y los percentiles.''' 
print('---------------------------------Operaciones con las series-----------------------------------------------------------')
print('---------------------------------print(serie1*2())--------------------------------------------------------------------')
print(serie1*2)
print('---------------------------------print(serie1//2)---------------------------------------------------------------------')
print(serie1//2)
print('---------------------------------print(serie1**2)---------------------------------------------------------------------')
print(serie1**2)
print('---------------------------------print(serie1.apply(log))-------------------------------------------------------------')
from math import log
print(serie1.apply(log))
print('----------------------------------------Creacion de mascaras----------------------------------------------------------')
mask= (serie1 % 2) ==0
print(mask)
print('_______________________')
print(serie1[mask])
print('-------------------------------------print(serie1.sort_values(ascending=True))----------------------------------------')
print(serie1.sort_values(ascending=True))#Este comando sirve para ordenar de menor a mayor dependiendo de el valor de asceding
''' Si esta en True los valores se ordenan de menor a mayor y si esta en False los valores
se ordenan de mayor a menor'''
print('------------------------------print(serie1.sort_index(ascending=True))------------------------------------------------')
print(serie1.sort_index(ascending=True))
print('------------------------------Eliminar datos desconocidos de una serie------------------------------------------------')
'''Debo recordar que los datos desconocidos se representan por NAN y los nulos por NONE'''
a0_1=pa.Series(['a','b','c',None,np.NaN,'d'])
print(a0_1)
print('-------------------------------------------print(a0_1.dropna())------------------------------------------------------')
s=a0_1.dropna()
print(s)#Este comando es para eliminar los  datos de tipo NaN y los None
#y cuenta con un parametro especial de nombre inplace=True que guarda la configuracion sin los datos tipo Nan y None y 
#no los guardara cuando esta en False
print('------------------------------------------------Crear dataFrame en pandas--------------------------------------------')
Dato1={'Nombres':['juan','salin','sebastian','lucas','gerardo'],
       'edad':[40,30,50,90,21],
       'Grado':['Economia','Medicina','Ingenieria','Arquitectura','Economia'],
       'Correo':['Juan@gmail.com','salin@gmail.com','sebastian@gmail.com','lucas@gmail.com','gerardo@gmail.com']}
df=pa.DataFrame(data=Dato1,index=range(1,6))
print(df)
'''Un DataFrame se puede crear a partir de una lista o partir de diccionarios'''
''' A continuacion un ejemplo de crear un data frame a partir de unas listas en python'''
datos_de_la_lista=[['Juan',40,'juan@gmail.com'],['salin',22,'salin@gmail.com'],['josue',15,'josue@gmail.com'],['Rodolfo',52,'Rodolfo@gmail.com']]
columnas_de_las_listas=['Nombres','edad','Correo']
print('------------------------------------------------------------------------------------')
df1=pa.DataFrame(data=datos_de_la_lista,columns=columnas_de_las_listas)
print(df1)
print('------------------------------------------------------------------------------------')
'''Este comando sirve para generar valores aleatorios en una matrix 4x4 con las columnas a,b,c,d y las filas
z,x,y,w'''
'''Nota:debo recordar que el comando np.random.randn(4,4) se utiliza para generar valores aleatorios entre una media de 0
y desviacion estandar de 1'''
df3=pa.DataFrame(np.random.randn(4,4),columns=['A','B','C','D'],index=['Z','X','Y','W'])
print(df3)
print('------------------------------------------------------------------------------------')
df4=pa.read_csv('Datos de prueba.csv',sep='|')
print(df4)
print('------------------------------------------------------------------------------------')
''' Debo recordar que este mismo metodo sirve para archivos en formato excel '''
'''Atributos de un Data Frame'''
print(df4.info())#Este comando me informacion del data frame o marco de datos
print('------------------------------------------------------------------------------------')
print(df4.shape)
print('------------------------------------------------------------------------------------')
print(df4.size)
print('------------------------------------------------------------------------------------')
'''Este comando es para imprimir el numero de columnas correspodientes a el data frame seleccionado'''
print(df4.head(2))
print('------------------------------------------------------------------------------------')
'''Este comando es para imprimir el numero de filas correspodientes a el data frame seleccionado'''
print(df4.tail(1))
print('------------------------------------------------------------------------------------')
'''Este comando nos arroja el nombre de las columnas '''
print(df4.columns)
print('------------------------------------------------------------------------------------')
'''Este comando se encarga de traer los primeros n elementos del data frame'''
print('------------------------------------------------------------------------------------')
print(df4.head(n=2))
'''Este comando se encarga de traer los ultimos elemento n del data frame'''
print('------------------------------------------------------------------------------------')
df4.tail(n=1)
'''Este comando sirve para imprimir la columna que nosotros hemos decidido llamar'''
print('------------------------------------------------------------------------------------')
print(df4['Nombre'])
print('------------------------------------------------------------------------------------')
'''Este comando sirve para añadir  nuevas columnas con sus respectivos datos al data frame'''
print('------------------------------------------------------------------------------------')
df4['Direccion']=['Calle 13#24-18','Calle 34#23-19','Calle 21#67-90','Cra 55#23-12']
print(df4)
print('------------------------------------------------------------------------------------')
'''Operaciones sobre un data Frame'''
print(df4['Edad']*10)#Mediante estos comandos podemos ejecutar operaciones para distintas columnas en python
print(df4['Edad']<23)
'''df4[columna].apply(f),El siguiente comando se utiliza para aplicar una funcion a los distintos elementos del Data frame'''
print(df4['Edad'].apply(log))
df5=pa.DataFrame ({'Nombre':['Maria','Antonio','Luis'],'Nacimiento':['05-03-2000','20-5-2001','23-8-1978']})
print(df5)
'''Este comando se utiliza para cambiar el formato de un columna defechas o tiempos de formato string a datatime'''
df5['Nacimiento']=pa.to_datetime(df5['Nacimiento'],format='%d-%M-%Y')
print(df5.info())
print(df4)
print('------------------------------------------------------------------------------------')
s_01=df4.rename(columns={'Nombre':'cod_nombre','Edad':'nom_Edad'})
print(s_01)
print('------------------------------------------------------------------------------------')
''' Este comando se utiliza para cambiar el indice de cada fila en un data frame, sin embargo hay que tener en cuenta que
al usarlo con el parametro inplace=True se modifica el data frame original es decir no se guarda una copia.
Si se imprime la variable s_02 el resultado sera none ya que el comando modifica la varible anterio mas no la guarda'''
s_02=df4.rename(index={0:1,1:2,2:3,3:4},inplace=True)
'''Aqui se imprime la varibale anterior'''
print(df4)
print('------------------------------------------------------------------------------------')
'''Este comando cambia directamente los indixes de el data frame'''
print(df4.reindex(index=[1,2,300,400]))
print('------------------------------------------------------------------------------------')
'''Esta funcion permite eliminar una columna del data frame y guardarlo en un variable para su posterio uso'''
direccion=df4.pop('Direccion')
print(direccion)
print(df4)
print('------------------------------------------------------------------------------------')
'''Este comando se utiliza volver a guardar la columna eliminada en el data frame'''
df4['Direccion'] = direccion
print(df4)
print('------------------------------------------------------------------------------------')
'''Este comando no me permite guardar la columna en ningun lado'''
del df4['Direccion']
'''Este comando permite eliminar las filas que nosotros queramos pero hay que tener en cuenta que si hay un tipo de dato Nan dentro del registro tambien
eliminara'''
df4.dropna()
print('------------------------------------------------------------------------------------')
'''Este comando sirver para organizar de menor a mayor la columna que hemos escojido'''
print(df4.sort_values('Edad',ascending=True))
print('------------------------------------------------------------------------------------')
'''Este comando ordena el data frame a traves sus indices'''
print(df4.sort_index(ascending=True))
print('------------------------------------------------------------------------------------')
'''Este comando es para buscar un dato en particular en un data frame'''
print(df4[df4['Correo']=='josue@gmail.com'])
print('------------------------------------------------------------------------------------')
'''Este comando sirve para escojer un dato dentro del data frame teniendo en uenta el numero de columnas y filas'''
print(df4.iloc[1,1])
print('------------------------------------------------------------------------------------')
'''Con este comando podemos obtener un dato teniedo en cuenta la columna y la fila'''
print(df4.loc[1,'Genero'])
print('------------------------------------------------------------------------------------')
'''Mas operaciones que se pueden usar en un data frame'''
''' con este comando podemos contar auntos indices tiene el data frame'''
print(df4['Nombre'].count())
print('------------------------------------------------------------------------------------')
print(df4['Nombre'].cumsum())
print('------------------------------------------------------------------------------------')
print(df4['Edad'].mean())#La media
print(df4['Edad'].median())#La mediana
print(df4['Edad'].std())#Desviacion estandar
print('------------------------------------------------------------------------------------')
print(df4.describe())#Me devuelve el calculo de varios datos
print('------------------------------------------------------------------------------------')
print(df4.groupby (by='Edad').count())
print('------------------------------------------------------------------------------------')
print(df4.pivot(index='Nombre',columns='Edad',values='Correo'))
print('------------------------------------------------------------------------------------')