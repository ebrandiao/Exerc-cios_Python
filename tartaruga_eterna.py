import turtle

from random import randint

turtle.title('tartaruga eterna')
turtle.shape('turtle')

angulo = 0

while angulo >= 0:
    angulo = int(input("Informe o ângulo:"))
    turtle.left(angulo)
    turtle.forward(100)
    

