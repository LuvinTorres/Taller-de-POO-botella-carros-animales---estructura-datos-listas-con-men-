from animales import Animales

class Animal_escarabajo(Animales):
    def __init__(self, nombre, habitat, tamaño, color, tipo_escarabajo, numero_antena):
        super().__init__(nombre, habitat, tamaño, color)
        
        self.tipo_escarabajo=tipo_escarabajo
        self.numero_antena= numero_antena
        
    def volar(self):
        return f"el escarabajo {self.nombre} esta volando."   
    
    def escalar(self):
        return f"el escarabajo {self.nombre}esta escalando una rama con facilidad." 
    
    def rodar_bola(self):
        return f" el escarabajo {self.nombre} rueda una bola de tierra."
    
    def enterrarse(self):
        return f"el escarabajo  {self.nombre} se entierra para protegerse."