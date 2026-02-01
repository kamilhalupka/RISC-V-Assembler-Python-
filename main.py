from Assembler import Assembler
from isa import registers, instructions
import os


my_asm = Assembler(registers, instructions)

print("Python RISC_V Assembler\n---------------------")
filename = input("Enter the filepath for the RISC-V file:")
if not filename.endswith(('.s', '.asm')):
    print("Warning: This doesn't look like a RISC-V assembly file!")

name_only = os.path.splitext(filename)[0]

with open(filename, 'r') as file:
    file_lines = file.read().splitlines()

cleaned_lines = my_asm.clean_lines(file_lines)
my_asm.first_pass(cleaned_lines)
hex_conversion = my_asm.second_pass(cleaned_lines)

output_filename = name_only + ".hex"
with open(output_filename, 'w') as f:
    for line in hex_conversion:
        f.write("x" + line + "\n")