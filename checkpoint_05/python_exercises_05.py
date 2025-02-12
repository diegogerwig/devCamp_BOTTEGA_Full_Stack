# Exercise 1: Cree un bucle For de Python.
print("\nExercise 1:")
for i in range(1, 6):
    print(i)


# Exercise 2: Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.
print("\nExercise 2:")
def sum(a, b, c):
    print(a)
    print(b)
    print(c)
    return a + b + c
print(sum(1, 2, 3))


# Exercise 3: Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.
print("\nExercise 3:")
sum_lambda = lambda a, b, c: a + b + c
print(sum_lambda(1, 2, 3))


# Exercise 4: Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in.
# 		nombre = 'Enrique'
# 		lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'
print("\nExercise 4:")
nombre = 'Enrique'
# nombre = 'George'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

# Using a for-in loop
print("\nUsing a 'for-in' loop:")
for name in lista_nombre:
    if name == nombre:
        print(f"{nombre} is in the list.")
        break
else:
    print(f"{nombre} is not in the list.")

# Using the in operator directly
print("\nUsing the 'in' operator:")
if nombre in lista_nombre:
    print(f"{nombre} is in the list.")
else:
    print(f"{nombre} is not in the list.")
