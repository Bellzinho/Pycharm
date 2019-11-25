soma = 0
contador = 1
while contador <= 10:
    valor = int(input(f'Digite o {contador}° valor: '))
    contador += 1
    soma = soma + valor
print(f'A soma dos 10 numeros é: {soma}')