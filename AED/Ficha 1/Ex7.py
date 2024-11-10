sexo = str(input('Indique o Sexo (M/F): '))
print ('')
idade = int(input('Indique a idade: '))
print('')

masc = 220 - idade
fem = 226 - idade

if sexo == 'M' or sexo == 'm':
    print ('FCM: {:.0f} bpm' .format(masc))

elif sexo == 'F' or sexo == 'f':
    print ('FCM: {:.0f} bpm' .format(fem))

else:
    print ('Dados incorretos')