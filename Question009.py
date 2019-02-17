from util.Console import get_string_input

is_running = True
list_of_sentences = list()
while is_running:
    word = get_string_input()
    if word == 'ext':
        is_running = False
    else:
        list_of_sentences.append(word.capitalize())
print('\n'.join(list_of_sentences))
