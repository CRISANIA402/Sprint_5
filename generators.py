import random
import string

def generate_email():
    name = "dashakolyadina"
    cohort = "53"
    digits = random.randint(100, 999)
    return f"{name}{cohort}{digits}@yandex.ru"

def generate_password(length=10):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def generate_name():
    return f"Тест{random.randint(100, 999)}"

def generate_short_password():
    return ''.join(random.choice(string.ascii_letters) for _ in range(5))