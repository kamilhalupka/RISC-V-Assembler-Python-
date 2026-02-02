# Setup initial values
addi x10, x0, 1024    # Base memory address
addi x11, x0, 5       # Loop counter (limit)
addi x12, x0, 0       # Current index
addi x5, x0, 1        # Value to increment

LOOP:
# Store value and increment index
sw x5, 0(x10)         # Store current value to memory
add x12, x12, x5      # Increment index counter
addi x10, x10, 4      # Move memory pointer forward

# Branching logic
blt x12, x11, LOOP    # If index < limit, jump back to LOOP

# Procedure call and return
jal x1, RESET_VAL     # Jump to reset logic, save return address in x1
sub x10, x10, x12     # Final arithmetic check

RESET_VAL:
addi x5, x0, 0        # Reset value register
jalr x0, 0(x1)        # Return to caller (This is an I-type jump!)