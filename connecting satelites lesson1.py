import pgzrun
from random import randint
from time  import time


WIDTH = 800
HEIGHT = 600


start_time = 0
total_time = 0
end_time = 0


number_of_satellites = 8

def create_satellites():
    global start_time
    for count in range(0, number_of_satellites):
        satellite = Actor("satellite")
        satellite.pos = randint(40, WIDTH-40),randint(40,HEIGHT-40)
        satellites.append(satellite)
    start_time = time()


    def draw():
        global total_time

        screen.blit("background", (0,0))
        number = 1
        for satlellite in satlellites:
            screen.draw.text(atr(number),  (satlellite.pos[0], satlellite.pos[1]+20))
            satlellite.draw()
            number = number + 1
        
        for line in lines:
            screen.draw.line(line[0], line[1], (255, 255, 255))
        
        if next_satlellites < number_of_satellites:
            total_time = time() - start_time
            screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30)
        else:
            screen.draw.text screen.draw.text(str(round(total_time,1)),(10,10), fontsize=30)

def update():
    pass
def on_mouse_down(pos):
    global next_satellite, lines
    if next_satellites < number_of_satellites:
        if satellites[next_satellites].colidepoint(pos):
            if next_satellite:
                lines.append((satellites[next_satellite-1].pos, satellites[next_satellites].pos))
            next_satellites = next_satellites + 1
        else:
            lines = []
            next_satellites

create_satellites

pzrun.go()