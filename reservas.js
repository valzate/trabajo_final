const prompt = require("prompt-sync")(); // Para poder ingresar los datos por cosola 

let reservas = [];
// Ingresar una nueva reserva
function ingresarReserva() {
  const codigoEstudiante = prompt("Código del estudiante: ");
  const nombreEstudiante = prompt("Nombre del estudiante: ");
  const codigoLibro = prompt("Código del libro: ");
  const nombreLibro = prompt("Nombre del libro: ");

  reservas.push([codigoEstudiante, nombreEstudiante, codigoLibro, nombreLibro]);
  console.log("✅ Reserva agregada correctamente.\n");
}
