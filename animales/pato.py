from animales import Animales

class Animal_pato(Animales):
    def __init__(self, nombre, habitat, tamaño, color, tipo_plumaje, envergadura_alas ):
        super().__init__(nombre, habitat, tamaño, color)
        
        self.tipo_plumaje=tipo_plumaje
        self.envergadura_alas= envergadura_alas
        
    def nadar(self):
        return f"el pato {self.nombre} esta nadando tranquilamente."   
    
    def graznar(self):
        return f"el pato {self.nombre} emite un fuerte graznido." 
    
    def volar(self):
        return f" el pato {self.nombre} abre sus alas y comienza a volar."