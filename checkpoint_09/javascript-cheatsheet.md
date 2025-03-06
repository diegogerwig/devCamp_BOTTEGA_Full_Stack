# JAVASCRIPT MODERNO - CHEATSHEET

# Resumen JavaScript Moderno

Voy a prepararte un resumen completo y una cheatsheet para ayudarte con tu examen sobre JavaScript moderno. Dividiré la información por secciones principales.

## Herramientas de JavaScript Moderno

### Lodash
- Biblioteca de utilidades que simplifica la manipulación de arrays, objetos, strings, etc.
- Funciones populares:
  - `_.keyBy()`: convierte un array en objeto usando una propiedad como clave
  - `_.reduce()`: reduce colección a un solo valor aplicando función acumuladora
  - `_.random()`: genera números aleatorios con rangos

### Depuración
- Depurador JavaScript: herramienta integrada en navegadores para inspeccionar y depurar código
- Quokka.js: extensión que muestra resultados de código en tiempo real en el editor
- Herramientas de Lint: (ESLint, JSLint) detectan problemas de código y estilo

## Estrategias de Aprendizaje y Desarrollo
- Aprender desde cero: estructura práctica (pequeños proyectos, incrementar complejidad)
- Aprender de errores: valor de fallar como proceso de aprendizaje
- Construir funciones prácticas (ejemplo: método prettyPrice para formatear precios)
- Cambio de tareas: gestión del tiempo al alternar entre proyectos

## Gestión de Errores en JavaScript
- Sintaxis básica: try/catch/finally, throw
- Clases de error personalizadas: extender Error para crear errores específicos
- Integración en llamadas API: manejo de errores en peticiones asíncronas

## Módulos JavaScript y ES6
- Generador de proyectos ES6: configuración rápida de entorno moderno
- Sintaxis de importación/exportación: compartir código entre archivos
- Importación múltiple: diferentes formas de importar elementos
- Exportaciones predeterminadas: exportar un elemento principal por archivo

## Gestión de Paquetes JavaScript
- NPM: sistema de gestión de paquetes para JavaScript
- Instalación de paquetes: proceso para agregar bibliotecas como MomentJS
- MomentJS: biblioteca popular para manipulación de fechas y tiempos
- Creación y despliegue de módulos NPM: publicar paquetes propios

He creado una cheatsheet detallada que puedes usar como referencia rápida para tu examen. Incluye ejemplos de código, sintaxis y consejos prácticos organizados por tema.

¿Hay alguna sección específica sobre la que necesites más información o ejemplos adicionales?


## LODASH

```javascript
// Instalación
npm install lodash
// o con CDN
<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>

// Importación
import _ from 'lodash';
// o específica
import { keyBy, reduce, random } from 'lodash';

// Funciones Principales
// keyBy - Convierte array en objeto usando clave
const users = [
  { id: 1, name: 'Ana' },
  { id: 2, name: 'Carlos' }
];
const usersByID = _.keyBy(users, 'id');
// Resultado: { '1': {id: 1, name: 'Ana'}, '2': {id: 2, name: 'Carlos'} }

// reduce - Reduce colección a un valor único
const sum = _.reduce([1, 2, 3], (total, n) => total + n, 0); // = 6

// random - Genera números aleatorios
_.random(1, 10); // Entre 1 y 10
_.random(10); // Entre 0 y 10
_.random(1.5, 3.5, true); // Decimal entre 1.5 y 3.5
```

## DEPURACIÓN

### Depurador del Navegador
```javascript
// Puntos de interrupción en código
debugger;

// En consola
console.log("Valor:", variable);
console.table(arrayDeObjetos); // Muestra datos tabulares
console.time("Etiqueta") / console.timeEnd("Etiqueta"); // Medir tiempo
console.trace(); // Muestra stack trace
```

### Quokka.js
- Instalar como extensión en VS Code o JetBrains
- Crear archivo .js con Quokka activado (Ctrl+K, Q)
- Muestra resultados en tiempo real junto al código

### Herramientas Lint
```bash
# Instalación de ESLint
npm install eslint --save-dev

# Configuración
npx eslint --init

# Usar en archivo
npx eslint archivo.js
```

## MANEJO DE ERRORES

### Sintaxis Básica
```javascript
try {
  // Código que puede fallar
  if (condicion) throw new Error("Mensaje de error");
} catch (error) {
  // Manejo del error
  console.error(error.message);
} finally {
  // Se ejecuta siempre
  console.log("Proceso terminado");
}
```

### Errores Personalizados
```javascript
class ValidationError extends Error {
  constructor(message, field) {
    super(message);
    this.name = "ValidationError";
    this.field = field;
  }
}

// Uso
try {
  throw new ValidationError("Email inválido", "email");
} catch (error) {
  if (error instanceof ValidationError) {
    console.log(`Error en campo ${error.field}: ${error.message}`);
  } else {
    console.error("Error desconocido:", error);
  }
}
```

### Errores en Llamadas API
```javascript
async function fetchData(url) {
  try {
    const response = await fetch(url);
    
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error; // Re-lanzar para manejo superior
  }
}
```

## MÓDULOS ES6

### Exportaciones e Importaciones
```javascript
// Exportación nombrada (archivo math.js)
export const sum = (a, b) => a + b;
export const multiply = (a, b) => a * b;

// Exportación predeterminada
export default class Calculator {
  // ...
}

// Importación en otro archivo
import Calculator, { sum, multiply } from './math.js';
import * as math from './math.js';

// Importación dinámica
const mathModule = await import('./math.js');
```

### Pretty Price Method
```javascript
const prettyPrice = (rawPrice, extension = 0.99) => {
  // Si extension es número entre 0-1, usarlo como decimal
  // Si es entero, convertirlo a formato decimal (ej: 99 -> 0.99)
  const extensionType = typeof extension;
  const decimal = extensionType === 'number' && extension < 1 
    ? extension 
    : extension / 100;
  
  // Truncar precio a entero y añadir extensión
  return Math.floor(rawPrice) + decimal;
};

prettyPrice(29.99, 0.99); // 29.99
prettyPrice(29.99, 99);   // 29.99
prettyPrice(29.99, 0.75); // 29.75
```

## NPM Y GESTIÓN DE PAQUETES

### Comandos Básicos
```bash
# Iniciar proyecto
npm init -y

# Instalar paquete
npm install moment --save
npm i lodash --save-dev  # Solo para desarrollo

# Instalar globalmente
npm install -g create-react-app

# Actualizar paquetes
npm update

# Listar paquetes instalados
npm list

# Ejecutar scripts (definidos en package.json)
npm run test
```

### MomentJS
```javascript
// Instalación
npm install moment

// Importación
import moment from 'moment';

// Funciones comunes
moment().format('YYYY-MM-DD'); // Fecha actual formateada
moment('2023-01-15').add(7, 'days'); // Añadir tiempo
moment('2023-01-15').subtract(1, 'months'); // Restar tiempo
moment().startOf('day'); // Inicio del día actual
moment().endOf('month'); // Final del mes actual
moment('2023-01-15').fromNow(); // Tiempo relativo ("hace 3 meses")
moment('2023-01-15').isBefore('2023-02-01'); // Comparación de fechas
```

### Publicar paquete NPM
```bash
# Login en NPM
npm login

# Publicar
npm publish

# Actualizar versión (patch, minor, major)
npm version patch
npm publish
```

## CONSEJOS PRÁCTICOS PARA DESARROLLO

1. **Enfoque Incremental**: Construir características en pequeños pasos
2. **División de Tareas**: Descomponer problemas en partes manejables
3. **Tiempo de Enfoque**: Bloques de 25-50 minutos sin interrupciones
4. **Cambio de Tareas**: Planificar cambios para minimizar costos
5. **Documentación**: Documentar código durante el desarrollo
6. **Tests**: Implementar pruebas para validar funcionamiento
7. **Aprender de Errores**: Analizar fallos para mejorar
8. **Prototipado**: Crear prototipos rápidos para validar ideas
