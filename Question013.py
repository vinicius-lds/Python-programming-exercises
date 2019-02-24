from util.StringUtils import count_digits, count_letters
from util.Console import get_string_input

given_input = get_string_input(message='Digite algo: ')
print('O que você digitou tem {} letra(s) e {} digito(s).'.format(
    count_letters(given_input), count_digits(given_input))
)
