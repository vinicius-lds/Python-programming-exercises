from util.Console import get_int_input
import math


up = get_int_input(message='UP ', allow_negative=False)
down = get_int_input(message='DOWN ', allow_negative=False)
right = get_int_input(message='RIGHT ', allow_negative=False)
left = get_int_input(message='LEFT ', allow_negative=False)

coordinates = [0, 0]
coordinates[0] += up
coordinates[0] -= down
coordinates[1] += right
coordinates[1] -= left

print(int(round(math.sqrt(coordinates[1]**2+coordinates[0]**2))))
