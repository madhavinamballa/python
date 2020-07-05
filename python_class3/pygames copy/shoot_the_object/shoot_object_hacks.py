import pgzrun
from random import randint
apple=Actor("apple")
orange=Actor("orange")
pineapple=Actor("pineapple")
score=0
def draw():
    screen.clear()
    apple.draw()
    orange.draw()
    pineapple.draw()
    pineapple.draw()
def place_apple():
    apple.x=randint(10,800)
    apple.y=randint(10,600)
def place_orange():
    orange.x=randint(10,800)
    orange.y=randint(10,600)
def place_pineapple():
    pineapple.x=randint(10,800)
    pineapple.y=randint(10,600)
def on_mouse_down(pos):
    global score
    if apple.collidepoint(pos):
        print("Good shot!!!")
        score=score+1
        print(score)
        place_apple()
        place_orange()
        place_pineapple()
    else:
        print("you missed")
        screen.fill("red")
        quit()
place_apple()
place_orange()
place_pineapple()
pgzrun.go()