

class Botella:
    def __init__(self,material,capacidad,forma,diseno):
        self.material=material
        self.capacidad= capacidad
        self.forma= forma
        self.diseno= diseno
    
    def __str__(self):
        return(
            f"Material:{self.material}\n" 
            f"capacidad:{self.capacidad}\n"
            f"forma:{self.forma}\n"
            f"diseño:{self.diseno}"
        )
       
    def contener_liquidos(self):
        print("este tipo de material puede almacenar agua, jugo o otros liquidos sin fugas.")   
        
    def facilitar_vertido(self):
        print("su diseno permite vertir el contenido sin derramarlo.")
        
    def cierre_hermetico(self):
        print("la tapa evita que el liquido se derrame o se contamine.")
        
    def transporte(self):
        print("es facil de llevar gracias a su tamano y forma.")