import random

num = random.randint(1,50)
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
        break
