import random

def generatePassword(userName):
    if ' ' in userName:
        return "username é inválido"
    
    password = ''.join(userName[i] + str(random.randint(1, 9)) for i in range(0, len(userName), 2))
    finalPassword =  password + str(len(userName))
    print(finalPassword)

userName = str(input("Username: "))
generatePassword(userName)