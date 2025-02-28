// Exercise 1: Cree una función JS que acepte 4 argumentos. Suma los dos primeros argumentos, luego los dos segundos y multiplícalos. Si el número creado es mayor que 50, la consola registra "¡El número es mayor que 50!". Si es más pequeño, la consola registra "¡El número es menor que 50!"

// Ejecuta el archivo mediante la terminal con el comando "node exercises_07.js" y verifica los resultados en la consola.

function calcularNumero(a, b, c, d) {

	// Verificar que existen 4 argumentos
    if (arguments.length !== 4) {
        console.log("❌ Error: La función requiere exactamente 4 argumentos.");
        return;
    }

    // Verificar que todos los argumentos sean números
    if (typeof a !== "number" || typeof b !== "number" || typeof c !== "number" || typeof d !== "number") {
        console.log("❌ Error: Todos los argumentos deben ser números.");
        return;
    }

    // Sumar los dos primeros argumentos
    let suma1 = a + b;
    // Sumar los dos segundos argumentos
    let suma2 = c + d;
    // Multiplicar los resultados de ambas sumas
    let resultado = suma1 * suma2;

    // Mostrar la información detallada de los cálculos
    console.log(`🔹 Argumentos recibidos: a=${a}, b=${b}, c=${c}, d=${d}`);
    console.log(`📌 Cálculo: (${a} + ${b}) * (${c} + ${d}) = ${suma1} * ${suma2} = ${resultado}`);

    // Verificar si el número es mayor o menor que 50
    if (resultado > 50) {
        console.log("🔼 ¡El número es mayor que 50!\n");
    } else {
        console.log("🔽 ¡El número es menor que 50!\n");
    }
}

// Casos válidos
calcularNumero(5, 10, 2, 3);     // 15 * 5 = 75 → Mayor que 50
calcularNumero(1, 2, 3, 4);      // 3 * 7 = 21 → Menor que 50
calcularNumero(1, -2, 3, 4);     // -1 * 7 = -7 → Menor que 50
calcularNumero(6, 2, -3, -4);    // 8 * -7 = -56 → Menor que 50
calcularNumero(-8, 2, -5, -4);   // -6 * -9 = 54 → Mayor que 50
calcularNumero(1.1, 2, 3.3, 4);  // 3.1 * 7.3 = 22.63 → Menor que 50

// Casos inválidos
calcularNumero(5, 10);               // ❌ Error: Faltan argumentos
calcularNumero(5, 10, 6, 7, 5);      // ❌ Error: Sobran argumentos
calcularNumero("a", 10, 2, 3);       // ❌ Error: Argumentos no numéricos
calcularNumero(5, null, 2, 3);       // ❌ Error: Argumentos no numéricos
calcularNumero(undefined, 10, 2, 3); // ❌ Error: Argumentos no numéricos
calcularNumero(5, 10, 2, false);     // ❌ Error: Argumentos no numéricos
