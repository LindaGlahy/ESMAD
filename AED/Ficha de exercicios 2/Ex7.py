num = int(input("Indique um número: "))

divisores = 0
for i in range(1,num):
    if num % i == 0:
        divisores += int(i)

if divisores == num:
    print (f"O número {num} é um número perfeito")
else:
    print (f"O número {num} não é um número perfeito")
