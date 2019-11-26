contador = 1;
a = 0;
while contador <= 20:
    n = int(input(f'Digite o {contador}° valor: '));
    if (n >= 0 and n <= 100):
        a = a + 1;
    contador += 1;
if a == 0:
    print(f'Não foram digitados nenhum entre 0 e 100!')
elif a == 1:
    print(f'Apenas um numero digitado está entre 0 e 100!')
else:
    print(f'Foram digitados {a} números entre 0 e 100!')
