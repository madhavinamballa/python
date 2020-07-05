import random
WIDTH = 800
HEIGHT = 600
# BACKGROUND_IMG = "grass-field"
# IMG_PREFIX = "unicorn"
player = Actor ("apple")
player.pos = 150,100
# food = Actor ("food")
# food.pos = (random.randint (50, 750), random.randint (50, 550))
# a counter to delay between changes
delay_timer = 0
# The game timer to restrict how long t
game_timer = 10
game_timer_start = 10
timer_decrement = 0.2
# which of the 3 images to display (value from 1 to 3)
image_number = 1
score = 0
def draw():
    if (game_timer <= 0):
    display_text = "Game Over\nScore "+str(score)
    screen.draw.text(display_text, fontsize=60, center=(400,300),
# shadow=(1,1), color=(255,255,255), scolor="#202020")
#  food.draw()
    player.draw()


def update():
    global delay_timer, image_number, score, game_timer
    if (game_timer <= 0):
        return
    else:
        game_timer -= 0.017

 # Only move whilst key is pressed
    if (delay_timer == 10):
        delay_timer = 0

 direction = "none"
 if (keyboard.up):
    if (player.y > 40):
        player.y -= 20
    direction = "rear"
    if (keyboard.down):
 if (player.y < 560):
 player.y += 20
 direction = "front"
 if (keyboard.left) :
 if (player.x > 40):
 player.x -= 20
 direction = "left"
 if (keyboard.right) :
 if (player.x < 760):
 player.x += 20
 direction = "right"

 if (direction != 'none'):
 image_number += 1
 if (image_number > 4):
 image_number = 1
 image_name = "{}-{}-{}".format(IMG_PREFIX,direction,image_number)
 player.image = image_name

 if (player.colliderect(food)):
 score += 1
 food.pos = (random.randint (50, 750), random.randint (50, 550))
 game_timer = game_timer_start - (score * timer_decrement)

 else:
 delay_timer += 1
 return