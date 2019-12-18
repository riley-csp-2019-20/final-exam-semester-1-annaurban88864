#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
# Anna Urban
#Date
# 12/18/2019


#### INSTRUCTIONS ####
# #Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors


#import required libraries
import turtle as trtl
player = trtl.Turtle()


#create turtle
player.pensize(5)


#movement functions
dis = 5

#color/drawing functions



#create screen



#bind to keypresses
def Up():
    player.setheading(90)
    player.forward(5)

def Right():
    player.setheading(0)
    player.forward(5)

def Left():
    player.setheading(180)
    player.forward(5)

def Down():
    player.setheading(270)
    player.forward(5)

def check_letter_U():
    if ("u"):
        player.penup()
    elif ('penup', True):
        player.pendown()
        

def Space():
    player.clear()

#listen
wn = trtl.Screen()
wn.onkeypress(Up,"Up")
wn.onkeypress(Right,"Right")
wn.onkeypress(Left,"Left")
wn.onkeypress(Down,"Down")
wn.onkeypress(check_letter_U, "u")
wn.onkeypress(Space,"space")
wn.listen()

#mainloop
wn.mainloop()



