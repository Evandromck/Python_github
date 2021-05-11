import random
al1 = str(input('Digite o primeiro aluno:'))
al2 = str(input('Digite o segundo aluno: '))
al3 = str(input('Digite o terceiro aluno:'))
al4 = str(input('Digite o quarto aluno: '))
lista = [al1, al2, al3, al4]
random.shuffle(lista)
print('A ordem vai ser ')
print(lista)
