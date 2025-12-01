from animales import Animales

class Animal_caballo(Animales):
    def __init__(self, nombre, habitat, tamaño, color, edad, raza):
        super().__init__(nombre, habitat, tamaño, color)
        
        self.edad=edad
        self.raza=raza
        
    def relinchar(self):
        return f"el caballo {self.nombre} esta relinchando."   
    
    def galopar(self):
        return f"el caballo {self.nombre} esta galopando rapidamente." 
    
    def beber_agua(self):
        return f"el caballo {self.nombre} esta bebiendo agua del abrevadero."
    
    def correr (self):
        return f"el caballo {self.nombre} corre con gran velocidad."
    