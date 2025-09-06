import pgzrun
import random

FONT_option = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
CENTRE_X = WIDTH / 2
CENTRE_Y = HEIGHT / 2
CENTRE = (CENTRE_X, CENTRE_Y)
FINAL_LEVEL = 6
START_SPEED= 10 
ITEMS = ["bag", "battery", "bottle", "chips"]

game_over = False
game_completed = False
current_level = 1
# bag = actor("papering")
items = []
animations = []

def draw():
    global items, current_level, game_over, game_completed
    screen.clear()
    screen.blit("bground", (0, 0))
    if game_over:
        display_message("GAME OVER", "Try Again")
    elif game_completed:
        display_message("YOU WON!", "Well Done")
    else:
        for item in items:
            item.draw()

def update():
    global items
    if len(items) == 0:
        items = make_items(current_level)

def make_items(number_of_extra_items):
    items_to_create = get_option_to_create(number_of_extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create(number_of_extra_items):
    
