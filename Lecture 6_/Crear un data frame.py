import pandas as pd  
s=open('Emisiones_CO2.CSV','r')
next(s)
lista=[]
columnas=['Codigo de pais','Nombre del pais','Region','Año','CO2(kt)','CO2 per capita (toneladas metricas)']
lista1=[]

for i in s:
  a=i.strip()
  a=i.split('|')
  lista.append(a)
w=pd.DataFrame(data=lista,columns=columnas)
w1=w.replace('\n','',regex=True)
w1=w.drop(['CO2(kt)','CO2 per capita (toneladas metricas)'],axis=1)
print(w1)
new_data={'Clave_Hash':lista1}
 
def hash_function(key):
    return sum(index * ord(character) for index, character in enumerate(repr(key), start=1))

for indices, i in w1['Codigo de pais'].items():
    lista1.append(hash_function(i))
w1['Clave_Hash'] = lista1
w1



   

































