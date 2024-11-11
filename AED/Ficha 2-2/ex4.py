import random

def jogo():
    numero = random.randint(0,10)
    tent = 0
    while True:
        tent += 1
        palpite = (int(input("Adivinhe o número: ")))
        if numero > tentativa:
            print ("O número é maior")
        elif numero < tentativa:
            print ("O número é menor")
        elif numeroTent == 10:
            print ("Esgotou as 10 tentativas :(")
            break
        elif numero == palpite:
            print (f"Parabéns, acertou em {tent} tentativas")
            tent = 0
            while True:
                novoJogo = (input("Novo jogo? (S/N): "))
                if novoJogo == "S" or "s":
                    numero = random.randint(0,10)
                    break
                elif novoJogo == "N" or "n": # Não funicona direito, WHY?
                    return
                else:
                    print("Insira um valor válido!")

jogo ()
print("Obrigado por jogar!")