# Curva parametrizada animada
import numpy as np
import turtle

tela = turtle.Screen()
for i in range(3000):
    t = (i / 80*np.pi)+(np.pi/2)
    x = 200*np.cos(t)
    y = 200*np.sin(2*t)
    turtle.goto(x,y)
screen.exitonclick()
