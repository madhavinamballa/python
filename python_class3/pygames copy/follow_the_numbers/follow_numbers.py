import pgzrun
from random import randint
#set the screen for our game
WIDTH=600
HEIGHT=460
#create the lists to store all the dots and lines
dots=[]
lines=[]
next_dot=0
#set up the Actors
# in this game ten dots are the acotrs
#use back slash character if u need to plit long line of code into two lines
for dot in range(0,10):
    actor=Actor("dot")
    actor.pos=randint(20,WIDTH-20),randint(20,HEIGHT-20)
    # the above code will ensure that the dots are placed atleast 20 pixels away from the screen so
    # whole dot can be shown
    dots.append(actor)
#display the acotrs on the screen using draw function
def draw():
    screen.fill("orange")
    #defining a variabkle to keep track of labels of the dots
    number=1
    for dot in dots:
        screen.draw.text(str(number),(dot.pos[0],dot.pos[1]+12))
        dot.draw()
        number=number+1
    for line in lines:
        screen.draw.line(line[0],line[1],(100,0,0))

def on_mouse_down(pos):
    global next_dot
    global lines
    if dots[next_dot].collidepoint(pos):
        if next_dot:
            lines.append((dots[next_dot-1].pos,dots[next_dot].pos))
        next_dot=next_dot+1
    else:
        lines=[]
        next_dot=0



pgzrun.go()