texto = str(input("Indique um texto: "))

caracteres = texto.count(texto[0:])
espacos = texto.count(" ")
vogais = texto.count("a") + texto.count("e") + texto.count("i") + texto.count("o") + texto.count("u")

print ("Nº de caracteres:", caracteres)
print ("Nº de vogais:", vogais)
print ("Nº de espaços:", espacos)