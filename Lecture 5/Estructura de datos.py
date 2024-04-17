class Estructura_pila():
    def __init__(self):
        self.__list=[]
    #Agregar un elemnto a la pila
    def push(self,item):
        self.__list.append(item)
    #Quitar el ultimo elemnto de la pila
    def pop(self,item):
       return self.__list.pop()
    #Obetener el elemnto superior de la lista
    def peek(self):
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        return self.__list==[] 
          
pila=Estructura_pila()
print(pila.is_empty())
        