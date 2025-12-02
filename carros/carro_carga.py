from carro import Carro

class Carro_carga(Carro):
    def __init__(self, modelo, color, capacidad, tipo_combustible, capacidad_carga, tipo_carga):
        super().__init__(modelo, color, capacidad, tipo_combustible)
        
        self.capacidad_carga=capacidad_carga
        self.tipo_carga= tipo_carga
        
    def cargar(self):
        return f"el carro esta cargando {self.tipo_carga}"
    
    def descargar(self):
        return f"el carro ha descargado la mercancia."   