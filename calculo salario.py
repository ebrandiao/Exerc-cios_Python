salario = float(input("Informe o valor do seu salário: "))

if salario <= 1000:
    salario = salario * 0.3 + salario
    print(f"O valor do seu salário atualizado é R$ {salario}")
elif salario > 1000 and salario <= 2000:
    salario = salario * 0.25 + salario
    print(f"O valor do seu salário atualizado é R$ {salario}")
elif salario > 2000 and salario <= 3000:
    salario = salario * 0.2 + salario
    print(f"O valor do seu salário atualizado é R$ {salario}")
elif salario > 3000 and salario <= 4000:
    salario = salario * 0.15 + salario
    print(f"O valor do seu salário atualizado é R$ {salario}")
else:
    salario = salario * 0.1 + salario
    print(f"O valor do seu salário atualizado é R$ {salario}")
