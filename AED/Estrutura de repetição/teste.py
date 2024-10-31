def soma(n1,n2):
    return n1+n2

def subtracao(n1,n2):
    return n1-n2

def multiplicacao(n1,n2):
    return n1*n2

def divisao(n1,n2):
    return n1/n2

n1= int(input('Informe primeiro numero:'))
n2= int(input('Informe secundo numero:'))
op= input('Informe operacao:')

match op:
    case  '+':
        print(soma(n1,n2))
    case  '-':
        print(subtracao(n1,n2))
    case  '*':
        print(multiplicacao(n1,n2))
    case  '/':
        print(divisao(n1,n2))
        