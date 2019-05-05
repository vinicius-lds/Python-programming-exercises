ext = False

while not ext:
    x = input('Type in what you want to see the documentation for: ')
    try:
        print(help(x))
    except:
        print('Sorry, there seem\'s to be a problem with what you want to see!')
    ext = input('Press Y to see another one... ').upper() != 'Y'

