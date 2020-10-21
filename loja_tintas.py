area = int(input("Informe a quantidade que será pintada:"))

litros = area // 3
if area % 3 > 0:
    litros = litros + 1
    if litros <= 18:
        print(f"Para pintar a área {area}, você precisará de {litros} e custará R$ 80,00")
    if litros <= 36:
        print(f"Para pintar a área {area}, você precisará de {litros} e custará R$ 160,00")
    else:
        print(f"Para pintar a área {area}, você precisará de {litros} e custará R$ 240,00")
