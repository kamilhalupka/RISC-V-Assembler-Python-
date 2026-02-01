import isa


class Assembler:
    def __init__(self, registers, instructions):
        self.symbol_table = {}
        self.registers = registers
        self.instructions = instructions

    def clean_lines(self, file_lines):
        tokens_list = []
        token = ""
        
        for line in file_lines:
            token = line.split("#")[0]
            token = token.strip()

            if not token:
                continue

            token = token.replace(":", ": ")
            token = token.replace(",", " ")
            token = token.split()
            tokens_list.append(token)

        return tokens_list

    def first_pass(self, tokens_list):
        PC = 4194304 # 0x00400000 in hex
        
        for tokens in tokens_list:
            if tokens[0].endswith(":"):
                label = tokens[0][:-1]
                self.symbol_table[label] = PC
                
                if len(tokens) == 1:
                    continue
                
            PC += 4
            
        pass

    def second_pass(self, tokens_list):
        PC = 4194304 # 0x00400000 in hex
        hex_lines = []
        
        for tokens in tokens_list:
            instruction = tokens[0]
            instruction_info = self.instructions[instruction]
            inst_type = instruction_info["type"]
            
            opcode = instruction_info["opcode"]
            funct3 = instruction_info["funct3"]
            funct7 = instruction_info["funct7"]
            
            if inst_type == "R":
                rd = self.registers[tokens[1]]
                rs1 = self.registers[tokens[2]]
                rs2 = self.registers[tokens[3]]
                bin = funct7 + rs2 + rs1 + funct3 + rd + opcode
                hex = f"{int(bin, 2):08x}"
                hex_lines.append(hex)
                
            elif inst_type == "I":
                rd = self.registers[tokens[1]]
                rs1 = self.registers[tokens[2]]
                imm_val = int(tokens[3])
                imm_bin = format(imm_val & 0xFFF, '012b')
                
                bin = str(imm_bin) + rs1 + funct3 + rd + opcode
                hex = f"{int(bin, 2):08x}"
                hex_lines.append(hex)
                
            elif inst_type == "S":    
                rs2 = self.registers[tokens[1]]
                
                clean_for_split = tokens[2].replace(")", "").replace("(", ",")
                parts = clean_for_split.split(",")
                
                rs1 = self.registers[parts[1]]
                simm = int(parts[0])
                simm_bin = format(simm & 0xFFF, '012b')
                
                bit_115 = simm_bin[0:7]
                bit_40  = simm_bin[7:12]
                
                bin = str(bit_115) + rs2 + rs1 + funct3 + str(bit_40) + opcode
                hex = f"{int(bin, 2):08x}"
                hex_lines.append(hex)
                
                pass
            elif inst_type == "SB":   
                rs1 = self.registers[tokens[1]] 
                rs2 = self.registers[tokens[2]]
                
                label_name = tokens[3]
                target_addr = int(self.symbol_table[label_name])
                
                sbimm = target_addr - PC
                sbimm_bin = format(sbimm & 0xFFF, '012b')
                
                bit_12     = sbimm_bin[0]    
                bit_11     = sbimm_bin[1]   
                bits_10_5  = sbimm_bin[2:8]  
                bits_4_1   = sbimm_bin[8:12] 
                
                bin = str(bit_12) + str(bits_10_5) + rs2 + rs1 + funct3 + str(bits_4_1) + str(bit_11) + opcode
                hex = f"{int(bin, 2):08x}"
                hex_lines.append(hex)
                
            elif inst_type == "U":   
                rd_u = self.registers[tokens[1]]
                uimm_val = int(tokens[2]) 
                uimm_bin = format(uimm_val & 0xFFF, '020b')
                
                bin = str(uimm_bin) + rd_u + opcode
                hex = f"{int(bin, 2):08x}"
                hex_lines.append(hex)
                
            elif inst_type == "UJ":    
                rd_u = self.registers[tokens[1]]
                ujimm_val = int(tokens[2]) 
                ujimm_bin = format(ujimm_val & 0xFFF, '021b')
                
                bit_20    = ujimm_bin[0]
                bits_101  = ujimm_bin[10:20]
                bit_11    = ujimm_bin[9]
                bits_1912 = ujimm_bin[1:9]
                
                ujimm_fin = str(bit_20 + bits_101 + bit_11 + bits_1912) 
                
                bin = ujimm_fin + rd_u + opcode
                hex = f"{int(bin, 2):08x}"
                hex_lines.append(hex)
                
            PC += 4
        return hex_lines
        pass
