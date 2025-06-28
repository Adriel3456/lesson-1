# import the pygame zero library
import pgzrun
from random import randint

TITLE = "Good Shot"

width = 500
height = 500

message = ""
alien = Actor('alien')

def place_alien():
    alien.x = randint(50, WIDTH-50)
    alien.y = randint(50, WIDTH-50)


def on_mouse_down(pos):
    #print("Hello World")
    global message
    if alien.collidepoint(pos):
        message = "Good shot"
        place_alien()
    else:
        message = "you missed"

place_alien()
pgzrun.go()                                                                                                   