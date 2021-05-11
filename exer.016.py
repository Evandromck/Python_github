#16 de float para int 
from math import trunc
num = float(input('digite um valor com virgula '))
print('Seu valor {} com formatação int {}'.format(num, trunc(num)))
print('Seu valor {} com formatação int {}'.format(num, int(num)))