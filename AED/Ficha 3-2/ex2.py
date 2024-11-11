def countText(text):
    '''
    Recebe um texto e devolve os números de caracteres, espaços e vogais.
    '''
    caracteres = len(text)
    vogais = text.count("A") + text.count("a") + text.count("E") + text.count("e") + text.count("I") + text.count("i") + text.count("O") + text.count("o") + text.count("U") + text.count("u")
    espacos = text.count(" ")

    print ("Nº de caracteres: ", caracteres)
    print ("Nº de vogais    : ", vogais)
    print ("Nº de espaços   : ", espacos)

text = input("Indique um texto: ")

print(countText(text))