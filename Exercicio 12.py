contador = 1
par = 0
while contador <= 20:
    n = int(input(f'Digite o {contador}° valor: '))
    if n % 2 == 0:
        par += 1
    contador += 1
if par == 0:
    print('Não foram digitados números pares!')
elif par == 1:
    print('Apenas um nuúmero é par!')
else:
    print(f'Foram digitados {par} números pares!')