def magic_sequence(n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2] + i)
    return seq

print(magic_sequence(10))