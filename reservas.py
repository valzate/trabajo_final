# Matriz doblemente anidada
reservas = []
# Función para agresar una nueva reserva
def ingresar_reserva():
    cod_est = input("Código del estudiante: ")
    nom_est = input("Nombre del estudiante: ")
    cod_lib = input("Código del libro: ")
    nom_lib = input("Nombre del libro: ")

    reservas.append([cod_est, nom_est, cod_lib, nom_lib])
    print("✅ Reserva agregada correctamente.\n")
# Función para buscar una reserva
def buscar_reserva():
    print("Buscar por:")
    print("1. Código de estudiante")
    print("2. Código de libro")
    opcion = input("Seleccione opción: ")

    if opcion == "1":
        cod_est = input("Ingrese código del estudiante: ")
        encontrados = [r for r in reservas if r[0] == cod_est]
    elif opcion == "2":
        cod_lib = input("Ingrese código del libro: ")
        encontrados = [r for r in reservas if r[2] == cod_lib]
    else:
        print("⚠️ Opción inválida.\n")
        return

    if encontrados:
        print("🔎 Resultados:")
        for r in encontrados:
            print(f"Estudiante: {r[1]} ({r[0]}) - Libro: {r[3]} ({r[2]})")
    else:
        print("⚠️ No se encontraron registros.")
    print()
# Función para eliminar una reserva
def eliminar_reserva():
    cod_est = input("Código del estudiante: ")
    cod_lib = input("Código del libro: ")

    indice = -1
    for i, r in enumerate(reservas):
        if r[0] == cod_est and r[2] == cod_lib:
            indice = i
            break

    if indice != -1:
        reservas.pop(indice)
        print("🗑️ Reserva eliminada correctamente.\n")
    else:
        print("⚠️ No se encontró esa reserva.\n")
# Funcion para mostrar todas las reservas de ser necesario
def mostrar_reservas():
    if not reservas:
        print("📂 No hay reservas registradas.\n")
    else:
        print("📚 Lista de reservas:")
        for r in reservas:
            print(f"Estudiante: {r[1]} ({r[0]}) - Libro: {r[3]} ({r[2]})")
        print()
# Menú interactivo
def menu():
    opcion = ""
    while opcion != "5":
        print("====== MENÚ RESERVAS ======")
        print("1. Ingresar reserva")
        print("2. Buscar reserva")
        print("3. Eliminar reserva")
        print("4. Mostrar todas las reservas")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_reserva()
        elif opcion == "2":
            buscar_reserva()
        elif opcion == "3":
            eliminar_reserva()
        elif opcion == "4":
            mostrar_reservas()
        elif opcion == "5":
            print("👋 Saliendo del sistema...")
        else:
            print("⚠️ Opción inválida.\n")
# Ejecutar el programa
menu()
import time
def ingresar_reserva(cod_est, nom_est, cod_lib, nom_lib):
    reservas.append([cod_est, nom_est, cod_lib, nom_lib])

def buscar_reserva(cod_est=None, cod_lib=None):
    if cod_est:
        return [r for r in reservas if r[0] == cod_est]
    elif cod_lib:
        return [r for r in reservas if r[2] == cod_lib]
    return []

def eliminar_reserva(cod_est, cod_lib):
    for i, r in enumerate(reservas):
        if r[0] == cod_est and r[2] == cod_lib:
            reservas.pop(i)
            return True
    return False
def probar_escenario(n):
    global reservas
    reservas = []  # Reiniciar lista

    print(f"\n--- Escenario con {n} reservas ---")

    # Medir tiempo de inserción
    inicio = time.time()
    for i in range(n):
        ingresar_reserva(f"E{i}", f"Estudiante{i}", f"L{i}", f"Libro{i}")
    fin = time.time()
    print(f"Inserción de {n} reservas: {fin - inicio:.6f} segundos")

    # Medir tiempo de búsqueda (último registro = peor caso)
    inicio = time.time()
    buscar_reserva(cod_est=f"E{n-1}")
    fin = time.time()
    print(f"Búsqueda de un estudiante: {fin - inicio:.6f} segundos")

    # Medir tiempo de eliminación (último registro = peor caso)
    inicio = time.time()
    eliminar_reserva(f"E{n-1}", f"L{n-1}")
    fin = time.time()
    print(f"Eliminación de una reserva: {fin - inicio:.6f} segundos")


# Ejecutar pruebas

for cantidad in [10, 100, 1000]:
    probar_escenario(cantidad) 