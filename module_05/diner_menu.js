// Bottega Diner Menu System

// Build out a Diner menu in JAVASCRIPT. Here are your instructions to build that Diner.
// Bottega Diner
// Have the Main Menu and a Sides Menu
// You get one entree and two side choices at regular cost.
// - show them the entire menu (print out)
// - A user selects an entree.
// - “Waitress” makes a comment based on their selection
// - comment can either be a comparison of the two items, or random comment pulled from a comment vault.
// - Tell them the price
// - repeat the above options for side choices (comment and a price)
// - total up the cost
// BONUS: Have breakfast, lunch, and dinner menu. Breakfast has different items, lunch and dinner have the same items but are different prices.
// BONUS: Allow for item customization (how items are prepared, decide additional cost implications)


// ************************************************************************************
// ************************************************************************************
//   Pasos:
//     1.- Instala prompt-sync con: npm install prompt-sync
//     2.- Ejecuta este archivo con: node bottegaDiner.js
// ************************************************************************************
// ************************************************************************************


// Importar prompt-sync para manejar entradas del usuario
const prompt = require('prompt-sync')({ sigint: true });

// Estructura de datos del menú con opciones para desayuno, comida y cena
const menu = {
  desayuno: {
    principales: [
      { nombre: "Tortitas", precio: 7.99, descripcion: "Tortitas con sirope y mantequilla" },
      { nombre: "Huevos Benedict", precio: 9.99, descripcion: "Huevos con bacon sobre pan tostado" },
      { nombre: "Tortilla de Verduras", precio: 8.99, descripcion: "Tortilla con verduras y queso" },
      { nombre: "Tostadas con Huevo", precio: 6.99, descripcion: "Pan frito bañado en huevo" },
      { nombre: "Burrito Desayuno", precio: 10.99, descripcion: "Burrito con huevos, chorizo y queso" }
    ],
    guarniciones: [
      { nombre: "Patatas Ralladas", precio: 2.49, descripcion: "Patatas fritas ralladas" },
      { nombre: "Bacon", precio: 3.49, descripcion: "Tiras de bacon" },
      { nombre: "Fruta", precio: 3.49, descripcion: "Fruta variada" },
      { nombre: "Tostadas", precio: 1.49, descripcion: "Pan tostado con mantequilla" },
      { nombre: "Gachas", precio: 2.49, descripcion: "Gachas de avena" }
    ]
  },
  comida: {
    principales: [
      { nombre: "Hamburguesa", precio: 11.99, descripcion: "Hamburguesa con lechuga y tomate" },
      { nombre: "Wrap de Pollo", precio: 10.99, descripcion: "Pollo enrollado en tortita" },
      { nombre: "Sándwich Mixto", precio: 12.99, descripcion: "Sándwich con carne y queso" },
      { nombre: "Ensalada Mixta", precio: 9.99, descripcion: "Ensalada con pollo y huevo" },
      { nombre: "Hamburguesa Vegetal", precio: 10.99, descripcion: "Hamburguesa sin carne" }
    ],
    guarniciones: [
      { nombre: "Patatas Fritas", precio: 3.49, descripcion: "Patatas fritas normales" },
      { nombre: "Aros de Cebolla", precio: 4.49, descripcion: "Cebollas rebozadas fritas" },
      { nombre: "Ensalada Verde", precio: 3.49, descripcion: "Lechuga y tomate" },
      { nombre: "Ensalada de Col", precio: 2.49, descripcion: "Col con mayonesa" },
      { nombre: "Sopa", precio: 4.49, descripcion: "Sopa casera del día" }
    ]
  },
  cena: {
    principales: [
      { nombre: "Hamburguesa", precio: 13.99, descripcion: "Hamburguesa con lechuga y tomate" },
      { nombre: "Wrap de Pollo", precio: 12.99, descripcion: "Pollo enrollado en tortita" },
      { nombre: "Sándwich Mixto", precio: 14.99, descripcion: "Sándwich con carne y queso" },
      { nombre: "Ensalada Mixta", precio: 11.99, descripcion: "Ensalada con pollo y huevo" },
      { nombre: "Hamburguesa Vegetal", precio: 12.99, descripcion: "Hamburguesa sin carne" }
    ],
    guarniciones: [
      { nombre: "Patatas Fritas", precio: 3.49, descripcion: "Patatas fritas normales" },
      { nombre: "Aros de Cebolla", precio: 4.49, descripcion: "Cebollas rebozadas fritas" },
      { nombre: "Ensalada Verde", precio: 3.49, descripcion: "Lechuga y tomate" },
      { nombre: "Ensalada de Col", precio: 2.49, descripcion: "Col con mayonesa" },
      { nombre: "Sopa", precio: 4.49, descripcion: "Sopa casera del día" }
    ]
  }
};

// Opciones de personalización
const personalizaciones = {
  hamburguesa: [
    { nombre: "Carne Extra", precio: 2.50 },
    { nombre: "Queso", precio: 0.80 },
    { nombre: "Bacon", precio: 1.20 },
    { nombre: "Aguacate", precio: 1.80 }
  ],
  huevos: [
    { nombre: "Poco Hechos", precio: 0 },
    { nombre: "Normal", precio: 0 },
    { nombre: "Muy Hechos", precio: 0 },
    { nombre: "Revueltos", precio: 0 }
  ],
  tostadas: [
    { nombre: "Pan Blanco", precio: 0 },
    { nombre: "Pan Integral", precio: 0 },
    { nombre: "Pan Especial", precio: 0.50 },
    { nombre: "Sin Gluten", precio: 1.20 }
  ],
  ensalada: [
    { nombre: "Aceite y Sal", precio: 0 },
    { nombre: "Aliño Normal", precio: 0 },
    { nombre: "Vinagre", precio: 0 },
    { nombre: "Sin Aliño", precio: 0 },
    { nombre: "Aliño Extra", precio: 0.60 }
  ]
};

// Comentarios de la camarera
const comentariosCamarera = {
  general: [
    "¡Buena elección!",
    "¡Sale enseguida!",
    "¡Te va a gustar!",
    "¡Está muy rico!",
    "¡Excelente!",
    "¡Muy bueno!",
    "¡Buena opción!",
    "¡Genial!",
    "¡Delicioso!",
    "¡Perfecto!"
  ],
  desayuno: {
    "Tortitas": ["Están muy ricas.", "Van bien con el sirope."],
    "Huevos Benedict": ["Los huevos están muy buenos.", "Recién hechos."],
    "Tortilla de Verduras": ["Lleva verduras frescas.", "Está buenísima."],
    "Tostadas con Huevo": ["El pan está crujiente.", "Muy ricas."],
    "Burrito Desayuno": ["Es grande y llenador.", "No pica mucho."]
  },
  comida: {
    "Hamburguesa": ["La carne está jugosa.", "Es casera."],
    "Wrap de Pollo": ["El pollo está muy tierno.", "Es ligero."],
    "Sándwich Mixto": ["El pan está tostadito.", "El queso se derrite bien."],
    "Ensalada Mixta": ["Las verduras están frescas.", "Es muy completa."],
    "Hamburguesa Vegetal": ["Sabe muy bien.", "Parece carne de verdad."]
  },
  guarniciones: {
    "Patatas Fritas": ["Están crujientes.", "Recién hechas."],
    "Aros de Cebolla": ["Están muy buenos.", "Bien fritos."],
    "Ensalada Verde": ["Está fresca.", "Los tomates son dulces."],
    "Ensalada de Col": ["Hecha hoy.", "Casera."],
    "Sopa": ["Está calentita.", "Receta de la casa."],
    "Patatas Ralladas": ["Están crujientes.", "Muy ricas."],
    "Bacon": ["Está crujiente.", "Rico rico."],
    "Fruta": ["Está fresca.", "De temporada."],
    "Tostadas": ["Con mantequilla.", "Bien tostadas."],
    "Gachas": ["Están cremosas.", "Muy ricas."]
  }
};

// Aplicación Restaurante Bottega
class RestauranteBottega {
  constructor() {
    this.horario = null;
    this.platoPrincipal = null;
    this.guarnicionesElegidas = [];
    this.personalizaciones = [];
    this.costoTotal = 0;
  }

  // Imprimir el menú completo
  imprimirMenu(horario) {
    console.log(`\n===== RESTAURANTE BOTTEGA - MENÚ DE ${horario.toUpperCase()} =====\n`);
    
    console.log("PLATOS PRINCIPALES (Elige uno):");
    menu[horario].principales.forEach((item, index) => {
      console.log(`${index + 1}. ${item.nombre} - ${item.precio.toFixed(2)}€`);
      console.log(`   ${item.descripcion}`);
    });
    
    console.log("\nGUARNICIONES (Elige dos):");
    menu[horario].guarniciones.forEach((item, index) => {
      console.log(`${index + 1}. ${item.nombre} - ${item.precio.toFixed(2)}€`);
      console.log(`   ${item.descripcion}`);
    });
    
    console.log("\n===========================================");
  }

  // Obtener comentario de la camarera
  obtenerComentarioCamarera(item, categoria) {
    let comentario;
    const comentariosEspecificos = comentariosCamarera[this.horario] || comentariosCamarera.comida;
    
    if (categoria === 'principal' && comentariosEspecificos[item.nombre]) {
      // Obtener comentario específico del plato
      const comentariosPlato = comentariosEspecificos[item.nombre];
      comentario = comentariosPlato[Math.floor(Math.random() * comentariosPlato.length)];
    } else if (categoria === 'guarnicion' && comentariosCamarera.guarniciones[item.nombre]) {
      // Obtener comentario específico de la guarnición
      const comentariosGuarnicion = comentariosCamarera.guarniciones[item.nombre];
      comentario = comentariosGuarnicion[Math.floor(Math.random() * comentariosGuarnicion.length)];
    } else {
      // Obtener comentario general aleatorio
      comentario = comentariosCamarera.general[Math.floor(Math.random() * comentariosCamarera.general.length)];
    }
    
    return comentario;
  }

  // Seleccionar plato principal
  seleccionarPrincipal(index) {
    const principales = menu[this.horario].principales;
    if (index >= 1 && index <= principales.length) {
      this.platoPrincipal = principales[index - 1];
      const comentario = this.obtenerComentarioCamarera(this.platoPrincipal, 'principal');
      
      console.log(`\nHas seleccionado: ${this.platoPrincipal.nombre} - ${this.platoPrincipal.precio.toFixed(2)}€`);
      console.log(`Camarera: "${comentario}"`);
      
      // Comprobar si hay personalización disponible
      this.ofrecerPersonalizacion(this.platoPrincipal.nombre);
      
      return true;
    } else {
      console.log("Selección no válida. Por favor, inténtalo de nuevo.");
      return false;
    }
  }

  // Ofrecer opciones de personalización
  ofrecerPersonalizacion(nombrePlato) {
    let tipoPersonalizacion = null;
    
    if (nombrePlato.includes("Hamburguesa")) {
      tipoPersonalizacion = "hamburguesa";
    } else if (nombrePlato.includes("Huevos") || nombrePlato.includes("Tortilla")) {
      tipoPersonalizacion = "huevos";
    } else if (nombrePlato.includes("Tostadas")) {
      tipoPersonalizacion = "tostadas";
    } else if (nombrePlato.includes("Ensalada")) {
      tipoPersonalizacion = "ensalada";
    }
    
    if (tipoPersonalizacion && personalizaciones[tipoPersonalizacion]) {
      console.log(`\n¿Te gustaría personalizar tu ${nombrePlato}?`);
      console.log("Opciones disponibles:");
      
      personalizaciones[tipoPersonalizacion].forEach((opcion, index) => {
        const textoPrecio = opcion.precio > 0 ? `+${opcion.precio.toFixed(2)}€` : "sin cargo";
        console.log(`${index + 1}. ${opcion.nombre} (${textoPrecio})`);
      });
      
      console.log("0. Sin personalización");
      
      const eleccionPersonalizacion = parseInt(prompt("Ingresa tu elección de personalización (0 para ninguna): "));
      if (eleccionPersonalizacion > 0) {
        this.añadirPersonalizacion(tipoPersonalizacion, eleccionPersonalizacion);
      }
    }
  }

  // Añadir personalización
  añadirPersonalizacion(tipo, index) {
    if (index > 0 && index <= personalizaciones[tipo].length) {
      const eleccion = personalizaciones[tipo][index - 1];
      this.personalizaciones.push(eleccion);
      console.log(`Añadido: ${eleccion.nombre} (+${eleccion.precio.toFixed(2)}€)`);
      this.costoTotal += eleccion.precio;
    }
  }

  // Seleccionar guarnición
  seleccionarGuarnicion(index) {
    const guarniciones = menu[this.horario].guarniciones;
    if (index >= 1 && index <= guarniciones.length) {
      const guarnicionElegida = guarniciones[index - 1];
      const comentario = this.obtenerComentarioCamarera(guarnicionElegida, 'guarnicion');
      
      console.log(`\nHas seleccionado: ${guarnicionElegida.nombre} - ${guarnicionElegida.precio.toFixed(2)}€`);
      console.log(`Camarera: "${comentario}"`);
      
      this.guarnicionesElegidas.push(guarnicionElegida);
      return true;
    } else {
      console.log("Selección no válida. Por favor, inténtalo de nuevo.");
      return false;
    }
  }

  // Calcular costo total
  calcularTotal() {
    // Añadir costo del plato principal
    this.costoTotal += this.platoPrincipal.precio;
    
    // Añadir costos de guarniciones (solo si se eligen más de 2)
    if (this.guarnicionesElegidas.length > 2) {
      // Ordenar guarniciones por precio (ascendente)
      const guarnicionesOrdenadas = [...this.guarnicionesElegidas].sort((a, b) => a.precio - b.precio);
      
      // Las dos primeras guarniciones están incluidas
      for (let i = 2; i < guarnicionesOrdenadas.length; i++) {
        this.costoTotal += guarnicionesOrdenadas[i].precio;
      }
    }
    
    // Añadir costos de personalización (ya añadidos cuando se selecciona la personalización)
    
    return this.costoTotal;
  }

  // Imprimir recibo
  imprimirRecibo() {
    console.log("\n========== RECIBO RESTAURANTE BOTTEGA ==========");
    console.log(`\nComida: ${this.horario.charAt(0).toUpperCase() + this.horario.slice(1)}`);
    
    console.log(`\nPlato principal: ${this.platoPrincipal.nombre} - ${this.platoPrincipal.precio.toFixed(2)}€`);
    
    if (this.personalizaciones.length > 0) {
      console.log("Personalizaciones:");
      this.personalizaciones.forEach(item => {
        console.log(`  - ${item.nombre} (+${item.precio.toFixed(2)}€)`);
      });
    }
    
    console.log("\nGuarniciones:");
    this.guarnicionesElegidas.forEach((guarnicion, index) => {
      const precio = index < 2 ? "Incluida" : `${guarnicion.precio.toFixed(2)}€`;
      console.log(`  - ${guarnicion.nombre} - ${precio}`);
    });
    
    console.log(`\nTotal: ${this.costoTotal.toFixed(2)}€`);
    console.log("\n¡Gracias por comer en Restaurante Bottega!");
    console.log("===========================================");
  }

  // Iniciar la experiencia del restaurante
  iniciar() {
    console.log("\n¡Bienvenido al Restaurante Bottega!");
    
    // 1. Elegir horario de comida
    console.log("\nPor favor, elige tu horario de comida:");
    console.log("1. Desayuno");
    console.log("2. Comida");
    console.log("3. Cena");
    
    let eleccionHorario;
    do {
      eleccionHorario = parseInt(prompt("Ingresa tu selección (1-3): "));
      switch(eleccionHorario) {
        case 1: this.horario = "desayuno"; break;
        case 2: this.horario = "comida"; break;
        case 3: this.horario = "cena"; break;
        default: console.log("Selección no válida. Por favor, inténtalo de nuevo.");
      }
    } while (![1, 2, 3].includes(eleccionHorario));
    
    // 2. Mostrar menú y obtener selecciones
    this.imprimirMenu(this.horario);
    
    // 3. Seleccionar plato principal
    let exitoPrincipal = false;
    do {
      const eleccionPrincipal = parseInt(prompt("\nSelecciona un plato principal (1-" + menu[this.horario].principales.length + "): "));
      exitoPrincipal = this.seleccionarPrincipal(eleccionPrincipal);
    } while (!exitoPrincipal);
    
    // 4. Seleccionar guarniciones (dos incluidas)
    console.log("\nSelecciona tus primeras dos guarniciones (incluidas en el precio):");
    for (let i = 0; i < 2; i++) {
      let exitoGuarnicion = false;
      do {
        const eleccionGuarnicion = parseInt(prompt(`\nSelecciona la guarnición #${i+1} (1-${menu[this.horario].guarniciones.length}): `));
        exitoGuarnicion = this.seleccionarGuarnicion(eleccionGuarnicion);
      } while (!exitoGuarnicion);
    }
    
    // 5. Preguntar si quieren guarniciones adicionales (con costo extra)
    const quiereGuarnicionExtra = prompt("\n¿Quieres una guarnición adicional? (s/n): ").toLowerCase().startsWith('s');
    if (quiereGuarnicionExtra) {
      let exitoGuarnicion = false;
      do {
        console.log("\nEsta guarnición adicional tendrá un costo extra:");
        const eleccionGuarnicion = parseInt(prompt(`Selecciona la guarnición adicional (1-${menu[this.horario].guarniciones.length}): `));
        exitoGuarnicion = this.seleccionarGuarnicion(eleccionGuarnicion);
      } while (!exitoGuarnicion);
    }
    
    // 6. Calcular total e imprimir recibo
    this.calcularTotal();
    this.imprimirRecibo();
  }
}

// Crear y ejecutar la aplicación del restaurante interactiva
const restauranteBottega = new RestauranteBottega();
restauranteBottega.iniciar();