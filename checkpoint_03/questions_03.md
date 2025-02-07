# CHECKPOINT 03

## ¿Cuáles son los tipos de Datos en Python?

- int (enteros): como 5, -3

- float (decimales): como 3.14, -0.001

- bool: True o False

- str (cadenas de texto): como "Hola"

- list (listas): como [1, 2, 3]

- tuple (tuplas): como (1, 2, 3)

- set (colecciones de elementos únicos no ordenados): como {1, 2, 3}

- dict (diccionarios, pares clave-valor): como

## ¿Qué tipo de convención de nomenclatura deberíamos utilizar para las variables en Python?

La convención más común es el snake_case para los nombres de las variables, es decir, usar minúsculas y separar las palabras con guiones bajos.

```python
favourite_film = 'Rambo'
dark_color = 'black'
```

## ¿Qué es un Heredoc en Python?

Es una forma de crear strings multilínea usando comillas triples (''' o """). 

Permite mantener el formato y saltos de línea del texto original.

```python
texto = """Este es un
texto multilínea
en Python."""
```

## ¿Qué es una interpolación de cadenas?

La interpolación de cadenas es la inclusión de valores dentro de una cadena. 

Se puede lograr de varias maneras:

- Usando el operador %:

```python
animal = 'perro'
patas = 4
print("El %s tiene %d patas." % (animal, patas))
```

- Usando el método .format():

```python
animal = 'perro'
patas = 4
print("El {} tiene {} patas.".format(animal, patas))
```

- Usando f-strings:

```python
animal = 'perro'
patas = 4
print(f"El {animal} tiene {patas} patas.")
```

## ¿Cuándo deberíamos usar comentarios en Python?

Debemos usar comentarios para aclarar el código, explicar su propósito o detalles específicos que puedan no ser obvios para quien que lea el código en el futuro. 

- Los comentarios se escriben usando el símbolo #:

```python
# Este es un comentario
resultado = a + b  # Suma de dos números
```

- Documentar funciones y clases: Usar docstrings (""" """) para describir el propósito de una función o clase.

```python
def sumar(a, b):
    """Devuelve la suma de dos números."""
    return a + b
```

## ¿Cuáles son las diferencias entre aplicaciones monolíticas y de microservicios?

Una aplicación monolítica puede ser útil para proyectos pequeños o medianos, mientras que los microservicios son usados para sistemas grandes y escalables.

**Aplicaciones monolíticas**

- Estructura: Un único bloque de código interconectado.

- Implementación: Todas las funcionalidades están agrupadas en una sola aplicación.

- Escalabilidad: Escalado horizontal y vertical más difícil.

- Despliegue: Un solo despliegue para toda la aplicación.

- Mantenimiento: Puede ser difícil de mantener y actualizar debido a su tamaño y complejidad.

**Aplicaciones de microservicios**

- Estructura: Conjunto de servicios pequeños y autónomos que se comunican entre sí.

- Implementación: Cada microservicio tiene su propia funcionalidad y puede ser desarrollado, desplegado y escalado de manera independiente.

- Escalabilidad: Escalado más sencillo, solo se escalan los microservicios que lo necesitan.

- Despliegue: Despliegue independiente de cada microservicio.

- Mantenimiento: Más fácil de mantener y actualizar ya que se pueden hacer cambios en un microservicio sin afectar a los demás.
