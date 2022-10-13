def is_acceptable(password):
    # condition1: 모음(a, e, i, o, u) 하나를 반드시 포함하여야 한다.
    # condition2: 모음이 3 개 혹은 자음이 3 개 연속으로 오면 안 된다.
    # condition3: 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
    vowels = ('a', 'e', 'i', 'o', 'u',)
    L = len(password)
    condition1 = False                                          # condition1 초깃값
    ppre_vowel = False if password[0] in vowels else True       # condition2 초깃값, password의 첫번째의 모음 판정결과와 반대로 설정
    pre_vowel = ppre_vowel
    pre_c = '0'                                                 # condition3 초깃값, 'a~z'외의 임의의 문자열로 설정
    for c in password:
        c_vowel = True if c in vowels else False

        # [condition 1] 체크하고 마지막에 다시 확인
        if c_vowel:                                             # 모음이 나오면
            condition1 = True

        # [condition 2]
        if ppre_vowel == pre_vowel and pre_vowel == c_vowel:    # 모음 자음이 3번 연속 나오면
            return False
        ppre_vowel = pre_vowel                                  # 다음 반복문을 위해 업데이트
        pre_vowel = c_vowel

        # [condition 3]
        if pre_c == c and c not in ('e', 'o'):                  # 같은 글자가 연속 두번 오면
            return False
        pre_c = c                                               # 다음 반복문을 위해 업데이트

    if condition1:                                              # condition 2 & 3을 모두 통과하면, condition 1을 확인
        return True
    else:
        return False

while True:
    password = input()
    if password == 'end':
        break
    if is_acceptable(password):
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')
