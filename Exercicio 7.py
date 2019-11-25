soma = 0
contador = 1
for i in range(1, 21):
    idade = int(input(f'Digite a idade da {contador}° pessoa: '))
    contador += 1
    soma = soma + idade
print(f'A média das idades informadas é: {soma/20}')