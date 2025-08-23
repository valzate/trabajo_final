const prompt = require("prompt-sync")(); // Para poder ingresar los datos por cosola 

let reservas = [];
// Función para ingresar una nueva reserva
function ingresarReserva() {
  const codigoEstudiante = prompt("Código del estudiante: ");
  const nombreEstudiante = prompt("Nombre del estudiante: ");
  const codigoLibro = prompt("Código del libro: ");
  const nombreLibro = prompt("Nombre del libro: ");

  reservas.push([codigoEstudiante, nombreEstudiante, codigoLibro, nombreLibro]);
  console.log("✅ Reserva agregada correctamente.\n");
}
// Función para buscar por código de estudiante o código de libro
function buscarReserva() {
  const opcion = prompt("Buscar por Estudiante (1) o Buscar por Libro (2):  ");

  if (opcion === "1") {
    const codigoEstudiante = prompt("Ingrese el código del estudiante: ");
    const encontrados = reservas.filter(r => r[0] === codigoEstudiante);

    if (encontrados.length > 0) {
      console.log("🔎 Resultados:");
      encontrados.forEach(r =>
        console.log(`Estudiante: ${r[1]} - Libro: ${r[3]} (${r[2]})`)
      );
    } else {
      console.log("⚠️ No se encontró ninguna reserva para ese estudiante.");
    }
  } else if (opcion === "2") {
    const codigoLibro = prompt("Ingrese el código del libro: ");
    const encontrados = reservas.filter(r => r[2] === codigoLibro);

    if (encontrados.length > 0) {
      console.log("🔎 Resultados:");
      encontrados.forEach(r =>
        console.log(`Libro: ${r[3]} - Estudiante: ${r[1]} (${r[0]})`)
      );
    } else {
      console.log("⚠️ No se encontró ninguna reserva para ese libro.");
    }
  } else {
    console.log("⚠️ Opción inválida.");
  }
  console.log();
}
// Función para eliminar una reserva
function eliminarReserva() {
  const codigoEstudiante = prompt("Código del estudiante: ");
  const codigoLibro = prompt("Código del libro: ");

  const indice = reservas.findIndex(
    r => r[0] === codigoEstudiante && r[2] === codigoLibro
  );

  if (indice !== -1) {
    reservas.splice(indice, 1);
    console.log("🗑️ Reserva eliminada correctamente.\n");
  } else {
    console.log("⚠️ No se encontró ninguna reserva con esos datos.\n");
  }
}

// M
// Función para mostrar todas las reservas de ser necesario
function mostrarReservas() {
  if (reservas.length === 0) {
    console.log("📂 No hay reservas registradas.\n");
  } else {
    console.log("📚 Lista de reservas:");
    reservas.forEach(r =>
      console.log(
        `Estudiante: ${r[1]} (${r[0]}) - Libro: ${r[3]} (${r[2]})`
      )
    );
    console.log();
  }
}
// Menú interactivo

function menu() {
  let opcion = "";
  while (opcion !== "5") {
    console.log("====== MENÚ RESERVAS ======");
    console.log("1. Ingresar reserva");
    console.log("2. Buscar reserva");
    console.log("3. Eliminar reserva");
    console.log("4. Mostrar todas las reservas");
    console.log("5. Salir");
    opcion = prompt("Seleccione una opción: ");

    switch (opcion) {
      case "1":
        ingresarReserva();
        break;
      case "2":
        buscarReserva();
        break;
      case "3":
        eliminarReserva();
        break;
      case "4":
        mostrarReservas();
        break;
      case "5":
        console.log("👋 Saliendo del sistema...");
        break;
      default:
        console.log("⚠️ Opción inválida.\n");
    }
  }
}
// Ejecutar el menú
menu();