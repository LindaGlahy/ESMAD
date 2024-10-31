import random

n = int(input("Digite a quantidade de números: "))

maior = 0
segundo_maior = 0

for _ in range(n):
    numero = random.randint(1, 100)
    print(f"Número gerado: {numero}") 

    if maior == 0 or numero > maior:
        segundo_maior = maior
        maior = numero
    elif (segundo_maior == 0 or numero > segundo_maior) and numero != maior:
        segundo_maior = numero

if segundo_maior is None:
    print("Não há um segundo maior valor.")
else:
    print("O segundo maior valor é:", segundo_maior)

# Need to fix!!