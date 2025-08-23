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
# Eliminar una reserva
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
# Mostrar todas las reservas
def mostrar_reservas():
    if not reservas:
        print("📂 No hay reservas registradas.\n")
    else:
        print("📚 Lista de reservas:")
        for r in reservas:
            print(f"Estudiante: {r[1]} ({r[0]}) - Libro: {r[3]} ({r[2]})")
        print()
