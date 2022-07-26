import sys

N, M = map(int, sys.stdin.readline().split()) # N, M 입력받기

cards = list(map(int, sys.stdin.readline().split()))    # 펼쳐진 카드들 입력 받기

cards.sort() # 카드를 오름차순으로 정렬
sum_list = [] # 합을 저장할 리스트 형성
result = 0

# print(cards)
flag = False    # 다중 반복문 빠져나가기 위한 flag 변수 지정
for i in range(len(cards)-2):
    for j in range(i+1, len(cards)-1):
        for k in range(j+1, len(cards)):
            sum_cards = cards[i] + cards[j] + cards[k]
            # print(sum_cards, i, j, k)
            if (result < sum_cards) and (sum_cards < M): # sum이 M보다 작고, reuslt보다 큰 경우 업데이트
                result = sum_cards
            elif sum_cards > M:   # sum이 M보다 큰 경우에는 다음 반복문으로 탈출
                break
            elif sum_cards == M:
                result = M
                flag = True # M과 같은  sum이 나오면 더이상 계산할 필요 없음
                break
        if flag:
            break
    if flag:
        break

print(result)