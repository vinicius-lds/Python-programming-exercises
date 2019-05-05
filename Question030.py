def print_largest(x, y):
    l = x if len(x) > len(y) else y
    l = l if len(x) != len(y) else f'{x}\n{y}'
    print(l)

print_largest('a', 'bb')
