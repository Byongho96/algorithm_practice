n_a = ord('a')
n_z = ord('z')
n_A = ord('A')
n_Z = ord('Z')

result = ''

for c in input():
    n_c = ord(c)
    if n_a <= n_c <= n_z:
        n_c += 13
        if n_c > n_z:
            n_c = n_c - n_z + n_a - 1
    elif n_A <= n_c <= n_Z:
        n_c += 13
        if n_c > n_Z:
            n_c = n_c - n_Z + n_A - 1
    result += (chr(n_c))

print(result)