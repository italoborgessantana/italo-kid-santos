print ("escolha umas das seguintes opçoes: 1 par ou impar, 2 numero primo, 3 fatorial, 4 soma, 5 subtração, 6 multiplicação, ou 7 divisão")
escolha = int(input(" "))
if escolha == 1:
    n1 = int(input("digite o numero que voce quer saber se é par: "))
    if n1%2 ==0:
        print (n1," é impar")
    else:
       print (n1," é par")


if escolha == 2:
    num = int(input("digite o num:"))
    div= 0

    for i in range(1, num+1):
        if num % i == 0:
            div+= 1

    if div == 2 :
        print("primo")
    else:
        print("não primo")


if escolha == 3:
    numero= int(input("Digite um número: "))
    fatorial= 1
    for i in range(1, numero+1):
     fatorial*= i
    print("O fatorial do número ", numero, "é", fatorial)


if escolha == 4:
    ns1 = int(input("digite o primeiro numero: "))
    ns2 = int(input("digite o segundo numero: "))
    soma = ns1 + ns2
    print (soma)


if escolha == 5:
    ns1 = int(input("digite o primeiro numero: "))
    ns2 = int(input("digite o segundo numero: "))
    subtração = ns1 - ns2
    print (subtração)


if escolha == 6:
    ns1 = int(input("digite o primeiro numero: "))
    ns2 = int(input("digite o segundo numero: "))
    multplicação = ns1*ns2
    print (multplicação)


if escolha == 7:
    ns1 = int(input("digite o primeiro numero: "))
    ns2 = int(input("digite o segundo numero: "))
    divisão = ns1/ns2
    print(divisão)