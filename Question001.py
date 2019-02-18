DIVISIBLE = 5
NON_DIVISIBLE = 7

LOWER_LIMIT = 2000
HIGHER_LIMIT = 3200

# Resolution
final_list = list()
for x in range(LOWER_LIMIT, HIGHER_LIMIT):
    if x % DIVISIBLE == 0 and x % NON_DIVISIBLE != 0:
        final_list.append(x)
print(final_list)
