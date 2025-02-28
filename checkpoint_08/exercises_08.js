// Ejecuta el archivo mediante la terminal con el comando "node exercises_08.js" y verifica los resultados en la consola.


// Exercise 1: Cree un bucle for en JS que imprima cada nombre en esta lista. miLista = “velma”, “exploradora”, “jane”, “john”, “harry”

console.log("--------- Ejercicio 1: Bucle for ---------");
const miLista = ["velma", "exploradora", "jane", "john", "harry"];

for (let i = 0; i < miLista.length; i++) {
  console.log(`Nombre ${i + 1}: ${miLista[i]}`);
}


// Exercise 2: Cree un bucle while que recorra la misma lista y también imprima los nombres. Nota: Recuerda crear un contador para que el ciclo no sea infinito.

console.log("\n--------- Ejercicio 2: Bucle while ---------");
let contador = 0;

while (contador < miLista.length) {
  console.log(`Nombre ${contador + 1}: ${miLista[contador]}`);
  contador++;
}


// Exercise 3: Cree una función de flecha que devuelva "Hola mundo".

console.log("\n--------- Ejercicio 3: Función flecha ---------");
const holaMundo = () => "Hola mundo";
console.log(`Resultado: ${holaMundo()}`);
