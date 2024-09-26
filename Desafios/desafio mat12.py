carro = int(input('Escolha o carro que voce quer: '
                  '\nFusca (1)'
                  '\nFiesta(2)'
                  '\nCamaro(3)'))
dia = int(input('Escolha por quantos dias voce usou: '))
precodia= dia * 60 * carro
km = float(input('Por quantos km voce rodou?'))
kmp = km * 0.15
pagar = precodia * kmp
print('Voce escolheu o carro {},andou por {} dias e percorreu {}kms, seu total ficou: {}'
      .format(carro, dia, km,pagar))

