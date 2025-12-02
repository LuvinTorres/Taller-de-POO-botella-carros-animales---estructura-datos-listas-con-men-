from Clase_botella import Botella

class Botella_plastico(Botella):
    def __init__(self,material, capacidad,forma,diseno, peso, flexibilidad):
        super().__init__(material,capacidad,forma,diseno)
        
        self.peso=peso
        self.flexibilidad=flexibilidad
            
    def reutilizacion(self):
        print("la botella plastica puede reutilizarse pocas veces antes de reciclarse.")      
        
    def reciclaje(self):
        print("debe depositarse en su contenedor respectivo para reciclarse.")      
        
    def deformar(self):
        print("la botella de plastico se puede deformar si se expone mucho tiempo al calor.")            