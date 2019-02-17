from util.Console import get_multiple_int_input
from math import sqrt


C = 50
H = 30
D = get_multiple_int_input(
    message='Digite três números para serem usados como a varivel D na fórmula "Q = Square root of [(2 * C * D)/H]"\n',
    max_length=3
)
for x in D:
    print('Q={}'.format(int(sqrt((2 * C * x) / H))))
