import random
import string
def password_gen(length: int):
    chars = string.ascii_letters
    chars += string.digits
    chars += string.punctuation
    password = ''
    for i in range(length):
        next_character = random.choice(chars)
        password += next_character
        print(password)
password_gen(8)