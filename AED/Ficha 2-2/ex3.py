import random

numero = random.randint(0,50)

numeroTent = 0
while numeroTent < 10:
    tentativa = (int(input("Aivinhe o número: ")))
    if numero > tentativa:
        numeroTent += 1
        print ("O número é maior")
    elif numero < tentativa:
        numeroTent += 1
        print ("O número é menor")
    elif numero == tentativa:
        print (f"Parabéns, acertou em {numeroTent} tentativas")
        break
    if numeroTent == 10:
        print ("Esgotou as 10 tentativas :(")

        