#  venv - виртуальное окружение

#  модули в питон


import random

print(random.randint(1,8))

from math import pi
from math import e as E
print(pi)
print(E)

from lesson3 import Bank

bank = Bank('Bank Account',19,1999)
import colorama
from art import tprint
print(colorama.Back.BLACK)
print(colorama.Fore.BLUE)
tprint('HELLO WORLD!')


p=[1,2,3,4,5,6,7,8,9]