ts = list()
ext = False

while not ext:
    name = input('Type in the name: ')
    age = input('Type in the age: ')
    score = input('Type in the score: ')

    ts.append((name, age, score))

    c = input('Press Y to continue... ')
    ext  = c.upper() == 'Y'

ts.sort(key=lambda t: (t[0], t[1], t[2]))
print(ts)
