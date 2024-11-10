sexo = str(input('\nIndique o sexo (M/F): '))
altura = int(input('\nIndique a altura (cm): '))

if sexo == 'M' or sexo == 'm':
    peso_ideal = (altura-100) - (altura-150)/4
    print ('\nO Peso Ideal é {:.2f} Kg' .format(peso_ideal))

elif sexo == 'F' or sexo == 'f':
    peso_ideal = (altura-100) - (altura-150)/2
    print ('\nO Peso Ideal é {:.2f} Kg' .format(peso_ideal))

else:
    print ('\nDados incorretos')