# JAVASCRIPT Y DOM CHEATSHEET

## Conceptos Básicos del DOM

### Descripción General del DOM
- **DOM**: Document Object Model - representación en memoria de la estructura del documento HTML
- Estructura jerárquica en forma de árbol donde cada nodo representa una parte del documento
- Proporciona una interfaz de programación para modificar dinámicamente el contenido, estructura y estilo
- Independiente del lenguaje de programación (aunque comúnmente manipulado con JavaScript)
- Conecta las páginas web con scripts o lenguajes de programación

### Estructura y Componentes del DOM

#### Tipos de Nodos

1. **Document**: Nodo raíz que representa el documento HTML completo (`document`)
2. **Element**: Nodos que representan etiquetas HTML (`<div>`, `<p>`, `<span>`, etc.)
3. **Attr**: Representan atributos de elementos (`id`, `class`, `href`, etc.)
4. **Text**: Contiene el texto dentro de un elemento
5. **Comment**: Representa comentarios HTML (`<!-- comentario -->`)
6. **DocumentFragment**: Nodo liviano que puede contener múltiples nodos sin ser parte del DOM activo

#### Relaciones entre Nodos

- **Padres**: Nodos que contienen otros nodos
- **Hijos**: Nodos contenidos dentro de otros nodos
- **Hermanos**: Nodos que comparten el mismo padre
- **Descendientes**: Todos los nodos contenidos en un nodo dado (hijos, nietos, etc.)
- **Ancestros**: Todos los nodos que contienen un nodo dado (padres, abuelos, etc.)

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

### Selectores Básicos

```javascript
// Seleccionar un único elemento por ID
const elemento = document.getElementById('miId');

// Seleccionar elementos por nombre de clase (devuelve HTMLCollection)
const elementos = document.getElementsByClassName('miClase');

// Seleccionar elementos por nombre de etiqueta (devuelve HTMLCollection)
const parrafos = document.getElementsByTagName('p');

// Seleccionar elementos por nombre (para inputs con atributo name)
const inputs = document.getElementsByName('miNombre');
```

### Selectores Modernos (API querySelector)

```javascript
// Seleccionar el primer elemento que coincida con el selector CSS
const elemento = document.querySelector('.miClase');
const primerBoton = document.querySelector('button');

// Seleccionar todos los elementos que coincidan (devuelve NodeList)
const elementos = document.querySelectorAll('div.miClase');
const todosLosParrafos = document.querySelectorAll('p');

// Ejemplos de selectores complejos
const items = document.querySelectorAll('ul > li:nth-child(odd)');
const activos = document.querySelector('.usuario.activo');
```

## Manipulación del DOM

### Crear y Modificar Elementos

```javascript
// Crear un nuevo elemento
const nuevoDiv = document.createElement('div');
const nuevoParrafo = document.createElement('p');

// Establecer contenido de texto
nuevoDiv.textContent = 'Texto del elemento';

// Establecer HTML interno (cuidado con XSS)
nuevoDiv.innerHTML = '<span>Contenido HTML</span>';
nuevoParrafo.innerHTML = 'Texto con <strong>HTML</strong>';

// Añadir atributos
nuevoParrafo.id = 'miParrafo';
nuevoParrafo.className = 'texto destacado';
nuevoParrafo.setAttribute('data-info', 'personalizado');

// Clonar un elemento (true para clonar también sus descendientes)
const clon = elemento.cloneNode(true);
```

### Insertar y Eliminar Elementos

```javascript
// Añadir al final de un elemento padre
padreElemento.appendChild(nuevoElemento);
document.body.appendChild(nuevoParrafo);  // Al final del body

// Insertar antes de un elemento específico
padreElemento.insertBefore(nuevoElemento, referenciaElemento);

// Métodos modernos de inserción
elementoReferencia.before(nuevoElemento); // Antes del elemento
elementoReferencia.after(nuevoElemento);  // Después del elemento
elementoReferencia.prepend(nuevoElemento); // Al inicio de sus hijos
elementoReferencia.append(nuevoElemento);  // Al final de sus hijos
parentElement.prepend(nuevoParrafo);      // Al inicio del parent

// Reemplazar un elemento
padreElemento.replaceChild(nuevoElemento, elementoAReemplazar);
parentElement.replaceChild(nuevoParrafo, viejoElemento);

// Eliminar un elemento
elementoAEliminar.remove(); // Método moderno
padreElemento.removeChild(elementoAEliminar); // Método tradicional
```

### Manipular Atributos y Propiedades

```javascript
// Obtener un atributo
const valor = elemento.getAttribute('href');

// Establecer un atributo
elemento.setAttribute('class', 'nueva-clase');

// Verificar si existe un atributo
const existe = elemento.hasAttribute('disabled');

// Eliminar un atributo
elemento.removeAttribute('hidden');

// Acceso directo a propiedades (más eficiente para propiedades comunes)
elemento.id = 'nuevoId';
elemento.className = 'clase1 clase2';
elemento.value = 'Nuevo valor';
```

## Manipulación de Clases CSS

```javascript
// API moderna para manipular clases
elemento.classList.add('nueva-clase');
elemento.classList.add('clase1', 'clase2');

// Eliminar clases
elemento.classList.remove('vieja-clase');
elemento.classList.remove('clase1', 'clase2');

// Alternar clase (añade si no existe, elimina si existe)
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
// Establecer estilos directamente
elemento.style.color = 'red';
elemento.style.backgroundColor = '#f0f0f0';
elemento.style.fontSize = '20px';
elemento.style.marginTop = '10px';

// Obtener estilos computados (incluidos los de hojas de estilo)
const estilos = window.getComputedStyle(elemento);
const colorActual = estilos.color;
const estiloAplicado = window.getComputedStyle(elemento).color;

// Establecer múltiples propiedades CSS
Object.assign(elemento.style, {
    color: 'blue',
    backgroundColor: '#f0f0f0',
    padding: '1rem'
});

// Eliminar un estilo específico
elemento.style.color = ''; // Eliminar propiedad color
```

## Eventos del DOM

### Gestión de Eventos

```javascript
// Método moderno (recomendado)
elemento.addEventListener('click', function(evento) {
    console.log('Elemento clickeado');
    console.log(evento.target); // El elemento que recibió el evento
});

// Listener con función nombrada
function manejarClick(event) {
    console.log('Función manejadora');
}
elemento.addEventListener('click', manejarClick);

// Eliminar un event listener
elemento.removeEventListener('click', manejarClick);

// Event listener con opciones
elemento.addEventListener('click', manejarClick, {
    once: true,       // Ejecutar solo una vez
    capture: true,    // Fase de captura en lugar de burbujeo
    passive: true     // No llamará a preventDefault()
});

// Método antiguo (evitar)
elemento.onclick = function() { /* ... */ };
```

### Propagación de Eventos

```javascript
// Detener la propagación del evento
elemento.addEventListener('click', function(evento) {
    evento.stopPropagation(); // Evita que el evento bubbling continúe
});

// Prevenir el comportamiento por defecto
formulario.addEventListener('submit', function(evento) {
    evento.preventDefault(); // Evita que el formulario se envíe
});
```

### Fases de Eventos

```javascript
// Captura (desde documento hacia el elemento)
elemento.addEventListener('click', callback, true);

// Bubbling (desde el elemento hacia el documento, comportamiento por defecto)
elemento.addEventListener('click', callback, false);
```

### Delegación de Eventos

```javascript
// Patrón útil para elementos dinámicos
document.getElementById('lista').addEventListener('click', function(evento) {
    if (evento.target.matches('li')) {
        console.log('Li clickeado:', evento.target);
    }
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

## Traversing del DOM (Recorrido)

```javascript
// Navegación por el árbol DOM
const padre = elemento.parentNode;
const siguiente = elemento.nextSibling; // Puede ser un nodo de texto
const anterior = elemento.previousSibling;

// Navegación solo por elementos (ignorando nodos de texto)
const siguienteElemento = elemento.nextElementSibling;
const anteriorElemento = elemento.previousElementSibling;
const primerHijo = elemento.firstElementChild;
const ultimoHijo = elemento.lastElementChild;

// Colecciones
const hijos = elemento.children; // Solo elementos hijos
const todosHijos = elemento.childNodes; // Incluye nodos de texto
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

## DOM y Rendimiento

### Buenas Prácticas

1. **Minimizar manipulaciones directas**:
   ```javascript
   // Malo: múltiples manipulaciones del DOM
   for (let i = 0; i < 100; i++) {
       document.body.appendChild(document.createElement('div'));
   }
   
   // Bueno: usar DocumentFragment
   const fragmento = document.createDocumentFragment();
   for (let i = 0; i < 100; i++) {
       fragmento.appendChild(document.createElement('div'));
   }
   document.body.appendChild(fragmento);
   ```

2. **Reducir reflow/repaint**:
   ```javascript
   // Malo: causa múltiples reflows
   elemento.style.width = '100px';
   elemento.style.height = '200px';
   elemento.style.margin = '10px';
   
   // Bueno: agrupar cambios de estilo
   elemento.classList.add('mi-estilo'); // Una clase con todos los estilos
   
   // Alternativa: modificar fuera del DOM
   elemento.style.display = 'none'; // Sacar del flujo
   // Hacer múltiples cambios
   elemento.style.display = ''; // Devolver al flujo
   ```

3. **Usar métodos eficientes de selección**:
   - `getElementById()` es más rápido que `querySelector()`
   - Almacenar referencias a elementos usados frecuentemente
   - Limitar el alcance de las consultas

4. **Virtualización para grandes listas**:
   - Renderizar solo elementos visibles en la ventana
   - Usar librerías específicas para listas grandes

## APIs DOM Avanzadas

### Intersection Observer

```javascript
// Detectar cuando elementos entran en el viewport
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            console.log('Elemento visible:', entry.target);
            // Cargar contenido, animar, etc.
        }
    });
});

observer.observe(document.querySelector('.elemento'));
```

### MutationObserver

```javascript
// Detectar cambios en el DOM
const observer = new MutationObserver((mutationsList) => {
    for (const mutation of mutationsList) {
        if (mutation.type === 'childList') {
            console.log('Se agregaron o eliminaron nodos hijos');
        } else if (mutation.type === 'attributes') {
            console.log('El atributo', mutation.attributeName, 'fue modificado');
        }
    }
});

observer.observe(elementoObservado, { 
    attributes: true, 
    childList: true, 
    subtree: true 
});
```

### ResizeObserver

```javascript
// Detectar cambios de tamaño en elementos
const observer = new ResizeObserver(entries => {
    for (const entry of entries) {
        console.log('Elemento redimensionado:', entry.target);
        console.log('Nuevo tamaño:', entry.contentRect);
    }
});

observer.observe(elemento);
```

## Diferencias entre Implementaciones de Navegadores

- **Soporte de características**: No todos los navegadores soportan las mismas APIs DOM
- **Prefijos de proveedor**: Algunas propiedades pueden requerir prefijos (`-webkit-`, `-moz-`, etc.)
- **Polyfills**: Código que proporciona funcionalidad moderna en navegadores antiguos
- **Detección de características**: Verificar si una característica existe antes de usarla

```javascript
// Ejemplo de detección de características
if ('IntersectionObserver' in window) {
    // Usar IntersectionObserver
} else {
    // Alternativa para navegadores que no lo soportan
}
```