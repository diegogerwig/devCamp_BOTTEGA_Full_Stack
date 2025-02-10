# CHECKPOINT 04

## ¿Cuál es la diferencia entre una lista y una tupla en Python?

- Lista (list): Es una estructura de datos mutable, lo que significa que sus elementos pueden modificarse, agregarse o eliminarse después de la creación. Se define con corchetes [].

```python
my_list = [1, 2, 3]
my_list.append(4)  
```

- Tupla (tuple): Es una estructura de datos inmutable, lo que significa que sus elementos no pueden cambiarse después de la creación. Se define con paréntesis ().

```python
my_tuple = (1, 2, 3)
```

## ¿Cuál es el orden de las operaciones?

El orden de las operaciones en Python sigue las reglas PEMDAS (Paréntesis, Exponentes, Multiplicación/División, Suma/Resta):

1. P → Paréntesis ()
2. E → Exponentes **
3. MD → Multiplicación *, División /, División entera //, Módulo % (de izquierda a derecha)
4. AS → Suma + y Resta - (de izquierda a derecha)

Ejemplo por pasos:
1. result = (3 + 2) * 2 ** 3 / 4 - 5  -> Resolvemos los parénteis: (3+2) = 5
2. result = 5 * 2 ** 3 / 4 - 5  -> Resolvemos los exponentes: 2^3 = 8 
3. result = 5 * 8 / 4 - 5  -> Resolvemos la multiplicación y/o la divisón (de izquierda a derecha): 5* 8 = 40    40 / 4 = 10
4. result = 10 - 5  -> Resolvemos la suma y/o resta (de izquierda a derecha)
5. result = 5

## ¿Qué es un diccionario Python?

Un diccionario es una estructura de datos en Python que almacena pares clave-valor. Es mutable y se define con llaves {}.

```python
my_dict = {
    "name": "Diego",
    "city": "Bilbao",
	"age": 49
}
print(my_dict["name"])
print(my_dict["city"])
print(my_dict["age"])
print(my_dict)  # Imprime el diccionario completo
```

## ¿Cuál es la diferencia entre el método ordenado y la función de ordenación?

- Método .sort():

Solo funciona en listas.
Modifica la lista original (in-place).
No devuelve una nueva lista.

```python
my_numbers = [3, 1, 4, 1, 5]
my_numbers.sort()
print(my_numbers)  # [1, 1, 3, 4, 5]
```

- Función sorted():

Funciona con cualquier estructura iterable (listas, tuplas, diccionarios, etc.).
No modifica la estructura original.
Devuelve una nueva lista ordenada.

```python
my_tuple = (3, 1, 4, 1, 5)
my_list = sorted(my_tuple)
print(my_list)  # [1, 1, 3, 4, 5]
```

## ¿Qué es un operador de reasignación?

Un operador de reasignación modifica el valor de una variable utilizando operadores aritméticos. Son 'atajos' para operaciones matemáticas.

```python
x = 10
x += 5  # Equivalente a: x = x + 5
x -= 2  # Equivalente a: x = x - 2
x *= 3  # Equivalente a: x = x * 3
x /= 2  # Equivalente a: x = x / 2
```

Estos operadores nos permiten escribir código más compacto y eficiente.
