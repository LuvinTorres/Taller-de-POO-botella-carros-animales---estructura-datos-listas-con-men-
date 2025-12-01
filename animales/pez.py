from animales import Animales

class Animal_pez(Animales):
    def __init__(self, nombre, habitat, tamaño, color, profundidad_maxima, tipo_agua):
        super().__init__(nombre, habitat, tamaño, color)
        
        self.profundidad_maxima=profundidad_maxima
        self.tipo_agua= tipo_agua
        
    def nadar_rapido(self):
        return f"el pez {self.nombre} esta nadando rapidamente."   
    
    def saltar_fuera_del_agua(self):
        return f"el pez {self.nombre} salta fuera del agua haciendo giros." 
    
    def esconderse(self):
        return f" el pez {self.nombre} se esconde entre los corales."
    
    