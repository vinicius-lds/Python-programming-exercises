from util.Console import get_multiple_string_input
from re import search


passwords = get_multiple_string_input()
valid_passwords = [password for password in passwords
                   if 6 <= len(password) <= 12
                   and search('[a-z]', password)
                   and search('[A-Z]', password)
                   and search('[0-9]', password)
                   and search('[$#@]', password)
                   and not search('[\s]', password)
                   ]


print(', '.join(valid_passwords))
