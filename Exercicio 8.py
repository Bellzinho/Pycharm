soma = 0
contador = 1
maior = 0
for i in range(1, 21):
    idade = int(input(f'Digite a idade da {contador}° pessoa: '))
    if idade >= 18:
        maior = maior + 1
    contador += 1

if maior == 1:
    print(f'Entre as idades apresentadas, apenas uma pessoa é maior de idade!')
else:
    print(f'Entre as idades apresentadas, {maior} pessoas são maiores de idade!')

