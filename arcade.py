from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

color1 = (255, 0, 0)
color2 = (0, 0, 0)

def generate_arcade():
    pattern = ''
    i = 0
    while i < 8:
        tempStr = ''
        j = 0
        while j < 4:
            tempStr += str(randint(0,1))
            j += 1
        pattern += tempStr + tempStr[::-1]
        i += 1
        
    color_pattern = []
    for x in list(pattern):
        if x == '0' :
            color_pattern.append(color1)
        elif x == '1' :
            color_pattern.append(color2)
    sense.set_pixels(color_pattern)
    return
    
while True:
    generate_arcade()
    sleep(2)
