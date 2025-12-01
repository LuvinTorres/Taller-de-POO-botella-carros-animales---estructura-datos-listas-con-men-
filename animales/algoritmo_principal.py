from animales import Animales
from caiman import Animal_caiman
from caballo import Animal_caballo
from escarabajo import Animal_escarabajo
from pato import Animal_pato
from pez import Animal_pez
from base_datos import BaseDatos

def mostrar_menu():
    print("\n--- MENU PRINCIPAL ---")
    print("1. Agregar animal")
    print("2. Ver todos los animales")
    print("3. Buscar animal")
    print("4. Eliminar animal")
    print("5. Salir")

def mostrar_tipos_animales():
    print("\nTipos de animales:")
    print("1. Caballo")
    print("2. Caiman")
    print("3. Escarabajo")
    print("4. Pato")
    print("5. Pez")

def crear_animal(tipo):
    nombre = input("Nombre: ")
    habitat = input("Habitat: ")
    tamaño = input("Tamaño: ")
    color = input("Color: ")
    
    if tipo == 1:
        edad = input("Edad: ")
        raza = input("Raza: ")
        return Animal_caballo(nombre, habitat, tamaño, color, edad, raza)
    
    elif tipo == 2:
        longitud = input("Longitud: ")
        temp = input("Temperatura: ")
        return Animal_caiman(nombre, habitat, tamaño, color, longitud, temp)
    
    elif tipo == 3:
        tipo_escarabajo = input("Tipo de escarabajo: ")
        antenas = input("Numero de antenas: ")
        return Animal_escarabajo(nombre, habitat, tamaño, color, tipo_escarabajo, antenas)
    
    elif tipo == 4:
        plumaje = input("Tipo de plumaje: ")
        alas = input("Envergadura de alas: ")
        return Animal_pato(nombre, habitat, tamaño, color, plumaje, alas)
    
    elif tipo == 5:
        profundidad = input("Profundidad maxima: ")
        agua = input("Tipo de agua: ")
        return Animal_pez(nombre, habitat, tamaño, color, profundidad, agua)

def mostrar_animal(animal, numero=None):
    if numero is not None:
        print(f"\nAnimal #{numero}:")
    print(f"Nombre: {animal.nombre}")
    print(f"Tipo: {type(animal).__name__}")
    print(f"Habitat: {animal.habitat}")
    print(f"Tamaño: {animal.tamaño}")
    print(f"Color: {animal.color}")

def main():
    db = BaseDatos()
    
    print("Bienvenido al Sistema de Animales")
    
    while True:
        mostrar_menu()
        opcion = input("\nElige una opcion: ")
        
        if opcion == "1":
            mostrar_tipos_animales()
            try:
                tipo = int(input("\nElige el tipo (1-5): "))
                if 1 <= tipo <= 5:
                    animal = crear_animal(tipo)
                    resultado = db.agregar(animal)
                    print(resultado)
                else:
                    print("Tipo no valido")
            except:
                print("Error: ingresa un numero")
        
        elif opcion == "2":
            animales = db.obtener_todos()
            if animales:
                print(f"\nTotal de animales: {len(animales)}")
                for i, animal in enumerate(animales, start= 1):
                    mostrar_animal(animal, i)
            else:
                print("No hay animales registrados")
        
        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            resultados = db.buscar(nombre)
            if resultados:
                for animal in resultados:
                    mostrar_animal(animal)
            else:
                print("No se encontraron animales")
        
        elif opcion == "4":
            animales = db.obtener_todos()
            if animales:
                print("\nAnimales disponibles:")
                for i, animal in enumerate(animales):
                    print(f"[{i}] {animal.nombre}")
                
                try:
                    indice = int(input("\nNumero del animal a eliminar: "))
                    resultado = db.eliminar(indice)
                    print(resultado)
                except:
                    print("Numero no valido")
            else:
                print("No hay animales para eliminar")
        
        elif opcion == "5":
            print("Adios")
            break
        
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()