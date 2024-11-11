def invertText(text):
    '''
    Recebe um texto e  imprime o mesmo texto, mas por ordem inversa.
    '''
    invert = text[::-1]
    return invert

text = input("Indique um texto: ")

print(invertText(text))