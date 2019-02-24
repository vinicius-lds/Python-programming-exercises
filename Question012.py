from util.StringUtils import is_every_digit_even


result = list()
for x in range(1000, 3001):
    if is_every_digit_even(x):
        result.append(str(x))
print(', '.join(result))
