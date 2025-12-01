class BaseDatos:
    def __init__(self):
        self.lista_animales = []
    
    def agregar(self, animal):
        self.lista_animales.append(animal)
        return f" {animal.nombre} agregado exitosamente"
    
    def obtener_todos(self):
        return self.lista_animales
    
    def buscar(self, nombre):
        return [animal for animal in self.lista_animales if nombre.lower() in animal.nombre.lower()]
    
    def actualizar(self, indice, nuevo_animal):
        if 0 <= indice < len(self.lista_animales):
            self.lista_animales[indice] = nuevo_animal
            return f" {nuevo_animal.nombre} actualizado exitosamente"
        return " Índice inválido"
    
    def eliminar(self, indice):
        if 0 <= indice < len(self.lista_animales):
            nombre = self.lista_animales[indice].nombre
            del self.lista_animales[indice]
            return f" {nombre} eliminado exitosamente"
        return " Índice inválido"
    
    def contar(self):
        return len(self.lista_animales)