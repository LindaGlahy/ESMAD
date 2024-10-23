print ('')
print ('Recebeu um tempo de contrato em meses e quer saber quanto fica em anos?')
print ('Descubra agora!')
print ('')
fim = 1
while fim == 1:
    contrato = float (input('Insira o tempo em meses:'))

    print ('')

    contrato_anos = int(contrato / 12)
    contrato_meses = int(contrato % 12)

    if contrato_anos <= 0 and contrato_meses >= 0:
        print("Seu contrato tem um total de " + str(contrato_meses) + " meses")

    elif contrato_anos <= 0 and contrato_meses == 1:
        print("Seu contrato tem um total de " + str(contrato_meses) + " mes")

    elif contrato_anos == 1 and contrato_meses == 0:
        print("Seu contrato tem um total de " + str(contrato_anos) + " ano")

    elif contrato_anos > 1 and contrato_meses == 0:
        print("Seu contrato tem um total de " + str(contrato_anos) + " anos")

    elif contrato_anos > 1 and contrato_meses == 1:
        print("Seu contrato tem um total de " + str(contrato_anos) + " anos e " + str(contrato_meses) + " mes")

    elif contrato_anos == 1 and contrato_meses > 1:
        print("Seu contrato tem um total de " + str(contrato_anos) + " ano e " + str(contrato_meses) + " meses")

    elif contrato_anos == 1 and contrato_meses == 1:
        print("Seu contrato tem um total de " + str(contrato_anos) + " ano e " + str(contrato_meses) + " mes")

    else:
        print("Seu contrato tem um total de " + str(contrato_anos) + " anos e " + str(contrato_meses) + " meses")

    print ('')
    import time
    time.sleep (2)

    print ('Gostava de reiniciar o programa? 1:Sim / 2:Nao')
    fim = (int(input('Eu escolho:')))
    print ('')

    if fim == 1:
        print ('Entao vamos de novo!')
    
    elif fim == 2:
        print ('Obrigado e volte em breve ;)')
        print ('')
        time.sleep (1)
        print('By Linda') 