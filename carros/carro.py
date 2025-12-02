class Carro:
    def __init__(self,modelo,color,capacidad,tipo_combustible):
        self.modelo=modelo
        self.color=color
        self.capacidad=capacidad
        self.tipo_combustible=tipo_combustible
        
    def arranque(self):
       return f"el carro{self.modelo} esta arrancando." 
   
    def apagado(self):
       return f"el carro{self.modelo} ha sido apagado." 
 
    def sistema_de_direccion(self):
       return f"el sistema de direccion ha sido activado." 
        
    def luces(self):
       return f"las luces del carro {self.modelo} estan encendidas." 
                