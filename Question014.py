from util.StringUtils import count_upper, count_lower
from util.Console import get_string_input

given_input = get_string_input(message='Digite algo: ')
print('O que você digitou tem {} letra(s) maiúscula(s) e {} letra(s) minúscula(s).'.format(
    count_upper(given_input), count_lower(given_input))
)
