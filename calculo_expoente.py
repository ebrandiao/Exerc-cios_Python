base = int(input("Informe o valor da base: "))
expoente = int(input("Informe o valor do expoente: "))

resultado = 1
count = base
while count > 0:
    resultado = resultado * base
    count = count - 1

print(f"{base}, elevado a, {expoente}, é igual a, {resultado}")
