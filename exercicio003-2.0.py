try:
    n1 = int(input('Digite um valor:'))
    if type(n1) == int:
        print(n1)
except ValueError:
    print("Não é um valor valido")

try:
    n2 = int(input('Digite um valor:'))
    if type(n2) == int:
        print(n2)
except ValueError:
    print("Não é um valor valido")

try:
    soma = n1 + n2
    print(f'A soame entre {n1} e {n2}, resultara em {soma}')
    print('A soma entre {} e {}, resultara em {}'.format(n1, n2, soma))
except NameError:
    print("deu ruim")
