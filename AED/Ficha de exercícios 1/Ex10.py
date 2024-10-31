'''Simulador de peso noutros planetas,em função da seu gravidade relativa
https://ecoosfera.com/sci-innovacion/cuanto-pesarias-en-otros-planetas/
'''

print ('      Planetas')
print ('    1 - Mercúrio')
print ('    2 - Venus')
print ('    3 - Marte')
print ('    4 - Júpiter')
print ('    5 - Saturno')
print ('    6 - Urano')

peso_terra = float(input('\nIndique o seu peso (Kg): '))

planet = int(input('\nIndique o código do planeta: '))

match planet:
    case 1:
        peso_final = peso_terra * 0.37
    case 2:
        peso_final = peso_terra * 0.90
    case 3:
        peso_final = peso_terra * 0.37
    case 4:
        peso_final = peso_terra * 0.53
    case 5:
        peso_final = peso_terra * 1.06
    case 6:
        peso_final = peso_terra * 0.91

print (f'\nO seu peso de {peso_terra} Kg no planeta {planet} seria de {peso_final} Kg')
