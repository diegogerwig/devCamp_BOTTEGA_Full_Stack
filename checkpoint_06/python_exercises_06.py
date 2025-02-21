# Exercise 1: Cree una clase de Python llamada Usuario que use el método init y cree un nombre de usuario y una contraseña. Crea un objeto usando la clase.

import random
import string

class Usuario:
    def __init__(self, username, password=None):
        self.username = username
        if password is None:
            self.password = self._generate_random_password()
        else:
            self.password = password
    
    def _generate_random_password(self, length=12):
        # Define character sets for password
        letters = string.ascii_letters  # a-z and A-Z
        digits = string.digits          # 0-9
        symbols = string.punctuation    # symbols
        
        # Combine all characters
        all_characters = letters + digits + symbols
        
        # Generate password
        password = ''.join(random.choice(all_characters) for _ in range(length))
        return password

# User with specified password
user1 = Usuario("Carlos", "mypass123")
print(f"User 1 ->  Username: {user1.username}  //  Password: {user1.password}")

# User with auto-generated password
user2 = Usuario("Susana")
print(f"User 2 ->  Username: {user2.username}  //  Password: {user2.password}")