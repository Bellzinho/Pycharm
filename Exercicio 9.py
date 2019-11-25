contador = 1
menor = 999999
for i in range(1, 4):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    if idade < menor:
        menor = idade
        nomen = nome
    contador += 1
if menor == 1:
    print(f'A pessoa mais nova é {nomen} e tem {menor} ano!')
elif menor == 0:
    print(f'A pessoa mais nova é {nomen} e é um recém nascido!')
else:
    print(f'A pessoa mais nova é {nomen} e tem {menor} anos')

