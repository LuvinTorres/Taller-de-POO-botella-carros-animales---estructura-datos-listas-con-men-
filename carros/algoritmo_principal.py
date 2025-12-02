from carro_transporte import Carro_transporte
from carro_deportivo import Carro_deportivo
from carro_carga import Carro_carga
from data_base import Base_datos
from carro import Carro

bd = Base_datos()

def crear_carro():
    print("1. Carro normal")
    print("2. Carro de transporte")
    print("3. Carro deportivo")
    print("4. Carro de carga")

    tipo = input("Seleccione el tipo de carro: ")

    modelo = input("Modelo: ")
    color = input("Color: ")
    capacidad = input("Capacidad: ")
    tipo_comb = input("Tipo de combustible: ")

    if tipo == "1":
        carro = Carro(modelo, color, capacidad, tipo_comb)

    elif tipo == "2":
        ruta = input("Ruta: ")
        empresa = input("Empresa: ")
        carro = Carro_transporte(modelo, color, capacidad, tipo_comb, ruta, empresa)

    elif tipo == "3":
        vel_max = input("Velocidad máxima: ")
        suspencion = input("Suspención: ")
        carro = Carro_deportivo(modelo, color, capacidad, tipo_comb, vel_max, suspencion)

    elif tipo == "4":
        cap_carga = input("Capacidad de carga: ")
        tipo_carga = input("Tipo de carga: ")
        carro = Carro_carga(modelo, color, capacidad, tipo_comb, cap_carga, tipo_carga)

    else:
        print("Opción inválida.")
        return

    print(bd.agregar_carro(carro))


def eliminar_carro():
    modelo = input("Ingrese el modelo del carro a eliminar: ")
    print(bd.eliminar_carro(modelo))


def actualizar_carro():
    modelo = input("Modelo del carro a actualizar: ")
    nuevo_color = input("Nuevo color: ")
    print(bd.actualizar_carro(modelo, nuevo_color))


def mostrar_carros():
    if bd.total_carros() == 0:
        print("No hay carros registrados.")
        return

    print("\nLista de carros en la base de datos:")
    for carro in bd.lista_carros:
        print(f"- Modelo: {carro.modelo}, Color: {carro.color}, Capacidad: {carro.capacidad}, Combustible: {carro.tipo_combustible}")
    print()


def menu():
    while True:
        print("\n===== MENÚ CRUD =====")
        print("1. Agregar carro")
        print("2. Eliminar carro")
        print("3. Actualizar carro")
        print("4. Mostrar carros")
        print("5. Total de carros")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_carro()
        elif opcion == "2":
            eliminar_carro()
        elif opcion == "3":
            actualizar_carro()
        elif opcion == "4":
            mostrar_carros()
        elif opcion == "5":
            print(f"Total de carros: {bd.total_carros()}")
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción incorrecta.")

menu()