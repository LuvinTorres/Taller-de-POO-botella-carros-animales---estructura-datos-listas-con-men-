class Base_datos:
    def __init__(self):
        self.lista_carros=[]
        
    def agregar_carro(self, nuevo_carro):
        self.lista_carros.append(nuevo_carro)
        return "carro agregado correctamente."
        
    def eliminar_carro(self, modelo):
        for indice,carro in enumerate(self.lista_carros):
            if carro.modelo== modelo:
                self.lista_carros.pop(indice)
                return f"el carro con modelo '{modelo}' ha sido eliminado."
        return f"no se encontro el carro con el modelo '{modelo}'"  
    
    def total_carros(self):
        return len(self.lista_carros)
    
    def actualizar_carro(self,modelo,nuevo_color=None):
        for carro in self.lista_carros:
            if carro.modelo == modelo:
                if nuevo_color:
                    carro.color=nuevo_color
                    return f"carro '{modelo}'actualizado."
        return f"no se encontro el modelo '{modelo}."
        