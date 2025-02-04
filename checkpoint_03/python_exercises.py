# Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.
my_string = "Python"
my_number = 42
my_list = ['blue', 2, 'Laura', False, 'last element in the list']
my_boolean = True

# Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable.
first_letters = my_string[:3]
print(first_letters)


# Exercise 3: Use an index to grab the first element from your list.
first_element = my_list[0]
print(first_element)

# Exercise 4: Create a new number variable that adds 10 to your original number.
new_number = my_number + 10
print(new_number)

# Exercise 5: Use an index to get the last element in your list.
last_element = my_list[-1]
print(last_element)

# Exercise 6: Use split to transform the following string into a list.
names = 'harry,alex,susie,jared,gail,conner'
names_list = names.split(',')
print(names_list)

# Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.
original_phrase = "hello world python"
print
first_word = original_phrase.split()[0]
print(first_word)
uppercase_word = first_word.upper()
print(uppercase_word)
new_phrase = uppercase_word + original_phrase[len(first_word):]
print(new_phrase)

# Exercise 8: Use string interpolation to print out a sentence that contains your number variable.
print(f"My favorite number is {my_number}")

# Exercise 9: Print “hello world”.
print("hello world")
