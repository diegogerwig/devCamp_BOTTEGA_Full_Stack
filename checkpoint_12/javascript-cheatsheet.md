# JavaScript Cheatsheet

## Manipulación de Elementos HTML con JavaScript

### Eliminar Elementos HTML
```javascript
// Seleccionar y eliminar un elemento
const element = document.querySelector('.mi-clase');
element.remove();

// Eliminar un elemento hijo
const padre = document.querySelector('#contenedor');
const hijo = document.querySelector('.elemento-hijo');
padre.removeChild(hijo);

// Eliminar múltiples elementos
document.querySelectorAll('.elementos-a-eliminar').forEach(el => el.remove());
```

### Crear y Eliminar Bullet Points Entre Listas

#### Crear elementos de lista
```javascript
// Crear un nuevo elemento de lista
const newListItem = document.createElement('li');
newListItem.textContent = 'Nuevo elemento';

// Añadir el elemento a una lista existente
const list = document.querySelector('ul');
list.appendChild(newListItem);

// Insertar en una posición específica
const referenceItem = list.children[2];
list.insertBefore(newListItem, referenceItem);
```

#### Eliminar elementos de lista
```javascript
// Eliminar un elemento específico de la lista
const itemToRemove = document.querySelector('li.elemento-a-eliminar');
itemToRemove.remove();

// Eliminar el último elemento de la lista
const list = document.querySelector('ul');
if (list.lastChild) {
    list.removeChild(list.lastChild);
}

// Limpiar todos los elementos de una lista
while (list.firstChild) {
    list.removeChild(list.firstChild);
}
```

## Consola en JavaScript

### Métodos de la Consola
```javascript
// Mensajes básicos
console.log('Mensaje informativo normal');
console.info('Mensaje informativo');
console.warn('Mensaje de advertencia');
console.error('Mensaje de error');

// Agrupación
console.group('Nombre del grupo');
console.log('Elemento 1 del grupo');
console.log('Elemento 2 del grupo');
console.groupEnd();

// Tablas
console.table([
    { nombre: 'Ana', edad: 28 },
    { nombre: 'Carlos', edad: 32 }
]);

// Tiempo de ejecución
console.time('operacion');
// código a medir
console.timeEnd('operacion');

// Contadores
console.count('etiqueta'); // cuenta: 1
console.count('etiqueta'); // cuenta: 2
console.countReset('etiqueta'); // reinicia contador

// Limpiar la consola
console.clear();
```

### Cómo Usar la Función Copy de la Consola para Web Scraping
```javascript
// Seleccionar todos los títulos de artículos y copiarlos
copy(Array.from(document.querySelectorAll('article h2')).map(h => h.textContent));

// Extraer y copiar URLs de todas las imágenes
copy(Array.from(document.querySelectorAll('img')).map(img => img.src));

// Extraer texto de una tabla
copy(Array.from(document.querySelectorAll('table tr')).map(row => 
    Array.from(row.querySelectorAll('td')).map(cell => cell.textContent)
));
```

## Array Popper Alternante

```javascript
function arrayPopper(arr) {
    let start = 0;
    let end = arr.length - 1;
    let fromStart = true;
    
    return function() {
        if (start > end) return null;
        
        if (fromStart) {
            fromStart = false;
            return arr[start++];
        } else {
            fromStart = true;
            return arr[end--];
        }
    };
}

// Ejemplo de uso:
const array = [1, 2, 3, 4, 5];
const pop = arrayPopper(array);

console.log(pop()); // 1 (desde el principio)
console.log(pop()); // 5 (desde el final)
console.log(pop()); // 2 (desde el principio)
console.log(pop()); // 4 (desde el final)
console.log(pop()); // 3 (desde el principio)
console.log(pop()); // null (no quedan elementos)
```

## "There is No Foo Bar"
Este concepto se refiere a usar ejemplos de código con nombres significativos en el contexto real, en lugar de nombres genéricos como "foo" y "bar" que no transmiten el propósito real de las variables o funciones.

```javascript
// Mal ejemplo
function foo(bar) {
    return bar * 2;
}

// Buen ejemplo
function calcularPrecioConImpuesto(precioBase) {
    return precioBase * 1.21; // 21% de IVA
}
```

## Guía de Rutas RESTful

| Método HTTP | Ruta            | Acción       | Descripción                       |
|-------------|-----------------|--------------|-----------------------------------|
| GET         | /recursos       | index        | Listar todos los recursos         |
| GET         | /recursos/nuevo | new          | Formulario para crear un recurso  |
| POST        | /recursos       | create       | Crear un nuevo recurso            |
| GET         | /recursos/:id   | show         | Mostrar un recurso específico     |
| GET         | /recursos/:id/editar | edit    | Formulario para editar un recurso |
| PUT/PATCH   | /recursos/:id   | update       | Actualizar un recurso específico  |
| DELETE      | /recursos/:id   | destroy      | Eliminar un recurso específico    |

## Función para Capitalizar Texto

```javascript
// Capitalizar primera letra de cada palabra
function capitalizar(texto) {
    return texto
        .toLowerCase()
        .split(' ')
        .map(palabra => palabra.charAt(0).toUpperCase() + palabra.slice(1))
        .join(' ');
}

// Ejemplo
console.log(capitalizar('hola mundo')); // "Hola Mundo"

// Versión alternativa (solo primera letra del texto)
function capitalizarPrimeraLetra(texto) {
    return texto.charAt(0).toUpperCase() + texto.slice(1).toLowerCase();
}

console.log(capitalizarPrimeraLetra('hola mundo')); // "Hola mundo"
```

## Herramientas de Desarrollo

### Network Tab en Dev Tools
- **Columnas principales**:
  - **Name**: Nombre del recurso solicitado
  - **Status**: Código de estado HTTP (200, 404, 500, etc.)
  - **Type**: Tipo MIME del recurso (javascript, css, html, etc.)
  - **Initiator**: Qué causó la solicitud
  - **Size**: Tamaño del recurso descargado
  - **Time**: Tiempo total para completar la solicitud
  - **Waterfall**: Representación visual del tiempo de carga

- **Funcionalidades clave**:
  - Filtrar por tipo de recurso (JS, CSS, XHR, etc.)
  - Throttling (simular conexiones lentas)
  - Preservar registro (mantener los logs entre navegaciones)
  - Deshabilitar caché
  - Ver encabezados de solicitud/respuesta
  - Ver contenido de la respuesta
  - Ver parámetros de consulta
  - Exportar datos como HAR
