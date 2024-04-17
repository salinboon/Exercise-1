class arbol_binario:
  def __init__(self,dato):
    self.dato=dato
    self.left=None
    self.right=None

  def insert_Val(self,dato:int):
      arbol_binario(dato)

  def busca_Val(self,val):
    if self.dato==val:
      print(h.verVal(val))
      return True
    elif self.dato!=val:
      print(h.verVal(val))
      return False

  def verVal(self,val):
    if val==self.dato:
      print('Dato encontrado')
      return self.dato
    else:
      print('Dato no encontrado')
      return self.dato
  
  
h=arbol_binario(5)
h.busca_Val(5)
h.busca_Val(4)
h.busca_Val(5)
h.busca_Val(7)