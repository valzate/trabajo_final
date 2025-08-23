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

