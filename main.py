from Assembler import Assembler
from isa import registers, instructions


my_asm = Assembler(registers, instructions)

tokens = [["add", "x1", "x2", "x3"]]
results = my_asm.second_pass(tokens)
print(results)