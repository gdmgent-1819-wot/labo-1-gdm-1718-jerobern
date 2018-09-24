from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

# Generate random color
def pick_random_color():
    random_red = randint(0, 255)
    random_green = randint(0, 255)
    random_blue = randint(0, 255)
    return (random_red, random_green, random_blue)

sense.clear()

j = 0
while j < 8:
    i = 0
    while i < 8:
        sense.set_pixel(i, j, pick_random_color())
        sleep(0.5)
        sense.clear()
        i += 1
    j += 1
    if j == 8: j = 0
