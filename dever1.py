from random import randint

Q = []

for numero in range (20):
    Q.append(randint(1, 100))

print(Q)

#Variavel de controle

maior = -1
menor = 101

for item_da_lista in Q:

    if maior < item_da_lista:
        maior = item_da_lista

    if menor > item_da_lista:
        menor = item_da_lista

        print(f'valor maximo: {maior}')
        print(f'valor minimo{menor}')
