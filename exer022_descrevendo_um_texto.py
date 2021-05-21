nome = str(input('Digite um nome completo: '))
print('Analisando seu nome...')
print('Seu nomde em maiúsculo é {}'.format(nome.upper())) #upper coloca o nome caixa alta
print('Seu nomde em minúsculo é {}'.format(nome.lower())) #lower colocar o nome caixa baixa 
print('Seu nome tem so todo {} letras'.format(len(nome) - nome.count(' '))) # len -> conta as letras! - espaços 
print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) #primeiro nome antes do espaço entre eles