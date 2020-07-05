import pgzrun
# from random import randint
# WIDTH=400
# HEIGHT=400
# dots=[]
# lines=[]
# next_dot=0
# for dot in range(0,10):
#     actor=Actor("dot")
#     actor.pos=randint(20,WIDTH-20),randint(20,HEIGHT-20)
#     dots.append(actor)
# def draw():
#     screen.fill("black")
#     number=number+1

HEIGHT = 5000
orange=Actor("orange")
apple=Actor("apple")
pineapple=Actor("pineapple")

def draw():
    screen.fill(("purple"))
    orange.draw()
    apple.draw()
    pineapple.draw()
def place_orange():
    orange.x=300
    orange.y=200
def place_apple():
    apple.x=600
    apple.y=200
def place_pineapple():
    pineapple.x=600
    pineapple.y=600

place_apple()
place_orange()
place_pineapple()

pgzrun.go()