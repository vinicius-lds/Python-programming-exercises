from util.Console import get_multiple_lines

total_amount = 0
deposits = list()
withdraws = list()
valid_input = False

while not valid_input:
    lines = get_multiple_lines(message='Insira as transações ocorridas.')
    for line in lines:
        valid_input = False
        if len(line) < 3 or line[1] != ' ':
            break
        type_of_transaction = line[0]
        value_of_transaction = line[2:]
        if type_of_transaction != 'D' and type_of_transaction != 'W':
            break
        try:
            value_of_transaction = int(value_of_transaction)
        except ValueError:
            break
        if type_of_transaction is 'D':
            deposits.append(value_of_transaction)
        else:
            withdraws.append(value_of_transaction)
        valid_input = True
    if not valid_input:
        print('Valores inválidos digitados!')

for deposit in deposits:
    total_amount += deposit
for withdraw in withdraws:
    total_amount -= withdraw

print('\nSaldo final: R${}'.format(total_amount))
