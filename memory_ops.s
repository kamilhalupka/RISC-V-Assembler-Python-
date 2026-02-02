addi x10, x0, 1024
addi x5, x0, 255
sw x5, 0(x10)
sw x5, 4(x10)
lw x6, 0(x10)
lw x7, 4(x10)