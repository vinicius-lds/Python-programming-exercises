from util.Console import get_int_input

ext = False
while not ext:
    x = get_int_input(message='Number to square: ')
    print(x ** 2)
    ext = input('Press Y to continue... ').upper() != 'Y'
