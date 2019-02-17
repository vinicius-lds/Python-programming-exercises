from util.Console import get_multiple_string_input


print(' '.join(sorted(set(get_multiple_string_input(message='Digite uma frase: ', separator=' ')))))
