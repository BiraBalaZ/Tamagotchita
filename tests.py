from time import sleep
from os import system
import colors as c

# Cleaning Terminal
system('cls')

# Declarating initial variables
var1 = 1
var2 = 2
var3 = 3

# Tests
try:
    assert var3 - var2 == var1
except AssertionError as error:
    print(f"var1 = {var1}")
    raise error
sleep(1)
print(f'Primeira variável = {var1}', end=' ')
sleep(1)
c.colored_print(c.c_green, "✓")

try:
    assert var3 - var1 == var2
except AssertionError as error:
    print(f"var2 = {var2}")
    raise error
sleep(1)
print(f'Segunda  variável = {var2}', end=' ')
sleep(1)
c.colored_print(c.c_green, "✓")

try:
    assert var1 + var2 == var3
except AssertionError as error:
    print(f"var3 = {var3}")
    raise error
sleep(1)
print(f'Terceira variável = {var3}', end=' ')
sleep(1)
c.colored_print(c.c_green, "✓")

# End of the tests
sleep(1)
print('The code passed in all tests =D')
sleep(.5)
print('Congratulations!')