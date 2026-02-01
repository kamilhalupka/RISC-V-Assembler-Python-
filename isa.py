# Create dictionary of registers
registers = {f"x{i}": format(i, '05b') for i in range(32)} 

# Create list of ABI names
abiNames = ["zero", "ra", "sp", "gp", "tp",
            "t0", "t1", "t2", "s0", "s1",
            "a0", "a1", "a2", "a3", "a4",
            "a5", "a6", "a7", "s2", "s3",
            "s4", "s5", "s6", "s7", "s8",
            "s9", "s10", "s11", "t3", "t4",
            "t5", "t6"]

# Map ABI names to binary in dictionary
for i, name in enumerate(abiNames):
    registers[name] = format(i, '05b')

# Format: {"opcode": , "funct3": , "funct7": , "type": }
instructions = {
    # loads
    "lb" : {"opcode": "0000011", "funct3": "000", "funct7": "0000000", "type": "I"},
    "lh" : {"opcode": "0000011", "funct3": "001", "funct7": "0000000", "type": "I"},
    "lw" : {"opcode": "0000011", "funct3": "010", "funct7": "0000000", "type": "I"},

    # arithmetic immediate
    # arithmetic immediate
    "addi"  : {"opcode": "0010011", "funct3": "000", "funct7": "0000000", "type": "I"},
    "slli"  : {"opcode": "0010011", "funct3": "001", "funct7": "0000000", "type": "I"},
    "slti"  : {"opcode": "0010011", "funct3": "010", "funct7": "0000000", "type": "I"},
    "sltiu" : {"opcode": "0010011", "funct3": "011", "funct7": "0000000", "type": "I"},
    "xori"  : {"opcode": "0010011", "funct3": "100", "funct7": "0000000", "type": "I"},
    "srli"  : {"opcode": "0010011", "funct3": "101", "funct7": "0000000", "type": "I"},
    "srai"  : {"opcode": "0010011", "funct3": "101", "funct7": "0100000", "type": "I"},
    "ori"   : {"opcode": "0010011", "funct3": "110", "funct7": "0000000", "type": "I"},
    "andi"  : {"opcode": "0010011", "funct3": "111", "funct7": "0000000", "type": "I"},

    # U-type
    "lui"   : {"opcode": "0110111", "funct3": "000", "funct7": "0000000", "type": "U"},
    "auipc" : {"opcode": "0010111", "funct3": "000", "funct7": "0000000", "type": "U"},

    # S-type (Stores)
    "sb"    : {"opcode": "0100011", "funct3": "000", "funct7": "0000000", "type": "S"},
    "sh"    : {"opcode": "0100011", "funct3": "001", "funct7": "0000000", "type": "S"},
    "sw"    : {"opcode": "0100011", "funct3": "010", "funct7": "0000000", "type": "S"},

   # R-type
    "add"   : {"opcode": "0110011", "funct3": "000", "funct7": "0000000", "type": "R"},
    "sub"   : {"opcode": "0110011", "funct3": "000", "funct7": "0100000", "type": "R"},
    "sll"   : {"opcode": "0110011", "funct3": "001", "funct7": "0000000", "type": "R"},
    "slt"   : {"opcode": "0110011", "funct3": "010", "funct7": "0000000", "type": "R"},
    "sltu"  : {"opcode": "0110011", "funct3": "011", "funct7": "0000000", "type": "R"},
    "xor"   : {"opcode": "0110011", "funct3": "100", "funct7": "0000000", "type": "R"},
    "srl"   : {"opcode": "0110011", "funct3": "101", "funct7": "0000000", "type": "R"},
    "sra"   : {"opcode": "0110011", "funct3": "101", "funct7": "0100000", "type": "R"},
    "or"    : {"opcode": "0110011", "funct3": "110", "funct7": "0000000", "type": "R"},
    "and"   : {"opcode": "0110011", "funct3": "111", "funct7": "0000000", "type": "R"},

    # SB-type (Branches)
    "beq"   : {"opcode": "1100011", "funct3": "000", "funct7": "0000000", "type": "SB"},
    "bne"   : {"opcode": "1100011", "funct3": "001", "funct7": "0000000", "type": "SB"},
    "blt"   : {"opcode": "1100011", "funct3": "100", "funct7": "0000000", "type": "SB"},
    "bge"   : {"opcode": "1100011", "funct3": "101", "funct7": "0000000", "type": "SB"},
    "bltu"  : {"opcode": "1100011", "funct3": "110", "funct7": "0000000", "type": "SB"},
    "bgeu"  : {"opcode": "1100011", "funct3": "111", "funct7": "0000000", "type": "SB"},

    # Jump
    "jal"   : {"opcode": "1101111", "funct3": "000", "funct7": "0000000", "type": "UJ"},
    "jalr"  : {"opcode": "1100111", "funct3": "000", "funct7": "0000000", "type": "I"},

    # System
    "ecall" : {"opcode": "1110011", "funct3": "000", "funct7": "0000000", "type": "SYS"},
    "wfi"   : {"opcode": "1110011", "funct3": "000", "funct7": "0001000", "type": "SYS"}

}