import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

min = max = numbers[0]

for n in numbers:
    if n > max:
        max = n
    elif n < min:
        min = n

print(min, max)