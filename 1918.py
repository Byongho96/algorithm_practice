# 괄호 넣기
fml = list(input())
fml_brk = []
ref = {'(': 0, ')': 0, '*': 1, '/': 1, '+': 2, '-': 2}

i = 0
while fml[i] != fml[-1]:
    if ref.get(fml[i]) == 2:
        if fml[i-1].isalpha:
            fml.insert(i - 2, '(')
            for j in range(i-1, len(fml)):
                if ref.get(fml[j])==2 or ref.get(fml[j])==1:
                    fml.insert(j - 1, ')')
print(fml)

