#JSON
import json
import os

ARCHIVO = "aprendices.json"

def cargar_datos():
    """Carga los datos del archivo JSON o devuelve una lista vacía si no existe."""
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_datos(aprendices):
    """Guarda la lista de aprendices en el archivo JSON."""
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(aprendices, f, indent=4, ensure_ascii=False)


def mostrar_aprendices(aprendices):
    """Muestra el listado completo de aprendices."""
    if not aprendices:
        print("\nNo hay aprendices registrados.\n")
        return
    print("\nLISTA DE APRENDICES:\n")
    for i, a in enumerate(aprendices, start=1):
        print(f"{i}. Nombre: {a['nombre']} {a['apellidos']}")
        print(f" Dirección: {a['direccion']}")
        print(f" Teléfono: {a['telefono']}")
        print(f" Ficha: {a['ficha']}")
        print("-" * 40)

def crear_aprendiz(aprendices):
    print("\nAgregar nuevo aprendiz:")
    nombre = input("Nombre: ").strip()
    apellidos = input("Apellidos: ").strip()
    direccion = input("Dirección: ").strip()
    telefono = input("Teléfono: ").strip()
    ficha = input("Ficha: ").strip()

    aprendiz = {
        "nombre": nombre,
        "apellidos": apellidos,
        "direccion": direccion,
        "telefono": telefono,
        "ficha": ficha
    }

    aprendices.append(aprendiz)
    guardar_datos(aprendices)
    print("\nAprendiz agregado con éxito.\n")


def leer_aprendices(aprendices):
    mostrar_aprendices(aprendices)


def actualizar_aprendiz(aprendices):
    mostrar_aprendices(aprendices)
    if not aprendices:
        return

    try:
        indice = int(input("\nIngrese el número del aprendiz a actualizar: ")) - 1
        if indice < 0 or indice >= len(aprendices):
            print("Número inválido.")
            return

        aprendiz = aprendices[indice]
        print("\nIngrese los nuevos datos (presione Enter para mantener los actuales):")
        aprendiz["nombre"] = input(f"Nombre ({aprendiz['nombre']}): ") or aprendiz["nombre"]
        aprendiz["apellidos"] = input(f"Apellidos ({aprendiz['apellidos']}): ") or aprendiz["apellidos"]
        aprendiz["direccion"] = input(f"Dirección ({aprendiz['direccion']}): ") or aprendiz["direccion"]
        aprendiz["telefono"] = input(f"Teléfono ({aprendiz['telefono']}): ") or aprendiz["telefono"]
        aprendiz["ficha"] = input(f"Ficha ({aprendiz['ficha']}): ") or aprendiz["ficha"]

        guardar_datos(aprendices)
        print("\nAprendiz actualizado correctamente.\n")

    except ValueError:
        print("Entrada inválida.")


def eliminar_aprendiz(aprendices):
    mostrar_aprendices(aprendices)
    if not aprendices:
        return

    try:
        indice = int(input("\nIngrese el número del aprendiz a eliminar: ")) - 1
        if indice < 0 or indice >= len(aprendices):
            print("Número inválido.")
            return

        eliminado = aprendices.pop(indice)
        guardar_datos(aprendices)
        print(f"\nAprendiz '{eliminado['nombre']} {eliminado['apellidos']}' eliminado con éxito.\n")

    except ValueError:
        print("Entrada inválida.")


def menu():
    aprendices = cargar_datos()

    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Agregar aprendiz")
        print("2. Ver aprendices")
        print("3. Actualizar aprendiz")
        print("4. Eliminar aprendiz")
        print("5. Salir")

        opcion = input("Seleccione una opción(Solo numeros del 1 al 5"
                       "): ")

        if opcion == "1":
            crear_aprendiz(aprendices)
        elif opcion == "2":
            leer_aprendices(aprendices)
        elif opcion == "3":
            actualizar_aprendiz(aprendices)
        elif opcion == "4":
            eliminar_aprendiz(aprendices)
        elif opcion == "5":
            print("\n Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    menu()
