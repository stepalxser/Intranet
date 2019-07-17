import random
import string

def generate_random_password(password_length=10):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(password_length))