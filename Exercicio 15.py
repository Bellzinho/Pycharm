N = 1;
contador = 1;
soma = 0
while (N > 0):
    n = int(input(f'Digite o {contador}° valor: '))
    contador += 1;
    N = n
    if n >= 0:
        soma = soma + n;

print(f'A soma dos valores digitados é: {soma}')