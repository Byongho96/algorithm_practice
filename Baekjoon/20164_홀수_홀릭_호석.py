ODDS = ('1', '3', '5', '7', '9')

def count_odds(string):
    num = 0
    for c in string:
        if c in  ODDS:
            num += 1
    return num

def divide(string, num_odds):
    global min_num
    global max_num

    cur_odd = count_odds(string)
    total_odds = cur_odd + num_odds

    if len(string) == 1:
        min_num = min(total_odds, min_num)
        max_num = max(total_odds, max_num)
        return

    if len(string) == 2:
        divide(str(int(string[0]) + int(string[1])), total_odds)
        return

    S = len(string)
    for i in range(1, S - 1):
        for j in range(i + 1, S):
            divide(str(int(string[:i]) + int(string[i:j]) + int(string[j:])), total_odds)

if __name__ == '__main__':
    number = input()

    min_num = float("inf") 
    max_num = 0
    divide(number, 0)

    print(min_num, max_num)