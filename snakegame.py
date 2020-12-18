import turtle
import random

#head orientation
h = [0]

#score
a = [0]
b = [0]

#food coord
fcoord = [0,0,0]

#position
pos = []


def home(x,y):
    x = 0
    y = 0
    a[0] = 0
    b[0] = 0
    h[0] = 0
    fcoord[2] = 0
    pos[:] = []
    turtle.hideturtle()
    turtle.clear()
    turtle.pu()
    turtle.color("black")
    turtle.goto(0,0)
    turtle.write("play")
    turtle.title("snake")
    turtle.onscreenclick(start)
    turtle.mainloop()
    
def level_1():
    turtle.clear()
    turtle.pu()
    turtle.speed(0)
    turtle.pensize(20)
    turtle.color("red")
    turtle.goto(-220,220)
    turtle.pd()
    turtle.goto(220,220)
    turtle.goto(220,-220)
    turtle.goto(-220,-220)
    turtle.goto(-220,220)
    turtle.pu()
    turtle.goto(0,0)
    
    
 def start(x,y):
    turtle.onscreenclick(none)
    
    level_1()
    
    tfood - turtle.turtle()
    tfood.hideturtle()
    tfood.pu()
    tfood.speed(0)
    tfood.shape("circle")
    tfood.color("black")
    
    tscore = turtle.turtle()
    tscore.hideturtle()
    tscore.pu()
    tscore.speed(0)
    tscore.goto(100,-250)
    tscore.write("score:" + str(a[0]), align="center",font=(10))
    
    while x > -210 and x < 210 and y > -210 and y <210:
        if fcoord[2] == 0:
            food(tfood)
            fcoord[2] = 1
        turtle.onkey(w,"up")
        turtle.onkey(a,"left")
        turtle.onkey(d,"right")
        turtle.onkey(s,"down")
        turtle.listen()
        move()
        x = turtle.xcor()
        y = turtle.ycor()
        if x > fcoord[0]*20-5 and x < fcoord[0]*20+5 and y > fcoord[1]*20-5 and y < fcoord[1]*20+5:
            fcoord[2] = 0
            tfood.clear()
           a[0] == 1
           tscore.clear()
           tscore.write("score:" + str(a[0]), align="center",font=(10))
        
        if len(pos) > 1:
            for i in range(1,len(pos)):
                if x < pos[i][0]-5 and y < pos[i][1]+5 and y > pos[i][1]-5:
                    tscore.clear()
                    tfood.write()
                    gameover()
                    
    tscore.clear()
    tfood.clear()
    gameover()
    
    
    #food
    def food(tfood):
        x = random.randrange(-8,8,1)
        y = random.randrange(-8,8,1)
        fcoord[0] = x
        fcoord[1] = y
        tfood.hideturtle()
        tfood.pu()
        tfood.shape("square")
        tfood.color("red")
        tfood.goto(x*20,y*20)
        tfood.stamp()
        
    #up
    def w():
        if h[0] == 270:
            pass
        else:
            h[0] = 90
            
    #down
    def s():
        if h[0] == 90:
          pass
        else:
         h[0] = 270
         
    #left
    def a():
        if h[0] == 0:
           pass
          else:
              h[0] = 180
              
     #right
     def d():
         if h[0] == 180:
            pass
          else:
              h[0] = 0
              
     def move():
         turtle.pensize(1)
         turtle.color("black")
         turtle.pu()
         turtle.speed(3)
         turtle.setheading(h[0])
         turtle.shape("square")
         turtle.stamp()
         turtle.fd(20)
        x = turtle.xcor()
        y = turtle.ycor()
        if [0] > a[0]:
            turtle.clearstamps(1)
            pos.insert(0,[round(x),round(y)])
            pos.pop(-1)
         else:
            pos.insert(0,[round(x),round(y)])
            b[0] += 1
            
     def gameover():
         turtle.onscreenclick(none)
         turtle.speed(0)
         turtle.pu()
         turtle.goto(0,150)
         turtle.color("red")
         turtle.write("game over",align="center",font=(10))
         turtle.goto(0,50)
         turtle.write("score:" + str(a[0]),align="center",font=(10))
         turtle.goto(200,200)
         turtle.write("(click anywhere to return to the main menu)",align="right",font=(0.0000001))
         turtle.onscreenclick(home)
         turtle.mainloop()
        
        
    if_name_=='_main_':
        home(0,0)
         
            
     #make sure you have learned something new