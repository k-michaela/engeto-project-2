"""
engeto-project-2.py: druhý projekt do Engeto Online Python Akademie

author: Michaela Jochcová (Kerberová)
email: michaela.kerberova@gmail.com
discord: k.michaela
"""

import random

# separator
separator = "-" * 50

# welcome text 
print(f"""
Hi there!
{separator}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{separator}
Enter a number: """
)

# random number generation
def generate_random_number():
    number = random.sample(range(10), 4)
    while number[0] == 0:
        number = random.sample(range(10), 4)
    number = ''.join(map(str, number))
    return number
print(generate_random_number())

# checking whether entered number is in correct format
def check_entered_number(input):
    if len(input) != 4 or not input.isdigit():
        message = "Please enter a four-digit number and try again."
    elif len(input) != len(set(input)):
        message = "Please enter a number without duplicates and try again."
    elif input[0] == "0":
        message = "Please enter a number that doesn't start with 0 and try again."
    else:
        return True    
    print(message, separator, sep="\n")
    return False

