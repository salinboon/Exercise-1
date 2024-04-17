import numpy as np 
class juego_de_pila:
    def __init__(self) :
        self.numbers=list(np.random.randint(1,21,size=20))
        self.numbers_delete=int(input('Digite el numero de elementos que se van a eliminar de la pila '))
    
    def elementos_eliminados(self):
        print(self.numbers)
        cont=0
        lista1=[]
        while self.numbers_delete>cont:
            lista_=self.numbers.pop()
            lista1.append(lista_)
            cont+=1
        return lista1   
    
    def sum_of_elements(self,s):
        a=sum(s)
        return a

    def puntuacion_final(self,a):
        calificacion=10
        if a>50:
            return 'Perdiste el juego'
        else:
            calificacion=calificacion-self.numbers_delete
            return 'Ganaste el juego su calificacion es',calificacion   



h=juego_de_pila()
s=h.elementos_eliminados()
print(s)
a=h.sum_of_elements(s)
print('Su puntaje es ',a)
print(h.puntuacion_final(a))




        