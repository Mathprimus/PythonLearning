import math
cateto_oposto = float(input('Coloque o valor do cateto oposto: '))
cateto_adjacente = float(input('Coloque o valor do cateto adjacente: '))
hipotenusa = (cateto_oposto**2 + cateto_adjacente**2)**(1/2)
print(f'O valor da hipotenusa é: {hipotenusa:.2f}')
h1 = math.hypot(cateto_oposto, cateto_adjacente)
print(f'A hipotenusa calculada pelo math é: {h1:.2f}')
