import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500

score = 0
game_over = False

cat = Actor("cat")
cat.pos = 100,100

mouse = Actor("mouse")
mouse.pos = 200,200

def draw():
  screen.blit("background", (0,0))
  mouse.draw()
  cat.draw()
  screen.draw.text("score: " + str(score), color="black")

  if game_over:
    screen.fill("pink")
    screen.draw.text("Times up! your final score: ")
    fontsize==40, color==("red")

    
def place_flower ():
  mouse.x = randint(70, (WIDTH-70))
  mouse.y = randint(70, HEIGHT-70)


def time_up():
  global game_over
  game_over = True 

def update():
  global score

  if keyboard.left:
    cat.x = cat.x - 2
  if keyboard.right:
    cat.x = cat.x + 2
  if keyboard.up:
    cat.y = cat.y - 2
  if keyboard.down:
    cat.y = cat.y + 2 

mouse_collected = cat.colliderect(mouse)

if mouse_collected:
  score = score + 10
  place_mouse()


  clock.schedule(time_up, 60.0)



  pgzrun.go