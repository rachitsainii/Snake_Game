import turtle
import time
import random

delay=0.125

score=0
high_score=0

#snake object
wn=turtle.Screen()
wn.title=("THE SNAKE GAME")
wn.bgcolor=("green")
wn.setup(width=600,height=600)
wn.tracer(0)

#snake characteistics
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

#SCORE
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0   High Score:0",align="center",font=("Courier",24,"normal"))
    

#functions

def go_up():
    if head.direction !="down":
        head.direction="up"
def go_down():
    if head.direction !="up":
        head.direction="down"
def go_right():
    if head.direction !="left":
        head.direction="right"
def go_left():
    if head.direction !="right":
        head.direction="left"    
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

#SNAKE FOOD
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


#BODY OF SNAKE
BODY=[]

        
        
#KEYBOARD CONTROL
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s" )
wn.onkeypress(go_right,"d" )
wn.onkeypress(go_left,"a" )


#MAIN GAME LOOP
while True:
    wn.update() 

    #COLLISION WITH THE BORDER
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        #GAME OVER PROMPT
        over=turtle.Turtle()
        over.speed(0)
        over.shape("square")
        over.color("red")
        over.penup()
        over.hideturtle()
        over.write("!GAME OVER!", align="center",font=("courier",85,"bold"))

        time.sleep(1)
        head.goto(0,0)
        head.direction= "stop"
        for body in BODY:
            body.goto(10000,10000)


            
            #CLRING THE BODY FOR A NEW GAME
        BODY.clear()
        over.clear()
        
        x=random.randint(-270,270)
        y=random.randint(-270,270)
        food.goto(x,y)
        
    #RESET THE SCORE
        score=0
        delay=0.125
        pen.clear()    
        pen.write("Score:{}  High Score:{}".format(score,high_score),align = "center", font=("courier",24,"normal"))    
        
    #COLLISON WITH FOOD
    if head.distance(food)<20:

        
        # MOVING THE FOOD TO RANDOM PLACE
        x=random.randint(-270,270)
        y=random.randint(-270,270)
        food.goto(x,y)

        #SEGMENTS OF THE SANKE
        body=turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color("purple")
        body.penup()
        BODY.append(body)

        #INCREASE IN THE SCORE
        score=score+10

        
        #INCREASING THE SPEED
        delay=delay-0.001
        
        if score>high_score:
            high_score=score
        pen.clear()
        
        pen.write("Score:{}  High Score:{}".format(score,high_score),align = "center", font=("courier",24,"normal"))   

        #MOVEMENT FOR THE REST BODY
        
    for i in range(len(BODY)-1,0,-1):
        x=BODY[i-1].xcor()
        y=BODY[i-1].ycor()
        BODY[i].goto(x,y)


            #MOVEMENT OF FIRST SEGMENT OF BODY
    if len(BODY)>0:
        x=head.xcor()
        y=head.ycor()
        BODY[0].goto(x,y)
            
            
    move()
        #COLLISION WITH THE BODY
    for body in BODY:
        if body.distance(head)<20:
                #GAME OVER PROMPT
            over=turtle.Turtle()
            over.speed(0)
            over.shape("square")
            over.color("red")
            over.penup()
            over.hideturtle()
            over.write("!GAME OVER!", align="center",font=("courier",85,"bold"))

            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            
            #RESET THE SCORE
            score=0
            delay=0.125
            pen.clear()    
            pen.write("Score:{}  High Score:{}".format(score,high_score),align = "center", font=("courier",24,"normal")) 
                
            dealay=0.125
            
            for body in BODY:
                body.goto(10000,10000)
            BODY.clear() 
            over.clear()
            x=random.randint(-270,270)
            y=random.randint(-270,270)
            food.goto(x,y)
            
    time.sleep(delay)
wn.mainloop()    
