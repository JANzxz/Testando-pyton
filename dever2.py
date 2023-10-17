from random import randint

lista = []
resultado_da_soma = 0
for n in range(10):
    lista.append(randint(1, 30))

    for i in lista:
        if (i % 2) == 0:
            resultado_da_soma = resultado_da_soma + i

    print(f' O resoltado da soma e: {resultado_da_soma}')
    print(lista)