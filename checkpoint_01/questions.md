# CHECKPOINT 01 

## ¿Cuáles son algunas de las cosas que hacen que SCSS sea diferente de CSS? (coloca ejemplos)
SCSS es una extensión de CSS que tiene características más avanzadas.

- Variables: permite definir variables 
```
$primary-color: #654321;
.body {
  color: $primary-color;
}
```

- Anidamiento: se pueden anidar selectores CSS dentro de otros selectores
```
.nav {
	ul {
		margin: 0;
		padding: 0;
		list-style: none;
  }
}
```

- Mixins: bloques de codigo reutilizables
```
@mixin center-flex {
  display: flex;
  justify-content: center;
  align-items: center;
}
.box {
  @include center-flex;
}
```

## ¿Qué es una variable SCSS? (porque crees que debes utilizarla pon un ejemplo de una variable, escribe una variable y como se pondría para utilizarla)
Una variable en SCSS es como una etiqueta para un valor que puedes reutilizar en diferentes partes de tu código. Es útil porque facilita el mantenimiento y la actualización del código. Por ejemplo, si defines un color principal y decides cambiarlo, solo necesitas cambiarlo en un lugar.
```
$main-color: #ffccaa;
.header {
  background-color: $main-color;
}
.footer {
  border-top: 2px solid $main-color;
}
```

## ¿Qué es un SCSS Mixin? (porque crees que debes utilizarla pon un ejemplo de un mixin, escribiendo cómo se crea y como se pondría para utilizarla)
Es como una función en programación. Te permite definir estilos reutilizables que puedes aplicar en cualquier lugar. Son útiles para evitar la repetición de código y para agrupar estilos que se utilizan con frecuencia.
```
@mixin box-shadow($x, $y, $blur, $color) {
  box-shadow: $x $y $blur $color;
}
.card {
  @include box-shadow(2px, 2px, 5px, #aabbcc);
}
```

## ¿Qué significa Unidad fraccionaria (fr) con CSS Grid?
Es una unidad de medida que representa una fracción del espacio disponible.
```
.grid-container {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
}
```