import sys
input = sys.stdin.readline

def solution(N, M, weights, marbles):
    availables = {0,}

    # {N 개의 추로 확인 가능한 무게} = {(N-1) 개의 추로 확인 가능한 무게} + {(N-1)개 + N번째 추로 확인 가능한 무게} + {(N-1)개 - N번째 추로 확인 가능한 무게}
    for w in weights:
        for a in availables.copy():
            availables.add(a+ w)
            availables.add(abs(a- w))

    return list(map(lambda m: 'Y' if m in availables else 'N', marbles))


if __name__ == "__main__":
    # weights information
    N = int(input())
    weights = list(map(int, input().split()))

    # marbles information
    M = int(input())
    marbles = list(map(int, input().split()))

    # answer
    answer = solution(N, M, weights, marbles)
    print(*answer)


# def solution(W, M, weights, marbles):

#     # 메인 아이디어
#     # {N 개의 추로 확인 가능한 무게} = {(N-1) 개의 추로 확인 가능한 무게} + {(N-1)개 + N번째 추로 확인 가능한 무게} + {(N-1)개 - N번째 추로 확인 가능한 무게}

#     available = {0}
    
#     for w in range(W):
#         previous_available = available.copy() # (N-1) 개의 추로 확인 가능한 무게
#         cur_weight = weights[w] # N번째 추

#         for weight in previous_available:
#             available.add(weight + cur_weight) # (N-1)개 + N번째 추로 확인 가능한 무게
#             available.add(abs(weight - cur_weight)) # (N-1)개 - N번째 추로 확인 가능한 무게

#     # 답안 작성
#     answer = []
#     for marble in marbles:
#         if marble in available:
#             answer.append('Y')
#         else:
#             answer.append('N')

#     return answer


# if __name__ == "__main__":
#     # 추 데이터 입력 받기
#     W = int(input())
#     weights = list(map(int, input().split()))
    
#     # 무게 데이터 입력 받기
#     M = int(input())
#     marbles = list(map(int, input().split()))

#     # 리스트 형태로 답안 반환
#     answer = solution(W, M, weights, marbles)
#     print(*answer)