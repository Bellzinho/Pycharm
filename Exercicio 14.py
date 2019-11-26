contador = 1;
a = 0;
b = 0;
c = 0;
while contador <= 4:
    n = int(input(f'Digite o {contador}° valor: '));
    if (n >= 0 and n <= 100):
        a = a + 1;
    elif (n >=101 and n <= 200):
        b += 1
    else:
        c += 1
    contador += 1;

if a == 0:
    print(f'Não foram digitados nenhum número entre 0 e 100!')
elif a == 1:
    print(f'Apenas um número digitado está entre 0 e 100!')
else:
    print(f'Foram digitados {a} números número entre 0 e 100!')
if b == 0:
    print(f'Não foram digitados nenhum número entre 101 e 200!')
elif b == 1:
    print(f'Apenas um número digitado está entre 200 e 200!')
else:
    print(f'Foram digitados {b} números entre 101 e 200!')
if c == 0:
    print(f'Não foram digitados nenhum número acima de 200!')
elif c == 1:
    print(f'Apenas um número digitado é maior que 200!')
else:
    print(f'Foram digitados {c} números maiores que 200!')