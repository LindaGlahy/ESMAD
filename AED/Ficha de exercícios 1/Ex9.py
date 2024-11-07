Peso = int(input('Peso (Kg): '))
print('')
Altura = float(input('Altura (m): '))
print('')
IMC = Peso/(Altura**2)

if IMC < 18.5:
    print ('Seu IMC é: {:.2f}'.format(IMC))
    print ('    Baixo Peso')

elif IMC >= 18.5 and IMC < 25:
    print ('Seu IMC é: {:.2f}'.format(IMC))
    print ('    Peso Normal')

elif IMC >= 25 and IMC < 30:
    print ('Seu IMC é: {:.2f}'.format(IMC))
    print ('    Excesso de Peso')

elif IMC >= 30 and IMC < 35:
    print ('Seu IMC é: {:.2f}'.format(IMC))
    print ('    Obesidade Grau I')

elif IMC >= 35 and IMC < 40:
    print ('Seu IMC é: {:.2f}'.format(IMC))
    print ('    Obesidade Grau II')

else:
    print ('Seu IMC é: {:.2f}'.format(IMC))
    print ('    Obesidade Mórbida')
