// Ejecuta el archivo mediante la terminal con el comando "node exercises_08.js" y verifica los resultados en la consola.

// Colores para la consola
const colors = {
  reset: "\x1b[0m",
  yellow: "\x1b[33m",
  cyan: "\x1b[36m"
};

// Exercise 1: Cree un bucle for en JS que imprima cada nombre en esta lista. miLista = “velma”, “exploradora”, “jane”, “john”, “harry”

console.log(`\n${colors.yellow}--------- Ejercicio 1: Bucle for ---------${colors.reset}`);
const miLista = ["velma", "exploradora", "jane", "john", "harry"];

for (let i = 0; i < miLista.length; i++) {
  console.log(`Nombre ${i + 1}: ${colors.cyan}${miLista[i]}${colors.reset}`);
}

// Exercise 2: Cree un bucle while que recorra la misma lista y también imprima los nombres. Nota: Recuerda crear un contador para que el ciclo no sea infinito.

console.log(`\n${colors.yellow}--------- Ejercicio 2: Bucle while ---------${colors.reset}`);
let contador = 0;

while (contador < miLista.length) {
  console.log(`Nombre ${contador + 1}: ${colors.cyan}${miLista[contador]}${colors.reset}`);
  contador++;
}


// Exercise 3: Cree una función de flecha que devuelva "Hola mundo".

console.log(`\n${colors.yellow}--------- Ejercicio 3: Función flecha ---------${colors.reset}`);
const holaMundo = () => "Hola mundo";
console.log(`Resultado: ${colors.cyan}${holaMundo()}${colors.reset}`);