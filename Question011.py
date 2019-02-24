from util.Console import get_multiple_string_input
from util.StringUtils import is_valid_binary_string, binary_to_integer


binary_strings = get_multiple_string_input(
    message='Digite uma sequencia de números binários separados por vírgula.\n',
    size=4,
    string_validator=is_valid_binary_string
)
result = list()
for binary_string in binary_strings:
    if binary_to_integer(binary_string) % 5 == 0:
        result.append(binary_string)
print(', '.join(result))

# The function int(binary_string, 2) could've been used too
# I've opted for this solution just so I could develop the
# binary_to_integer function
