import pgzrun
from random import randint
# defing screen width and height
WIDTH=400
HEIGHT=400
score=0
game_over=False
# creating fox and coin objects from Actor class
fox=Actor("fox")
fox.POS=100,100
coin=Actor("coin")
coin.pos=200,200
# draw function
# def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: "+ str(score), color="black", topleft=(10,10))
    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: "+str(score),topleft=(10,10),fontsize=60
def place_coin():
    coin.x=randint(20,(WIDTH-20))
    coin.Y=randint(20,(HEIGHT-20))
def time_up():
    global game_over
    game_over=True
def update():
    global score
    if keyboard.left:
        fox.x=
pgzrun.go()
    