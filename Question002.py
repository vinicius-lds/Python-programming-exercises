from util.Console import get_int_input

given_input = get_int_input(allow_negative=False, allow_zero=False)

for x in range(given_input - 1, 1, -1):
    given_input *= x

print(given_input)
