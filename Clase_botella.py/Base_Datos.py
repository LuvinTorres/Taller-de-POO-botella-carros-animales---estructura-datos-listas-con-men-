class Base_dato:
    def __init__(self):
        self.lista_botellas=[]
        
    def agregar_botella(self, obj_botella):
        self.lista_botellas.append(obj_botella)
        return "botella agregada correctamente."
    
    def actualizar_botella(self, indice, nueva_botella):
        if 0 <= indice < len(self.lista_botellas):
            self.lista_botellas[indice]= nueva_botella
                  
    def eliminar_botella(self, indice):
        if 0 <= indice < len(self.lista_botellas):
            self.lista_botellas.pop(indice)
        return "botella eliminada correctamente."  
    
    def mostrar_botella(self):
        if not self.lista_botellas:
            print("no hay botellas registradas")
            return
        
        for indice, botella in enumerate(self.lista_botellas):
            print(f"{indice + 1}.{botella}")

                                     