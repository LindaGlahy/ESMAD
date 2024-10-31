'''Programa que determina em qual etapa da vida mediante a idade colocada
https://reyabogado.com/brasil/qual-a-idade-de-cada-fase-da-vida/#:~:text=Abaixo%20est%C3%A3o%20descritas%20as%209%20fases%20da%20vida,8%208.%20Velhice%20%2865%20a%2079%20anos%29%3A%20
'''

print ('\nDescubra em qual etapa da vida estais!')
idade = int(input('\nInsira sua idade: '))

if idade < 0:
    print ('\nDados invalidos')

elif idade >= 0 and idade <= 2:
    print ('\nInfância - Primeira infância')

elif idade >= 3 and idade <= 6:
    print ('\nInfância - Infância Intermediária')

elif idade >= 7 and idade <= 12:
    print ('\nInfância - Pré-adolescência')

elif idade >= 13 and idade <= 14:
    print ('\nAdolescência - Puberdade')

elif idade >= 15 and idade <= 19:
    print ('\nAdolescência - Adolescência tardia')

elif idade >= 20 and idade <= 39:
    print ('\nAdultez - Jovem adulto')

elif idade >= 40 and idade <= 59:
    print ('\nAdultez - Meia idade')

elif idade >= 60 and idade <= 74:
    print ('\nTerceira Idade - Idosos jovens')

else:
    print ('\nTerceira Idade - Idosos Velhos')
