lista = [0,1,1,2,3,5,8,19]

anterior = 0
atual = 1
print(anterior)
print(atual)

for i in range(2,10):
    proximo = anterior + atual
    print(proximo)
    anterior = atual
    atual = proximo