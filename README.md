<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>README - Proyecto de Estructuras de Datos</title>
</head>
<body>
  <h1>📘 Proyecto de Estructuras de Datos</h1>

  <h2>📌 Descripción</h2>
  <p>
    Este repositorio contiene la implementación de un sistema diseñado para 
    manejar datos de manera eficiente y escalable de una biblioteca de una universidad. El enfoque principal 
    ha sido optimizar el rendimiento en las operaciones: 
        - inserción 
        - búsqueda 
        - eliminación.
  </p>

  <h2>⚙️ Justificación Estructura de datos</h2>
  <p>
    Se eligio hacer una matriz enlazada para acomodar estos datos de una manera
    que fuera más fácil el guardar/insertar, buscar y eliminar los datos segun sea
    necesario, ya que este también lo acomoda de un a buena manera
    y los datos quedan bien organizados
  </p>

  <h2>🚀 Resultados de Pruebas de Rendimiento</h2>
  <h3>--- Escenario con 10 reservas ---</h3>
  <ul>
    <li>Inserción de 10 reservas: 0.000029 segundos</li>
    <li>Búsqueda de un estudiante: 0.000011 segundos</li>
    <li>Eliminación de una reserva: 0.000014 segundos</li>
  </ul>
  <h3>--- Escenario con 100 reservas ---</h3>
  <ul>
    <li>Inserción de 100 reservas: 0.000105 segundos</li>
    <li>Búsqueda de un estudiante: 0.000011 segundos</li>
    <li>Eliminación de una reserva: 0.000012 segundos</li>
  </ul>
  <h3>--- Escenario con 1000 reservas ---</h3>
  <ul>
    <li>Inserción de 10 reservas: 0.000604 segundos</li>
    <li>Búsqueda de un estudiante: 0.000047 segundos</li>
    <li>Eliminación de una reserva: 0.000083 segundos</li>
  </ul>
  <p>
    Las pruebas demuestran que el sistema mantiene un rendimiento 
    estable incluso con volúmenes moderados de datos.
  </p>

  <h2>📈 Conclusiones sobre Escalabilidad</h2>
  <p>
    El sistema es <strong>escalable</strong> para esta biblioteca universitaria que 
    requieren inserciones y eliminaciones frecuentes. Sin embargo, 
    debido a la naturaleza secuencial de las búsquedas en las matrices enlazadas, 
    si se presentan duplicados pueden haber perdida de datos. 
    Para sistemas  solucionar esto se podria hacer una tablas hash.
  </p>

  <h2>📝 Autor</h2>
  <p>
    <strong>Vania Andrea Alzate Gómez<strong/>
  </p>
</body>
</html>
