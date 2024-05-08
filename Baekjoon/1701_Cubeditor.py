# KMP Alogrithm : https://yiyj1030.tistory.com/495

def make_table(pattern: str) -> list:
    table = [0] * len(pattern)
    s = 0
    for e in range(1, len(pattern)):
        # find the longest prefix that is also suffix
        while s > 0 and pattern[s] != pattern[e]:
            s = table[s - 1]
        # increase the length of the prefix
        if pattern[s] == pattern[e]:
            s += 1
            table[e] = s
    return table

def solution(string: str) -> int:
    mx = 0
    for i in range(len(string)):
        pattern = string[i:]
        mx = max(mx, max(make_table(pattern)))
    return mx

if __name__ == "__main__":
    pattern = input()

    answer = solution(pattern)
    print(answer) 


    #     max_len = 0
    # for i in range(len(string)):
    #     for j in range(i+1, len(string)+1):
    #         if string[i:j] in string[j:]:
    #             max_len = max(max_len, j-i)
    # return max_len