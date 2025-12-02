from Clase_botella import Botella

class Botella_vidrio(Botella):
    def __init__(self,material,capacidad,forma,diseno, resistencia_termica, fragilidad):
        super().__init__(material, capacidad,forma,diseno)
        self.resistencia_termica=resistencia_termica
        self.fragilidad=fragilidad
         
            
    def esterilizar(self):
        print("la botella de vidrio se puede esterilizar con agua caliente.")      
        
    def enfriar(self):
        print("la botella de vidrio puede mantener el liquido frio por mas tiempo.")      
        
    def romper(self):
        print("cuidado, la botella de vidrio se puede romper si se cae.")    