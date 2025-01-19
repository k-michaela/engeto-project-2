import random

def generate_unique_number_1():
    # První číslice musí být mezi 1 a 9
    first_digit = random.choice(range(1, 10))
    # Zbývající tři číslice mohou být mezi 0 a 9, ale musí být unikátní
    remaining_digits = random.sample(range(10), 3)
    
    # Zajistíme, že první číslice není v seznamu zbývajících číslic
    while first_digit in remaining_digits:
        remaining_digits = random.sample(range(10), 3)
    
    # Spojíme první číslici a zbývající číslice do jednoho čísla
    number = str(first_digit) + ''.join(map(str, remaining_digits))
    
    return number

# Příklad použití
print(generate_unique_number_1())



import random

def generate_unique_number():
    first_digit = random.choice(range(1, 10))
    remaining_digits = random.sample(range(10), 3)
    while first_digit in remaining_digits:
        remaining_digits = random.sample(range(10), 3)
    number = str(first_digit) + ''.join(map(str, remaining_digits))
    return number
print(generate_unique_number())


def random_number():
    number = str(random.randint(1000, 9999))
    while len(number) != len(set(number)):
        number = str(random.randint(1000, 9999))
    return number
print(random_number())


def generate_unique_number_2():
    digits = list(range(10))
    first_digit = random.choice(digits[1:])  # první číslice není nula
    digits.remove(first_digit)
    remaining_digits = random.sample(digits, 3)
    number = str(first_digit) + ''.join(map(str, remaining_digits))
    return number
print(generate_unique_number_2())


def generate_unique_number_3():
    digits = random.sample(range(10), 4)
    while digits[0] == 0:
        digits = random.sample(range(10), 4)
    number = ''.join(map(str, digits))
    return number
print(generate_unique_number_3())