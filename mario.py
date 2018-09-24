from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

# Define colors
x = (0, 0, 0) #black
z = (29, 43, 83) #dark blue
r = (255, 0, 77) #red
w = (255, 255, 255) #white
d = (171, 82, 54) #dark brown
p = (255, 204, 170) #pink/flesh color
y = (255, 255, 39) #yellow
b = (41, 173, 255) #blue
o = (255, 163, 0) #orange
u = (131, 118, 156) #purple
i = (126, 37, 83) #dark purple

mario = [
    x,x,x,r,r,r,w,x,
    x,x,x,r,r,r,r,r,
    x,x,d,p,d,z,p,x,
    x,x,d,p,p,d,d,p,
    x,x,x,d,p,p,p,x,
    x,r,r,y,b,b,o,x,
    w,z,b,b,b,b,z,u,
    x,x,d,x,x,x,i,x
]

mario2 = [
    x,x,d,p,d,z,p,x,
    x,x,d,p,p,d,d,p,
    x,x,x,d,p,p,p,x,
    x,r,r,y,b,b,o,x,
    w,z,b,b,b,b,z,u,
    x,x,d,x,x,x,i,x,
    x,x,x,x,x,x,x,x,
    x,x,x,x,x,x,x,x
]

sense.set_pixels(mario)

while True:
    for event in sense.stick.get_events():
        if event.direction == "up" and event.action == "released":
            sense.set_pixels(mario2)
            sleep(0.3)
            sense.set_pixels(mario)
        
