from util.Console import get_int_input
from util.Console import print_two_dimensional_array

row_number = get_int_input(message='X=')
col_number = get_int_input(message='Y=')
two_dimensional_array = [
    [0 for col in range(col_number)]
    for row in range(row_number)
]

print_two_dimensional_array(two_dimensional_array)
