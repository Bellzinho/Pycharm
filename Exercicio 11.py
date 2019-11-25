contador = 1
maior = 0
while contador <= 20:
    valor = int(input(f'Digite o {contador}° valor: '))
    if valor > 8:
        maior += 1
    contador += 1
if maior == 1:
    print(f'Dos numeros digitados apenas um é maior que 8!')
else:
    print(f'Dos numeros digitados {maior} são maiores que 8!')