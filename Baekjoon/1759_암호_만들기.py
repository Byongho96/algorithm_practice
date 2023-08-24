VOWELS = ('a', 'e', 'i', 'o', 'u')

def backtracking(n, idx, selected, used, vowels, consonants):
    # pruning
    if C - idx < (L - n) or C - idx < 2 - consonants:
        return 
        
    # end condition
    if n == L:
        if consonants > 1 and vowels > 0:
            print(''.join(selected))
        return
    
    # canidate cases
    for i in range(idx, C):
        if used[i]:
            continue
        # print(n, i)
        used[i] = True
        selected[n] = alphabets[i]
        is_vowel = alphabets[i] in VOWELS
        backtracking(n + 1, i + 1, selected, used, vowels + 1 if is_vowel else vowels, consonants if is_vowel else consonants + 1)
        used[i] = False

if __name__ =='__main__':
    L, C = map(int, input().split())
    alphabets = list(input().split())

    # sort the alphabets
    alphabets.sort()

    # run backtracking
    used = [False] * C
    selected = [0] * L
    backtracking(0, 0, selected, used, 0, 0)