di = (0, 1, 0, -1)
dj = (1, 0, -1, 0)

def dfs(si, sj):
    global mx_distance

    distance_per_bit = [[{} for _ in range(M + 2)] for _ in range(N + 2)]   # {}를 값으로 가지는 바둑판 배열
    stack = [(si, sj, 1, 0 | 1 << alphabet_to_num[arr[1][1]])] # 행, 렬, 거리, 방문한 알파벳 비트열

    while stack:
        i, j, distance, visited  = stack.pop()
        for idx in range(4):
            ni = i + di[idx]
            nj = j + dj[idx]
            if arr[ni][nj] and not ((visited >> alphabet_to_num[arr[ni][nj]]) & 1): # 방문하지 않은 배열일 경우
                new_visited = visited | (1 << alphabet_to_num[arr[ni][nj]]) # 새 방문한 알파벳 비트열 생성
                new_distance = distance + 1 
                prev_max_distance = distance_per_bit[ni][nj].get(new_visited, 0)
                if prev_max_distance < new_distance:
                    distance_per_bit[ni][nj][new_visited] = new_distance
                    stack.append((ni, nj, new_distance, new_visited))
                    mx_distance = max(mx_distance, new_distance)

if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = [[0] * (M + 2)] + [[0] + list(input()) + [0] for _ in range(N) ] + [[0] * (M + 2)] 

    # {'A': 0, 'B': 2, 'C':3, ...}
    alphabet_to_num  = {}
    for i in range(ord('A'), ord('Z') + 1):
        alphabet_to_num[chr(i)] = i - ord('A')

    mx_distance = 1
    dfs(1, 1)
    print(mx_distance)
        