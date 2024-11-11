import random

def jogo():
    num = random.randint(1,10)
    tent = 0
    while True:
        tent += 1
        if tent == 11:
            print ('Esgotou as 10 tentativas :(')
            break
        n1 = int(input('Indique o seu palpite: '))
        if num > n1:
            print ('O número é maior!')
        elif num < n1:
            print ('O número é menor!')
        else:
            print (f'Parabéns! Acertou em {tent} tentativas')
            tent = 0
            while True:
                r1 = input('Novo jogo? (S/N):')
                if r1 == 'S':
                    num = random.randint(1,10)
                    break
                elif r1  == 'N':
                    return
                else:
                    print ('Resposta incorreta!')

jogo()
print('Tchau!')