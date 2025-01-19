import random

def generate_unique_number_3():
    digits = random.sample(range(10), 4)
    while digits[0] == 0:
        digits = random.sample(range(10), 4)
    number = ''.join(map(str, digits))
    return number
print(generate_unique_number_3())
