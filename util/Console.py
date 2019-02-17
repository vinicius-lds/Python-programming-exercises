def get_int_input(**kwargs):
    message = kwargs.get('message') if kwargs.get('message') else 'Digite um número: '

    parse_error_message = \
        kwargs.get('parse_error_message') if kwargs.get('parse_error_message') else 'Você deve digitar um número!'

    allow_negative = kwargs.get('allow_negative') if kwargs.get('allow_negative') else True

    negative_error_message = \
        kwargs.get('negative_error_message') \
        if kwargs.get('negative_error_message') \
        else 'Não são permitidos números negativos!'

    allow_zero = kwargs.get('allow_zero') if kwargs.get('allow_zero') else True

    zero_error_message = \
        kwargs.get('zero_error_message') if kwargs.get('zero_error_message') else 'Não são permitidos 0\'s'

    is_running = True

    while is_running:
        try:
            x = int(input(message))
            if not allow_negative and x < 0:
                print(negative_error_message)
            elif not allow_zero and x == 0:
                print(zero_error_message)
            else:
                return x
        except ValueError:
            print(parse_error_message)
    return x


def get_multiple_int_input(
        message='Digite uma sequencia de números separados por vírgula:\n',
        parse_error_message='Sequencia de digitos inválida!',
        max_length=-1,
        min_length=-1,
        size=-1,
        list_size_error_message='O tamanho da lista é inválido!',
        separator=','
):
    if size >= 0:
        max_length = size
        min_length = size
    is_running = True
    is_valid = True
    final_list = list()
    while is_running:
        given_input = input(message)
        for x in given_input.split(sep=separator):
            try:
                final_list.append(int(x.strip()))
                is_valid = True
            except ValueError:
                print(parse_error_message)
                is_valid = False
                final_list.clear()
                break
        if is_valid:
            if min_length >= 0 and min_length > len(final_list)\
                    or 0 <= max_length < len(final_list):
                print(list_size_error_message)
                final_list.clear()
            else:
                is_running = False
    return final_list # if max_length < 0 else final_list[0:max_length]


def get_string_input(message='Digite uma palavra: '):
    return input(message)


def get_multiple_string_input(
        message='Digite uma sequencia de palavras separados por vírgula:\n',
        max_length=-1,
        min_length=-1,
        size=-1,
        list_size_error_message='O tamanho da lista é inválido!',
        separator=','
):
    if size >= 0:
        max_length = size
        min_length = size
    is_running = True
    final_list = list()
    while is_running:
        given_input = input(message)
        for x in given_input.split(sep=separator):
            final_list.append(x)
        if min_length >= 0 and min_length > len(final_list)\
                or 0 <= max_length < len(final_list):
            print(list_size_error_message)
            final_list.clear()
        else:
            is_running = False

    return final_list # if max_length < 0 else final_list[0:max_length]


def print_two_dimensional_array(two_dimensional_array):
    for x in range(len(two_dimensional_array)):
        for y in range(len(two_dimensional_array[x])):
            print('{} '.format(two_dimensional_array[x][y]), end='')
        print()
