from animales import Animales

class Animal_caiman(Animales):
    def __init__(self, nombre, habitat, tamaño, color, longitud,temperatura_corporal):
        super().__init__(nombre, habitat, tamaño, color)
        
        self.longitud=longitud
        self.temperatura_corporal=temperatura_corporal
        
    def nadar(self):
        return f"el caiman{self.nombre} esta nadando sigilosamente."   
    
    def tomar_sol(self):
        return f"el caiman {self.nombre} esta tomando el sol para regular su temperatura." 
    
    def atacar(self):
        return f"el caiman {self.nombre} realiza un ataque rapido desde el agua."
    
    def hacer_sonido(self):
        return f"el caiman {self.nombre} emite un gruñido grave."
    