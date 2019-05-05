phrase = input('Type in a phrase.\n')

words = phrase.split(' ')
words.sort()
result = dict()

for word in words:
    if not word in result:
        result[word] = words.count(word)

for word in result:
    print(f'{word} - {result[word]}')
