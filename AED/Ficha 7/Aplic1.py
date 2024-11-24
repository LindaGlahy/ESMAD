import os
from unicodedata import normalize

listaContin = ["EUROPA", "AMERICA", "AFRICA", "ASIA", "OCEANIA"]

def menu():
    os.system('clear')

    print ("\t\t   MENU")
    print ("\a -----------------------------------------")
    print ("\n\t 1 - Inserir paises")
    print ("\a\t 2 - Consulta paises")
    print ("\a\t 3 - Consulta por continente ")
    print ("\a\t 4 - Consulta nº paises")
    print ("\a\t 5 - Sair")
    
    opcao = int(input("\n\t Opção: "))

    if opcao == 1:
        inserePaises()
    
    elif opcao == 2:
        consultaPaises()
    
    elif opcao == 3:
        consultaContin()
    
    elif opcao == 4:
        consultaNum()

    else:
        os.system('clear')
        print ("Volte sempre!")

def inserePaises():
    ''''
    Adiciona País e Continente indicados pelo utilizador ao ficheiro [paises.txt]
    '''

    while True:
        os.system('clear')

        país = input("País: ")
        pais = normalize('NFKD', país).encode('ASCII','ignore').decode('ASCII')

        continê = input ("Continente: ")
        contin = normalize('NFKD', continê).encode('ASCII','ignore').decode('ASCII')

        escreve = "\n" + pais.upper() + ";" + contin.upper()
        readFile = open("paises.txt", "r", encoding="utf-8")
        listaFile = readFile.readlines()
        readFile.close()

        # há um erro quanto a leitura correta desta parte do código...
        for linha in listaFile:
            if pais == linha.split(";")[0]:
                print(f"O país '{pais}' já existe na lista.")
                input("Pressione Enter para continuar...")
                return
        for linha in listaFile:
            readFile = open("paises.txt", "r", encoding="utf-8")
            if contin == linha.split(";")[1]:
                print ("Por favor insira um continente válido")
                input ("Pressione Enter para continuar...")
                return
                
        addFile = open("paises.txt", "a", encoding="utf-8")
        addFile.write(escreve)
        addFile.close()
        print ("O país e o continente foram adicionados a lista")

        input ("\nPressione Enter para voltar ao menu...")
        if input:
            menu()

def consultaPaises():
    '''
    Mostra lista dos países e continentes existentes no ficheiro [paises.txt]
    '''
    os.system('clear')

    print ("\t Países \t\t Continente")
    print ("-------------------------------------------")

    fPaises = open ("paises.txt", "r", encoding="utf-8")
    listaFile = fPaises.readlines()
    fPaises.close()

    for linha in listaFile:
        campos = linha.split(";")
        if len(campos[1]) <= 6:
            print ("\t", campos[0], "\t\t\t", campos[1])
        else:
            print ("\t", campos[0], "\t\t", campos[1])

    input("\nPressione Enter para voltar ao menu...")
    if input:
        menu()

    
def consultaContin():
    '''
    Mostra lista dos países e continentes existentes no ficheiro [paises.txt]
    '''

    os.system('clear')

    continêSearch = input("Indique o continente de procura: ")
    continSearch = normalize('NFKD', continêSearch).encode('ASCII','ignore').decode('ASCII')
    fPaises = open ("paises.txt", "r", encoding="utf-8")
    listaFile = fPaises.readlines()
    fPaises.close()

    print ("\n\t Países \t\t Continente")
    print ("--------------------------------------------------")

    # Não está imprimido a lista...
    for linha in listaFile:
        campos = linha.split(";")
        if continSearch.upper == campos[1].strip():
            if len(campos[1]) <= 6:
                print ("\t", campos[0], "\t\t\t", campos[1])
            else:
                print ("\t", campos[0], "\t\t", campos[1])

    input("\nPressione Enter para voltar ao menu...")
    if input:
        menu()

def consultaNum():
    '''
    '''
    os.system('clear')

    fPaises = open ("paises.txt", "r", encoding="utf-8")
    listaFile = fPaises.readlines()
    fPaises.close()
    
    europa = 0
    america = 0
    africa = 0
    asia = 0
    oceania = 0

    for linha in listaFile:
        campos = linha.split(";")[1].strip()

        if campos == "EUROPA":
            europa += 1

        elif campos == "AMERICA":
            america += 1

        elif campos == "AFRICA":
            africa += 1

        elif campos == "ASIA":
            asia += 1

        elif campos == "OCEANIA":
            oceania += 1

    print ("\t Nº países \t Continente")
    print ("-----------------------------------------------")
    print ("\t", europa, "\t\t", "Europa")
    print ("\t", america, "\t\t", "America")
    print ("\t", africa, "\t\t", "Africa")
    print ("\t", asia, "\t\t", "Asia")
    print ("\t", oceania, "\t\t", "Oceania")

    input ("\nPressione Enter para voltar ao menu...")
    if input:
        menu()

menu()