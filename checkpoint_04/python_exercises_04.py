# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

from decimal import Decimal

my_list = ["apple", "banana", "cherry"]
print(my_list)

my_tuple = (10, 20, 30)
print(my_tuple)

my_float = 7.25
print(my_float)
new_float = 0.1 + 0.2
print(new_float)

my_int = 42
print(my_int)

my_decimal = Decimal("7.25")  # Decimal is more precise than float. It uses exact arithmetic.
print(my_decimal)
num1 = Decimal("0.1")
num2 = Decimal("0.2")
print(num1 + num2)

my_dict = {"name": "Laura", "age": 7, "city": "Bilbao"}
print(my_dict)


# Exercise 2: Round your float up.

import math

rounded_float = math.ceil(my_float)
print(rounded_float) 


# Exercise 3: Get the square root of your float.

sqrt_float = math.sqrt(my_float)
print(sqrt_float)


# Exercise 4: Select the first element from your dictionary.

first_key = list(my_dict.keys())[0]
print(first_key)
first_value = my_dict[first_key]
print(first_value)


# Exercise 5: Select the second element from your tuple.

second_tuple_element = my_tuple[1]
print(second_tuple_element)


# Exercise 6: Add an element to the end of your list.

my_list.append("grape")
print(my_list) 


# Exercise 7: Replace the first element in your list.

my_list[0] = "orange"
print(my_list) 


# Exercise 8: Sort your list alphabetically.

my_list.sort()
print(my_list) 


# Exercise 9: Use reassignment to add an element to your tuple.

my_tuple += (40,)
print(my_tuple) 
