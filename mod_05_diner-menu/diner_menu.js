// Bottega Diner Menu System

// Elegir el tipo de menú (desayuno, comida, cena) en función de la hora que introduzcamos, admitir formatos hh:mm y hh
// Cada menú debe tener 3 platos principales, 3 secundarios y 3 postres, con sus precios
// Si el usuario escribe mal el nombre, volver a preguntar.
// Admitir los nombres con mayúsculas, minúsculas, con o sin tilde
// Mostar un comentario aleatorio para cada plato elegido, que sea obtenido de un listado global de comentarios
// Mostar un resumen del pedido con los precios unitarios y el precio del conjunto del menú

// Horarios 
const horarios = {
  desayuno: { inicio: 7, fin: 11 }, // 7:00 - 11:59
  comida: { inicio: 12, fin: 16 },  // 12:00 - 16:59
  cena: { inicio: 17, fin: 23 }     // 17:00 - 23:59
};

// Opciones para desayuno, comida y cena
const menu = {
  desayuno: {
    principales: [
      { nombre: "Tortitas", precio: 4.99 },
      { nombre: "Huevos", precio: 5.99 },
      { nombre: "Tostadas", precio: 6.99 }
    ],
    secundarios: [
      { nombre: "Cereales", precio: 4.99 },
      { nombre: "Yogur", precio: 3.99 },
      { nombre: "Croissant", precio: 2.99 }
    ],
    postres: [
      { nombre: "Fruta", precio: 3.49 },
      { nombre: "Bizcocho", precio: 2.99 },
      { nombre: "Tarta", precio: 4.49 }
    ]
  },
  comida: {
    principales: [
      { nombre: "Ensalada", precio: 7.99 },
      { nombre: "Sopa", precio: 8.99 },
      { nombre: "Gazpacho", precio: 9.99 }
    ],
    secundarios: [
      { nombre: "Pollo", precio: 7.99 },
      { nombre: "Pasta", precio: 6.99 },
      { nombre: "Pescado", precio: 8.99 }
    ],
    postres: [
      { nombre: "Helado", precio: 3.99 },
      { nombre: "Café", precio: 4.99 },
      { nombre: "Flan", precio: 4.49 }
    ]
  },
  cena: {
    principales: [
      { nombre: "Filete", precio: 8.99 },
      { nombre: "Trucha", precio: 7.99 },
      { nombre: "Salmón", precio: 9.99 }
    ],
    secundarios: [
      { nombre: "Arroz", precio: 7.99 },
      { nombre: "Lasaña", precio: 6.99 },
      { nombre: "Guisantes", precio: 5.99 }
    ],
    postres: [
      { nombre: "Torrijas", precio: 5.49 },
      { nombre: "Natillas", precio: 3.99 },
      { nombre: "Trenza", precio: 4.49 }
    ]
  }
};

// Comentarios
const comentarios = [
  "¡Buena elección!",
  "¡Sale enseguida!",
  "¡Te va a gustar!",
  "¡Está muy rico!",
  "¡Excelente elección!",
  "¡Muy buena opción!",
  "¡Gran elección!",
  "¡Genial!",
  "¡Delicioso plato!",
  "¡Perfecto!"
];

// Función para parsear la hora
function parsearHora(horaInput) {
  let resultado = {
    hora: null,
    minutos: null,
    textoFormateado: ""
  };
  
  if (horaInput.includes(':')) {
    const [horas, minutos] = horaInput.split(':').map(Number);
    if (!isNaN(horas) && !isNaN(minutos) && horas >= 0 && horas <= 23 && minutos >= 0 && minutos <= 59) {
      resultado.hora = horas;
      resultado.minutos = minutos;
      resultado.textoFormateado = `${horas}:${minutos.toString().padStart(2, '0')}`;
    } else {
      return null; 
    }
  } else {
    const hora = parseInt(horaInput);
    if (isNaN(hora) || hora < 0 || hora > 23) {
      return null; 
    }
    resultado.hora = hora;
    resultado.textoFormateado = `${hora}:00`;
  }
  
  return resultado;
}

// Función para determinar el horario de comida según la hora
function determinarHorarioComida(resultadoHora) {
  const hora = resultadoHora.hora;
  
  if (hora >= horarios.desayuno.inicio && hora < horarios.desayuno.fin) {
    return "desayuno";
  } else if (hora >= horarios.comida.inicio && hora < horarios.comida.fin) {
    return "comida";
  } else if (hora >= horarios.cena.inicio && hora <= horarios.cena.fin) {
    return "cena";
  } else {
    return "cerrado";
  }
}

// Función para normalizar texto (eliminar tildes y convertir a minúsculas)
function normalizarTexto(texto) {
  return texto
    .toLowerCase()
    .normalize('NFD')  // Normalizar: descompone los caracteres acentuados
    .replace(/[\u0300-\u036f]/g, '')  // Eliminar los diacríticos (tildes)
    .trim();
}

// Función para buscar un plato por nombre (sin importar mayúsculas/minúsculas o tildes)
function buscarPlatoPorNombre(nombreBuscado, tipoPlato, horarioComida) {
  const nombreNormalizado = normalizarTexto(nombreBuscado);
  
  const platos = menu[horarioComida][tipoPlato];
  const platoEncontrado = platos.find(plato => 
    normalizarTexto(plato.nombre) === nombreNormalizado
  );
  
  return platoEncontrado || null;
}

// Función para mostrar opciones de platos por categoría
function formatearOpcionesPlatos(tipoPlato, horarioComida) {
  let opciones = `OPCIONES DE ${tipoPlato.toUpperCase()}:\n\n`;
  
  menu[horarioComida][tipoPlato].forEach((item, index) => {
    opciones += `${index + 1}. ${item.nombre} - ${item.precio.toFixed(2)}€\n`;
  });
  
  opciones += "\nPor favor, escribe el nombre del plato o su número (1-3).\n";
  opciones += "También puedes escribir 'ninguno' o '0' para no elegir.";
  
  return opciones;
}

// Función para obtener un comentario aleatorio
function obtenerComentarioAleatorio() {
  const indice = Math.floor(Math.random() * comentarios.length);
  return comentarios[indice];
}

// Función para formatear el recibo como una cadena formateada
function formatearRecibo(pedido) {
  let recibo = "======== RECIBO RESTAURANTE BOTTEGA ========\n\n";
  
  recibo += `Comida: ${pedido.horario.charAt(0).toUpperCase() + pedido.horario.slice(1)}\n`;
  recibo += `Hora: ${pedido.horaTexto}\n\n`;
  
  recibo += "PLATOS SELECCIONADOS:\n";
  
  if (pedido.platoPrincipal) {
    recibo += `Principal: ${pedido.platoPrincipal.nombre} - ${pedido.platoPrincipal.precio.toFixed(2)}€\n`;
  } else {
    recibo += "Principal: No seleccionado\n";
  }
  
  if (pedido.platoSecundario) {
    recibo += `Secundario: ${pedido.platoSecundario.nombre} - ${pedido.platoSecundario.precio.toFixed(2)}€\n`;
  } else {
    recibo += "Secundario: No seleccionado\n";
  }
  
  if (pedido.platoPostre) {
    recibo += `Postre: ${pedido.platoPostre.nombre} - ${pedido.platoPostre.precio.toFixed(2)}€\n`;
  } else {
    recibo += "Postre: No seleccionado\n";
  }
  
  recibo += `\nIMPORTE TOTAL: ${pedido.importeTotal.toFixed(2)}€\n\n`;
  recibo += "¡Gracias por comer en Restaurante Bottega!\n";
  recibo += "==========================================\n\n";
  recibo += "Presiona OK para finalizar.";
  
  return recibo;
}

// Función para calcular el importe total del pedido
function calcularTotal(pedido) {
  let total = 0;
  
  // Añadir importe del plato principal
  if (pedido.platoPrincipal) {
    total += pedido.platoPrincipal.precio;
  }
  
  // Añadir importe del plato secundario
  if (pedido.platoSecundario) {
    total += pedido.platoSecundario.precio;
  }
  
  // Añadir importe del postre
  if (pedido.platoPostre) {
    total += pedido.platoPostre.precio;
  }
  
  return total;
}

// Función para seleccionar un plato
function seleccionarPlato(tipoPlato, horarioComida, opcionesFormateadas) {
  let platoSeleccionado = null;
  let seleccionValida = false;
  
  while (!seleccionValida) {
    const seleccion = prompt(opcionesFormateadas);
    
    // Verificar si se canceló el prompt
    if (seleccion === null) {
      return { cancelado: true };
    }
    
    // Si el usuario escribe "ninguno" o "0", retornar null
    if (seleccion.toLowerCase() === 'ninguno' || seleccion === '0') {
      return { cancelado: false, plato: null };
    }
    
    // Convertir a número si es posible
    const numSeleccion = parseInt(seleccion);
    
    // Verificar si es un número válido (1-3)
    if (!isNaN(numSeleccion) && numSeleccion >= 1 && numSeleccion <= 3) {
      platoSeleccionado = menu[horarioComida][tipoPlato][numSeleccion - 1];
      seleccionValida = true;
      
      // Mostrar comentario aleatorio
      alert(`Has seleccionado: ${platoSeleccionado.nombre} - ${platoSeleccionado.precio.toFixed(2)}€\n\nComentario: "${obtenerComentarioAleatorio()}"`);
    } else {
      // Intentar buscar por nombre
      platoSeleccionado = buscarPlatoPorNombre(seleccion, tipoPlato, horarioComida);
      
      if (platoSeleccionado) {
        seleccionValida = true;
        
        // Mostrar comentario aleatorio
        alert(`Has seleccionado: ${platoSeleccionado.nombre} - ${platoSeleccionado.precio.toFixed(2)}€\n\nComentario: "${obtenerComentarioAleatorio()}"`);
      } else {
        alert(`Selección no válida. Por favor, elige un número entre 1 y 3, escribe el nombre del plato, o escribe 'ninguno' o '0'.`);
      }
    }
  }
  
  return { cancelado: false, plato: platoSeleccionado };
}

// Función principal para gestionar el pedido
function gestionarPedido() {
  // Variable para almacenar el estado del pedido
  let pedido = {
    horario: null,
    horaTexto: "",
    platoPrincipal: null,
    platoSecundario: null,
    platoPostre: null,
    importeTotal: 0
  };
  
  // 1. Solicitar la hora
  let horaValida = false;
  let resultadoHora;
  
  while (!horaValida) {
    const horaInput = prompt("Por favor, ingresa la hora actual (formato hh:mm o solo hh):");
    
    // Verificar si se canceló el prompt
    if (horaInput === null) {
      prompt("Pedido cancelado.");
      return;
    }
    
    resultadoHora = parsearHora(horaInput);
    
    if (resultadoHora !== null) {
      horaValida = true;
    } else {
      alert("Formato de hora no válido. Por favor, ingresa la hora en formato hh:mm o solo hh.");
    }
  }
  
  // 2. Determinar el horario de comida
  const horarioComida = determinarHorarioComida(resultadoHora);
  
  if (horarioComida === "cerrado") {
    alert(`Lo sentimos, el restaurante está cerrado en este momento.
Horario de apertura:
Desayuno: ${horarios.desayuno.inicio}:00 - ${horarios.desayuno.fin - 1}:59
Comida: ${horarios.comida.inicio}:00 - ${horarios.comida.fin - 1}:59
Cena: ${horarios.cena.inicio}:00 - ${horarios.cena.fin}:59`);
    
    return;
  }
  
  pedido.horario = horarioComida;
  pedido.horaTexto = resultadoHora.textoFormateado;
  
  // 3. Mostrar bienvenida
  alert(`¡Bienvenido al Restaurante Bottega!\nServicio de ${horarioComida.toUpperCase()}\nHora actual: ${resultadoHora.textoFormateado}`);
  
  // 4. Seleccionar plato principal - Mostrar opciones específicas
  const opcionesPrincipales = formatearOpcionesPlatos('principales', horarioComida);
  const resultadoPrincipal = seleccionarPlato('principales', horarioComida, opcionesPrincipales);
  
  if (resultadoPrincipal.cancelado) {
    prompt("Pedido cancelado.");
    return;
  }
  
  pedido.platoPrincipal = resultadoPrincipal.plato;
  
  // 5. Seleccionar plato secundario - Mostrar opciones específicas
  const opcionesSecundarios = formatearOpcionesPlatos('secundarios', horarioComida);
  const resultadoSecundario = seleccionarPlato('secundarios', horarioComida, opcionesSecundarios);
  
  if (resultadoSecundario.cancelado) {
    prompt("Pedido cancelado.");
    return;
  }
  
  pedido.platoSecundario = resultadoSecundario.plato;
  
  // 6. Seleccionar postre - Mostrar opciones específicas
  const opcionesPostres = formatearOpcionesPlatos('postres', horarioComida);
  const resultadoPostre = seleccionarPlato('postres', horarioComida, opcionesPostres);
  
  if (resultadoPostre.cancelado) {
    prompt("Pedido cancelado.");
    return;
  }
  
  pedido.platoPostre = resultadoPostre.plato;
  
  // 7. Calcular el importe total y mostrar el recibo en el prompt final
  pedido.importeTotal = calcularTotal(pedido);
  const reciboFormateado = formatearRecibo(pedido);
  
  // 8. Mostrar el recibo final en un prompt
  prompt(reciboFormateado);
  
}

// Iniciar el sistema cuando se carga la página
window.onload = function() {
  gestionarPedido();
};