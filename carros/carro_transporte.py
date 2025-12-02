from carro import Carro

class Carro_transporte(Carro):
    def __init__(self, modelo, color, capacidad, tipo_combustible, ruta, empresa):
        super().__init__(modelo, color, capacidad, tipo_combustible)
        
        self.ruta=ruta
        self.empresa=empresa
        
    def iniciar_ruta(self):
        return f"el transporte {self.modelo} ha iniciado la ruta {self.ruta}."
    
    def detener_transporte(self):
        return f"el transporte {self.modelo} ha detendio su recorrido."   