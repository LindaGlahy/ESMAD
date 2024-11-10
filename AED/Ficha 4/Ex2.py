import random

def generateNumbers(n1,n2,n3):
    cont = 0
    listNumber = []
    while cont < n3:
        number = random.randint(n1,n2)
        if number not in listNumber:
            listNumber.append(number)
            cont+=1
    return listNumber

resposta = "S"
while resposta.upper() == "S":
    key = generateNumbers(1,50,5)
    star = generateNumbers(1,12,2)
    print (f"Chave do Euromilhões: {key} Estrlas: {star}")
    resposta = input("Gerar nova chave (S/N): ")