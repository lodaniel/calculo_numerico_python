# Animacao da Espiral de Arquimedes
import math
import turtle
tela = turtle.Screen()
for i in range(3000):
    wt = i / 80*math.pi
    x = (wt*5*+5)*math.cos(wt)
    y = (wt*5*+5)*math.sin(wt)
    turtle.goto(x,y)
screen.exitonclick()


'''
# Animacao da Espiral de Arquimedes - variacao 1
import math
import turtle
tela = turtle.Screen()
for i in range(20):
    #wt = i / 40*math.pi
    wt = i / 4*math.pi
    x = (wt*5*+5)*math.cos(wt)
    y = (wt*5*+5)*math.sin(wt)
    turtle.goto(x,y)
    for k in range(20):
        #wt = i / 40*math.pi
        wt = k / 4*math.pi
        x = (wt*5*+5)*math.cos(wt)
        y = (wt*5*+5)*math.sin(wt)
        turtle.goto(x,y)
screen.exitonclick()

# Animacao da Espiral de Arquimedes - variacao 2
import math
import turtle
tela = turtle.Screen()
for i in range(20):
    #wt = i / 40*math.pi
    wt = i / 4*math.pi
    x = (wt*5*+5)*math.cos(wt)
    y = (wt*5*+5)*math.sin(wt)
    turtle.goto(x,y)
    for k in range(20):
        #wt = i / 40*math.pi
        wt = k / 8*math.pi
        x = (wt*5*+5)*math.cos(wt)
        y = (wt*5*+5)*math.sin(wt)
        turtle.goto(x,y)
screen.exitonclick()

# Animacao da Espiral de Arquimedes - variacao 3
import math
import turtle
tela = turtle.Screen()
for i in range(20):
    #wt = i / 40*math.pi
    wt = i / 2*math.pi
    x = (wt*5*+5)*math.cos(wt)
    y = (wt*5*+5)*math.sin(wt)
    turtle.goto(x,y)
    for k in range(20):
        #wt = i / 40*math.pi
        wt = k / 3*math.pi
        x = (wt*5*+5)*math.cos(wt)
        y = (wt*5*+5)*math.sin(wt)
        turtle.goto(x,y)
screen.exitonclick()
'''