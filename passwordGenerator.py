import random
import string

from symtable import Symbol
LETTERS = string.ascii_letters
NUMS = '0123456789'
SPE = '-+*&$!_'
Symbols = LETTERS + NUMS + SPE
len = int(input("ENTER PASS. LENGTH"))
password = "".join(random.sample(Symbols, len))
print(password)