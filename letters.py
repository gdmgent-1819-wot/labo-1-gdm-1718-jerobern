from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

# Generate random color
def pick_random_color():
    random_red = randint(0, 255)
    random_green = randint(0, 255)
    random_blue = randint(0, 255)
    return (random_red, random_green, random_blue)

# Desplay each letter from string
def display_letters(string, letter_sleep):
    for letter in list(string):
        sense.show_letter(letter, pick_random_color())
        sleep(int(letter_sleep))
    return

string = input("Voeg een string in: ")
letter_sleep = input("Hoeveel seconden tussen de letters? ")
loop_sleep = input("Hoeveel seconden tussen de loop? ")

while True:
    display_letters(string, letter_sleep)
    sense.clear()
    sleep(int(loop_sleep))
