import math
valor = float(input('Digite o angulo que voce desejea:'))
angulo = math.radians(valor)
seno = math.sin(angulo)
tangente = math.tan(angulo)
cosseno = math.cos(angulo)
print(f'O angulo é: {valor}'
      f'\n seu seno é: {seno:.2f}'
      f'\n sua tangente é: {tangente:.2f}'
      f'\n seu cosseno é: {cosseno:.2f}')
