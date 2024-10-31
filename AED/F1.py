def soma(n1,n2):
    soma = 0
    for i in range(n1,n2+1):
        soma += i
    return soma

n1 = int(input('indiqueo valor inferior: '))
n2 = int(input('indiqueo valor superior: '))
print (soma(n1,n2))