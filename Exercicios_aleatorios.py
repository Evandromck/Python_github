import random

for p in range(1, 6):
    print('-'*30)
    print(' ')
    print(' ')
    ex = 'Digite um numero para saber seu sucessor e seu antecessor'
    ex1 = 'A media de um aluno'
    ex2 = 'metros para centimetros'
    lista = [ex, ex1, ex2]
    escolhido = random.choice(lista)
    print('{}'.format(escolhido))
    print(' ')
    print(' ')
    print('-'*30)

    if escolhido == ex :
        print(' ')
        n = int(input('Ver resposta 1 . 0'))
        if n == 1:
            print(' ')
            print('n1 = int input Digite um numero para saber seu sucessor e seu antecessor')
            print('a = n1 - 1')
            print('b = n1 + 1')
            print('seu numero é { e o seu antecessor é { e o sucessor é {".formatn1, a, b')
            print(' ')

    if escolhido == ex1 :
        print(' ')
        n = int(input('Ver resposta 1 . 0'))
        if n == 1:
            print(' ')
            print('n1 = int (input ( Digite a primeira nota')
            print('n2 = int (input ( Digite a segunda nota  )')
            print('a = n1 + n2')
            print('s = a / 2') 
            print ('sua nota foi { e seu media é {} forma(a, s)')  
            print(' ')     
