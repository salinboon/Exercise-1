#2) Implementar un juego donde constas de 2 jarras, de capacidad 5 y 3 litros respectivamente, y debes colocar 4 litros en la jarra de 5L.
#Las opciones posibles son:
#* Llenar la jarra de 3 litros
#* Llenar la jarra de 5 litros
#* Vaciar la jarra de 3 litros
#* Vaciar la jarra de 5 litros
#* Verter el contenido de la jarra de 3 litros en la de 5 litros
#* Verter el contenido de la jarra de 5 litros en la de 3 litros

class play_of_jar:
   def __init__(self):
      self.desire=int(input('Que funcion quieres ejecutar\n'
                        '1.fill_the_jar_of_3_liters \n'
                        '2.fill_the_jar_of_5_liters\n'
                        '3.empty_the_jar_of_3_liters\n'
                        '4.empty_the_jar_of_5_liters\n'
                        '5.pour_the_content_of_3_liters_in_the_of_5_liters\n'
                        '6.pour_the_content_of_jar_of_5_liters_in_the_of_3_liters\n'))
      if self.desire==1:
       print(self.fill_the_jar_of_3_liters())
      elif self.desire==2:
        self.fill_the_jar_of_5_liters()
      elif self.desire==3:
        self.empty_the_jar_of_3_liters()
      elif self.desire==4:
        self.empty_the_jar_of_5_liters()
      elif self.desire==5:
        self.pour_the_content_of_3_liters_in_the_of_5_liters()
      elif self.desire==6:
        self.pour_the_content_of_jar_of_5_liters_in_the_of_3_liters()   
              
   
   def fill_the_jar_of_3_liters(self):
      return 'filling the jar of 3 liters'

   def fill_the_jar_of_5_liters(self):
      return 'filling the jar of 5 liters'

   def empty_the_jar_of_3_liters(self):
      return 'filling the jar of 5 liters'

   def empty_the_jar_of_5_liters(self):
      return 'filling the jar of 5 liters'

   def pour_the_content_of_3_liters_in_the_of_5_liters(self):
      return 'filling the jar of 5 liters'
    
   def pour_the_content_of_jar_of_5_liters_in_the_of_3_liters(self):
      return'filling the jar of 5 liters'  

h=play_of_jar()
print(h)