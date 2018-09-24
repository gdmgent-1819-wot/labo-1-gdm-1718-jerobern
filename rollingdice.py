from sense_hat import SenseHat
from random import randint
from time import sleep
import sys
import os

sense = SenseHat()

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
total1 = 0
total2 = 0

def restart():
    os.execv(sys.executable, ['python'] + sys.argv)

sense.show_message('1')
i = 0
while i < 3:
    sense.clear()
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    
    x = abs(x)
    y = abs(y)
    z = abs(z)
    
    if x > 2 or y > 2 or z > 2:
        number = randint(1,6)
        sense.show_letter(str(number), red)
        total1 += number
        sleep(1)
        i += 1
        
sense.show_message(str(total1))
sense.show_message('2')

j = 0
while j < 3:
    sense.clear()
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    
    x = abs(x)
    y = abs(y)
    z = abs(z)
    
    if x > 2 or y > 2 or z > 2:
        number = randint(1,6)
        sense.show_letter(str(number), green)
        total2 += number
        sleep(1)
        j += 1
        
sense.show_message(str(total2))

while True:
    if total1 > total2:  
        sense.show_message("1 Won!")
    if total2 > total1:  
        sense.show_message("2 Won!")
    if total2 == total1:  
        sense.show_message("Tie!")
        
    for event in sense.stick.get_events():
        if event.direction == "middle" and event.action == "released":
            restart()