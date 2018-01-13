def set_bit(val, i, bit):
    num = 1 << i

    if bit:
        return val | num

    return val & ~num

NQ = input()

two_ints = NQ.split()

# N and Q
N, Q = int(two_ints[0]), int(two_ints[1])

# A bit string
A = int(input(), 2)

# B bit string
B = int(input(), 2)

# Q lines
output = []
for i in range(Q):
    input_line = input()
    split_input = input_line.split()

    query = split_input[0]
    index = int(split_input[1])

    if query == 'set_a':
        val = int(split_input[2])
        A = set_bit(A, index, val)

    elif query == 'set_b':
        val = int(split_input[2])
        B = set_bit(B, index, val)

    elif query == 'get_c':
        C = A + B
        C_bit = int(bool(C & (1<<index)))
        output.append(str(C_bit))

print(''.join(output))


