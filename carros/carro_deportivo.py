from carro import Carro

class Carro_deportivo(Carro):
    def __init__(self, modelo, color, capacidad, tipo_combustible, velocidad_maxima,suspencion):
        super().__init__(modelo, color, capacidad, tipo_combustible)
        
        self.velocidad_maxima=velocidad_maxima
        self.suspencion=suspencion
        
    def modo_sport(self):
        return "el modo sport ha sido activado."
    
    def mostrar_velocidad_maxima(self):
        return f"la velocidad maxima es {self.velocidad_maxima}km/h."   