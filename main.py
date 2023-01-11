import random

def generate_numbers():
    numbers = random.sample(range(1, 49), 6)
    return numbers

numbers = generate_numbers()
print("Wylosowane liczby:", numbers)