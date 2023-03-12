brks = input()
ref = {')': ('(', 2), ']': ('[', 3)}
stk = []

try:
    for b in brks:
        if b == '(' or b == '[':
            stk.append(b)
        else:
            b1 = stk.pop()
            if b1 == ref[b][0]:
                stk.append(ref[b][1])
            elif isinstance(b1, int):
                b2 = stk.pop()
                while isinstance(b2, int):
                    b1 += b2
                    b2 = stk.pop()
                if b2 == ref[b][0]:
                    stk.append(b1 * ref[b][1])
                else:
                    print(0)
                    break
            else:
                print(0)
                break
    else:
            print(sum(stk))
except:
    print(0)