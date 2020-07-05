import pgzrun
from random import randint
#set the screen
WIDTH=800
HEIGHT=600
score=0
# creating actor
balloon=Actor("balloon")
balloon.pos=400,300

house=Actor("house")
house.pos=randint(800,1600),460

tree=Actor("tree")
tree.pos=randint(800,1600),450
bird=Actor("bird-up")
bird.pos=randint(800,1600),randint(10,200)


def draw():
    screen.blit("background",(0,0))
    balloon.draw()
    house.draw()
    tree.draw()
    bird.draw()
    screen.draw.text("Score: "+str(score),(700,5),color="black")
pgzrun.go()

