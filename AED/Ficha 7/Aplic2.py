import os

def menu():
    '''
    Menu para consultas
    '''
    os.system('clear')

    print ("\t\t   MENU")
    print ("\a -----------------------------------------")
    print ("\n\t 1 - Consulta por dada")
    print ("\a\t 2 - Consulta estatistica")
    print ("\a\t 0 - Sair")
    
    opcao = int(input("\n\t Opção: "))

    if opcao == 1:
        consultaData()
    
    elif opcao == 2:
        consultaEstatist()

    else:
        os.system('clear')
        print ("Volte sempre!")

def consultaData():
    '''
    '''

    os.system('clear')

    dataSearch = input("Data da consulta (AAAA-MM-DD): ")
    fTemp = open ("temperatura.txt", "r", encoding="utf-8")
    listaFile = fTemp.readlines()
    fTemp.close()

    print ("\n\t Data \t\t Hora \t\t Temperatura")
    print ("--------------------------------------------------")

    for linha in listaFile:
        campo = linha.split(";")
        if dataSearch == campo[0].strip():
            print ("\t", campo[0], "\t", campo[1], "\t", campo[2])

    input("\nPressione Enter para voltar ao menu...")
    if input:
        menu()

def consultaEstatist():
    '''
    '''
    fTemp = open("temperatura.txt", "r", encoding="utf-8")

    temperaturas = []

    for linha in fTemp:
        campos = linha.strip().split(";")
        if len(campos) > 2:
            try:
                temperaturas.append(float(campos[2]))
            except ValueError:
                print(f"Erro ao processar temperatura na linha: {linha.strip()}")

    # OU || temperaturas = [float(linha.split(";")[2]) for linha in arquivo if len(linha.split(";")) > 2] ||

    fTemp.close()

    maiorTemp = max(temperaturas)
    menorTemp = min(temperaturas)
    mediaTemp = sum(temperaturas) / len(temperaturas)
        

    print ("\n\t\tO maior valor de temperatura registada foi de ", maiorTemp)
    print ("\t\tO menor valor de temperatura registada foi de ", menorTemp)
    print ("\t\tO valor médio de temperatura registada foi de {:.2f}" .format(mediaTemp))

    input("\nPressione Enter para voltar ao menu...")
    if input:
        menu()


menu()