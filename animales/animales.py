class Animales:
    def __init__(self,nombre,habitat,tamaño,color):
        self.nombre= nombre
        self.habitat= habitat
        self.tamaño= tamaño
        self.color= color
        
    def moverse(self):
        return f"{self.nombre} se desplaza para buscar alimento o protegerse."
    
    def reproduccion(self):
        return f"{self.nombre} se reproduce para generar nuevas crias."
    
    def comunicacion(self):
        return f"{self.nombre} se comunica con sonidos, gestos o señales."
    
    def descanso(self):
        return f"{self.nombre} reduce su actividad para recuperarse."
    
    def adaptacion(self):
        return f"{self.nombre} desarrolla cambios para sobrevivir en su ambiente."