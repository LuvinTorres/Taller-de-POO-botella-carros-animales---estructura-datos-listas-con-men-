from Class_botellaPlastico import Botella_plastico
from Class_botellaVidrio import Botella_vidrio
from Clase_botella import Botella
from Base_Datos import Base_dato


def crear_botella():
    print("\n--- Crear botella ---")
    print("1. Botella de plástico")
    print("2. Botella de vidrio")
    tipo = input("Seleccione el tipo: ")

    material = input("Material: ")
    capacidad = input("Capacidad: ")
    forma = input("Forma: ")
    diseno = input("Diseño: ")

    if tipo == "1":
        peso = input("Peso: ")
        flexibilidad = input("Flexibilidad: ")
        return Botella_plastico(material, capacidad, forma, diseno, peso, flexibilidad)

    elif tipo == "2":
        resistencia_termica = input("Resistencia térmica: ")
        fragilidad = input("Fragilidad: ")
        return Botella_vidrio(material, capacidad, forma, diseno, resistencia_termica, fragilidad)

    else:
        print("Opción inválida.")
        return None


def main():
    bd = Base_dato()

    while True:
        print("\n--- MENU CRUD BOTELLAS ---")
        print("1. Agregar botella")
        print("2. Mostrar botellas")
        print("3. Actualizar botella")
        print("4. Eliminar botella")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            botella = crear_botella()
            if botella:
                print(bd.agregar_botella(botella))

        elif opcion == "2":
            print("\n--- Botellas registradas ---")
            bd.mostrar_botella()

        elif opcion == "3":
            bd.mostrar_botella()
            indice = int(input("Índice a actualizar: "))
            nueva = crear_botella()
            if nueva:
                bd.actualizar_botella(indice, nueva)
                print("Botella actualizada correctamente.")

        elif opcion == "4":
            bd.mostrar_botella()
            indice = int(input("Índice a eliminar: "))-1
            print(bd.eliminar_botella(indice))

        elif opcion == "5":
            break

        else:
            print("Opción inválida. Intente de nuevo.")


main()