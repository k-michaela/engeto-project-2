"""
engeto-project-2.py: druhý projekt do Engeto Online Python Akademie, Bulls&Cows

author: Michaela Jochcová (Kerberová)
email: michaela.kerberova@gmail.com
discord: k.michaela
"""

import random
import re

# separator definition
separator = "-" * 50

# random four-digits number generator
def generate_random_number():
    while True:
        number = ''.join(random.choices('0123456789', k=4))
        if number[0] != '0' and len(set(number)) == 4:
            return number

# inserting player's input and checking number entered correctly
def check_entered_number(input):
    if not re.match(r'^[1-9]\d{3}$', input) or len(set(input)) != 4:
        print("Please enter a valid four-digit number without duplicates and not starting with 0.", separator, sep="\n")
        return False
    return True

# bulls and cows calculation
def bulls_and_cows_count(generate_random_number, player_guess):
    bulls = sum(1 for index, digit in enumerate(player_guess) if generate_random_number[index] == digit)
    cows = sum(1 for digit in player_guess if digit in generate_random_number) - bulls
    return bulls, cows

# evaluation of number of attempts
def evaluate_players_score(number_of_attempts):
    evaluation_messages = {
        range(1, 6): "Wow, excellent score!",
        range(6, 11): "Very good score!",
        range(11, 16): "Not so bad!",
        range(16, 21): "Could be better!",
        range(21, 1000): "Practice and you will definitely improve."
    }
    
    for attempts_range, evaluation_message in evaluation_messages.items():
        if number_of_attempts in attempts_range:
            print(evaluation_message)
            break

# play game
def play_game():
    # welcome the player
    print(f"""
Hi there!
{separator}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{separator}
Enter a number: 
{separator}"""
)
    # random four-digits number generator
    number = generate_random_number()

    attempts = 0

    # player's input and evaluation of player's tip
    while True:
        player_guess = input(">>> ")

        if check_entered_number(player_guess):
            attempts += 1
            if player_guess == number:
                print(f"Correct, you've guessed the right number in {attempts} guesses!")
                break
            else:
                bulls, cows = bulls_and_cows_count(number, player_guess)
                bull_or_bulls = "bull" if bulls == 1 else "bulls"
                cow_or_cows = "cow" if cows == 1 else "cows"
                print(f"{bulls} {bull_or_bulls} and {cows} {cow_or_cows}")
            print(separator)

    print(separator)
    evaluate_players_score(attempts)


if __name__ == "__main__":
    play_game()