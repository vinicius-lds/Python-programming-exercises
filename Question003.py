from util.Console import get_int_input


dictionary = dict()
given_input = get_int_input(allow_zero=False, allow_negative=False)

for x in range(1, given_input + 1):
    dictionary[x] = x * x

print(dictionary)
