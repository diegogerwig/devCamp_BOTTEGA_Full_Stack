# CHECKPOINT 02

## Nombra cuatro valores que se pueden usar con la propiedad justify-content.
La propiedad justify-content se usa en Flexbox para alinear los elementos a lo largo del eje principal.

- flex-start: Los elementos se agrupan al inicio
```css
.container {
  display: flex;
  justify-content: flex-start;
}
```

- flex-end: Los elementos se agrupan al final
```css
.container {
  display: flex;
  justify-content: flex-end;
}
```

- center: Los elementos se centran
```css
.container {
  display: flex;
  justify-content: center;
}
```

- space-between: Espacio igual entre elementos, sin espacios en los extremos
```css
.container {
  display: flex;
  justify-content: space-between;
}
```

## ¿Qué es un objetivo primordial?
La razón principal por la que se realiza una acción.
Suele haber un único objetivo primordial, siendo posible múltiples objetivos secundarios.
El objetivo principal debe tener prioridad respecto de los secundarios.

## ¿Qué son los wireframes de baja fidelidad?
Los wireframes de baja fidelidad son bocetos simples de una interfaz de usuario, sin detalles gráficos, que ayudan a planificar la estructura y funcionalidad de una página web o app.
Son rápidos de crear y modificar.
Permiten identifcar probelmas en las etapas iniciales.

## ¿Qué es Git y para qué sirve?
Git es un sistema de control de versiones distribuido que permite rastrear cambios en el código, colaborar con otros desarrolladores y gestionar diferentes versiones de un proyecto.
Plataformas de hosting más comunes:
- GitHub
- GitLab
- Bitbucket

## ¿Qué es un mapa del sitio?
Un mapa del sitio (sitemap) es un documento que representa la arquitectura completa de un sitio web.
Nos muestra la organización jerárquica del contenido.
Ayuda a los motores de búsqueda a indexar el contenido.

Inicio  
├── Artículos  
│   ├── Programación  
│   ├── Ciberseguridad  
│   ├── Inteligencia Artificial  
├── Sobre mí  
└── Contacto   

## Nombra tres valores que se pueden usar con flex-direction, incluido el valor predeterminado que usa flexbox cuando se crea.
La propiedad flex-direction define la dirección en la que los elementos flexibles se organizan dentro del contenedor.

- row (valor predeterminado): Los elementos se colocan en una fila de izquierda a derecha.
```css
.container {
  display: flex;
  flex-direction: row;
}
```
Ejemplo: Un menú horizontal de navegación.

- column: Los elementos se organizan en una columna de arriba hacia abajo.
```css
.container {
  display: flex;
  flex-direction: column;
}
```
Ejemplo: Un formulario con etiquetas y campos de entrada en línea vertical.

- row-reverse: Similar a row, pero el orden de los elementos se invierte.
```css
.container {
  display: flex;
  flex-direction: row-reverse;
}
```
Ejemplo: Un chat donde los mensajes más recientes aparecen primero.