import turtle
turtle.title('Números positivos')

distancia = input("Quantos passos a tartaruga dará?:")
distancia = int(distancia)

if distancia > 0:
    turtle.forward(distancia)

else:
    print("Número inválido mané")
