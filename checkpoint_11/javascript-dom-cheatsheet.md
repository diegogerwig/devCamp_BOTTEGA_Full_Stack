# JAVASCRIPT Y DOM CHEATSHEET

## Conceptos Básicos del DOM

### Descripción General del DOM
- **DOM**: Document Object Model - representación en memoria de la estructura del documento HTML
- Estructura de árbol donde cada nodo representa una parte del documento
- Permite a JavaScript interactuar con el contenido HTML y CSS

### Window vs Document

| `window` | `document` |
|----------|------------|
| Objeto global de nivel superior | Propiedad del objeto window |
| Representa la ventana del navegador | Representa el documento HTML cargado |
| `window.location`, `window.history` | `document.body`, `document.head` |
| Eventos de navegador (resize, scroll) | Eventos de documento (click, input) |
| `window.addEventListener()` | `document.addEventListener()` |

```javascript
// Ejemplos de Window
window.alert("Mensaje");
window.open("https://ejemplo.com");
let altura = window.innerHeight;

// Ejemplos de Document
let titulo = document.title;
let cuerpo = document.body;
document.cookie = "key=value";
```

## Selección de Elementos

### Query Selectors
```javascript
// Seleccionar un elemento por ID
const elemento = document.getElementById('miId');

// Seleccionar el primer elemento que coincide con el selector CSS
const primerElemento = document.querySelector('.miClase');
const primerBoton = document.querySelector('button');

// Seleccionar todos los elementos que coinciden (devuelve NodeList)
const todosLosParrafos = document.querySelectorAll('p');
const elementosClase = document.querySelectorAll('.miClase');

// Selección por nombre de etiqueta (devuelve HTMLCollection)
const divs = document.getElementsByTagName('div');

// Selección por clase (devuelve HTMLCollection)
const clasesBoton = document.getElementsByClassName('boton');
```

## Manipulación de Clases

```javascript
// Añadir clases
elemento.classList.add('nueva-clase');
elemento.classList.add('clase1', 'clase2');

// Eliminar clases
elemento.classList.remove('vieja-clase');
elemento.classList.remove('clase1', 'clase2');

// Alternar clase (si existe la quita, si no existe la añade)
elemento.classList.toggle('activo');

// Comprobar si tiene una clase
if (elemento.classList.contains('activo')) {
    // hacer algo
}

// Reemplazar una clase por otra
elemento.classList.replace('vieja-clase', 'nueva-clase');
```

## Manipulación de Estilos CSS

```javascript
// Añadir o modificar estilos inline
elemento.style.color = 'red';
elemento.style.fontSize = '20px';
elemento.style.marginTop = '10px';

// Obtener valor computed style (estilos aplicados)
const estiloAplicado = window.getComputedStyle(elemento).color;

// Establecer múltiples propiedades CSS
Object.assign(elemento.style, {
    color: 'blue',
    backgroundColor: '#f0f0f0',
    padding: '1rem'
});

// Eliminar un estilo específico
elemento.style.color = '';  // Eliminar propiedad color
```

## Event Listeners

```javascript
// Añadir event listener
elemento.addEventListener('click', function(event) {
    console.log('Elemento clickeado');
    console.log(event); // objeto del evento
});

// Listener con función nombrada
function manejarClick(event) {
    console.log('Función manejadora');
}
elemento.addEventListener('click', manejarClick);

// Remover event listener
elemento.removeEventListener('click', manejarClick);

// Event listener con opciones
elemento.addEventListener('click', manejarClick, {
    once: true,       // Ejecutar solo una vez
    capture: true,    // Fase de captura en lugar de burbujeo
    passive: true     // No llamará a preventDefault()
});
```

### Comparación: inline onclick vs addEventListener

```html
<!-- Inline onclick (no recomendado para proyectos grandes) -->
<button onclick="alert('Hola')">Click me</button>
```

```javascript
// addEventListener (mejor práctica)
document.querySelector('button').addEventListener('click', function() {
    alert('Hola');
});
```

| Inline onclick | addEventListener |
|----------------|------------------|
| Mezcla HTML y JS | Separa HTML y JS |
| Solo un handler | Múltiples handlers |
| No hay control de burbujeo | Control completo de eventos |
| Más difícil de mantener | Más mantenible y modular |

## Creación y Manipulación de Elementos

```javascript
// Crear un nuevo elemento
const nuevoParrafo = document.createElement('p');

// Añadir contenido
nuevoParrafo.textContent = 'Este es un nuevo párrafo';
// o
nuevoParrafo.innerHTML = 'Texto con <strong>HTML</strong>';

// Añadir atributos
nuevoParrafo.id = 'miParrafo';
nuevoParrafo.className = 'texto destacado';
nuevoParrafo.setAttribute('data-info', 'personalizado');

// Insertar en el DOM
document.body.appendChild(nuevoParrafo);  // Al final del body
parentElement.prepend(nuevoParrafo);      // Al inicio del parent
parentElement.insertBefore(nuevoParrafo, referenciaElemento);

// Reemplazar elemento
parentElement.replaceChild(nuevoParrafo, viejoElemento);

// Eliminar elemento
elementoAEliminar.remove();
// o
parentElement.removeChild(elementoAEliminar);
```

## Ejemplos Prácticos

### Contador de Caracteres
```javascript
const textarea = document.querySelector('textarea');
const contador = document.querySelector('.contador');

textarea.addEventListener('input', function() {
    const caracteresRestantes = 280 - this.value.length;
    contador.textContent = caracteresRestantes;
    
    // Añadir clases según el número de caracteres
    if (caracteresRestantes < 0) {
        contador.classList.add('error');
    } else {
        contador.classList.remove('error');
    }
});
```

### Función Toggle (alternar)
```javascript
function toggleElementVisibility(selector) {
    const elemento = document.querySelector(selector);
    
    if (elemento.style.display === 'none') {
        elemento.style.display = 'block';
    } else {
        elemento.style.display = 'none';
    }
    
    // Alternativa usando classList.toggle
    // elemento.classList.toggle('hidden');
}

// Uso
toggleElementVisibility('#miElemento');
```

### Teclas de Acceso Rápido (Hotkeys)
```javascript
document.addEventListener('keydown', function(event) {
    // Ctrl + S
    if (event.ctrlKey && event.key === 's') {
        event.preventDefault(); // Prevenir comportamiento por defecto
        guardarDocumento();
    }
    
    // Alt + N
    if (event.altKey && event.key === 'n') {
        event.preventDefault();
        crearNuevoDocumento();
    }
});

function guardarDocumento() {
    console.log('Documento guardado');
}

function crearNuevoDocumento() {
    console.log('Nuevo documento creado');
}
```

### Compartir Comportamiento con Funciones
```javascript
// Función reutilizable para validar formularios
function validarCampo(input, validacionFn, mensajeError) {
    input.addEventListener('blur', function() {
        const esValido = validacionFn(this.value);
        const mensajeElement = this.nextElementSibling;
        
        if (!esValido) {
            this.classList.add('error');
            mensajeElement.textContent = mensajeError;
        } else {
            this.classList.remove('error');
            mensajeElement.textContent = '';
        }
    });
}

// Uso
const emailInput = document.querySelector('#email');
validarCampo(
    emailInput, 
    (valor) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(valor),
    'Por favor ingresa un email válido'
);

const passwordInput = document.querySelector('#password');
validarCampo(
    passwordInput,
    (valor) => valor.length >= 8,
    'La contraseña debe tener al menos 8 caracteres'
);
```
