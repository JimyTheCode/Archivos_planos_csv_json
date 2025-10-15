import csv
import os
import pandas as pd
from tabulate2 import tabulate


archivo = "Datos_aprendiz.csv"
encabezados = ["Nombre", "Apellidos", "Direccion", "Telefono", "Ficha"]


def crear_archivo():
    if not os.path.exists(archivo):
        with open(archivo, mode="w", newline="", encoding="utf-8") as file:
            escritor = csv.writer(file)
            escritor.writerow(encabezados)
        print("Archivo creado correctamente.")


def agregar_aprendiz():
    while True:
        print("\n--- AGREGAR NUEVO APRENDIZ ---")
        nombre = input("Ingrese el Nombre del aprendiz: ").strip()
        apellido = input("Ingrese el Apellido del aprendiz: ").strip()
        direccion = input("Ingrese la Direccion del aprendiz: ").strip()
        telefono = input("Ingrese el Telefono del aprendiz: ").strip()
        ficha = input("Ingrese el número de Ficha del aprendiz: ").strip()

        confirmar = input("¿Desea guardar este registro? (s/n): ")
        if confirmar.lower() == "s":
            with open(archivo, mode="a", newline="", encoding="utf-8") as file:
                escritor = csv.writer(file)
                escritor.writerow([nombre, apellido, direccion, telefono, ficha])
            print("Datos guardados correctamente.")
        else:
            print("Registro descartado.")

        continuar = input("¿Desea agregar otro aprendiz? (s/n): ")
        if continuar.lower() != "s":
            break


def leer_aprendices():
    if not os.path.exists(archivo):
        print("No existe el archivo de datos.")
        return

    df = pd.read_csv(archivo)

    if df.empty:
        print("No hay aprendices registrados.")
        return

    print("\nLISTADO COMPLETO DE APRENDICES:\n")
    print(tabulate(df, headers="keys", tablefmt="fancy_grid", showindex=False))


def actualizar_aprendiz():
    if not os.path.exists(archivo):
        print("No existe el archivo de datos.")
        return

    ficha_buscar = input("\nIngrese el número de ficha del aprendiz a actualizar: ").strip()

    registros = []
    encontrado = False

    with open(archivo, mode="r", encoding="utf-8") as file:
        lector = csv.DictReader(file)
        for fila in lector:
            if fila["Ficha"] == ficha_buscar:
                encontrado = True
                print(f"\nAprendiz encontrado: {fila['Nombre']} {fila['Apellidos']}")
                fila["Nombre"] = input(f"Nuevo Nombre ({fila['Nombre']}): ") or fila["Nombre"]
                fila["Apellidos"] = input(f"Nuevos Apellidos ({fila['Apellidos']}): ") or fila["Apellidos"]
                fila["Direccion"] = input(f"Nueva Direccion ({fila['Direccion']}): ") or fila["Direccion"]
                fila["Telefono"] = input(f"Nuevo Telefono ({fila['Telefono']}): ") or fila["Telefono"]
                fila["Ficha"] = input(f"Nuevo número de Ficha ({fila['Ficha']}): ") or fila["Ficha"]

                confirmar = input("¿Desea guardar los cambios? (s/n): ")
                if confirmar.lower() != "s":
                    print("⚠Cambios descartados.")
            registros.append(fila)

    if not encontrado:
        print("No se encontró ningún aprendiz con esa ficha.")
        return

    with open(archivo, mode="w", newline="", encoding="utf-8") as file:
        escritor = csv.DictWriter(file, fieldnames=encabezados)
        escritor.writeheader()
        escritor.writerows(registros)

    if encontrado:
        print("Datos actualizados correctamente.")


def menu():
    crear_archivo()

    while True:
        print("\n========= MENÚ PRINCIPAL =========")
        print("1. Agregar aprendiz")
        print("2. Leer aprendices")
        print("3. Actualizar aprendiz")
        print("4. Salir")
        print("==================================")

        opcion = input("Seleccione una opción (Solo numeros del 1 al 4): ")

        if opcion == "1":
            agregar_aprendiz()
        elif opcion == "2":
            leer_aprendices()
        elif opcion == "3":
            actualizar_aprendiz()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
