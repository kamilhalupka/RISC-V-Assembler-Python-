addi x1, x0, 0
addi x2, x0, 5
LOOP:
beq x1, x2, END
addi x1, x1, 1
jal x0, LOOP
END:
add x1, x0, x0