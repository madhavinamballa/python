# import pgzrun
# # WIDTH=800
# # HEIGHT=600
# alien = Actor('astronaut')
# alien.topright = 0, 10
# apple=Actor("apple")
# WIDTH=alien.height+800
# HEIGHT=alien.height+600
# def draw():
#     screen.clear()
#     alien.draw()

 
 
# def update():
#     alien.left += 400
#     if alien.left > WIDTH:
#         alien.right = 0
# pgzrun.go()
import pgzrun
 
alien = Actor('apple')
alien.topright = 0, 10
 
WIDTH = 500
HEIGHT = alien.height + 20
 
 
def draw():
    screen.clear()
    alien.draw()
 
 
def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0
 
 
score = 0
 
 
def on_mouse_down(pos):
    global score
    if alien.collidepoint(pos):
        score += 1
    else:
        score -= 1
        print("Nothing here")
    print(score)
pgzrun.go()