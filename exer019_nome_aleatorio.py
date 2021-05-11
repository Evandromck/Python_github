import random
al1 = str(input('Digite o primeiro nome:'))
al2 = str(input('Digite o segundo nome: '))
al3 = str(input('Digite o terceiro: '))
al4 = str(input('Digite o quarto: '))
lista = [al1, al2, al3, al4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido)) 
