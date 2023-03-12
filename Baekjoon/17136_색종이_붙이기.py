from pprint import pprint
from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

def backtracking(n, papers, used):
    global mn
    # 종료조건.
    if n == 100:        # (9, 9)까지 탐색 완료하면
        mn = min(mn, used)  # 최솟값 어데이트
        return
    # 가지치기
    if used >= mn:      # 최솟값 찾는 중
        return
    # 후보군 출력
    i, j = divmod(n, 10)    # n번째 위치의 행,열 값 추출
    if arr[i][j]:           # 해당 자리가 1이면
        for idx in range(1, 6): # 5가지 종이 모두 넣어보며 가능한 후보군에서 재귀출력
            if papers[idx]:     # idx번째 종이가 있으면,

                # i,j를 왼쪽 위 지점으로 해서 idx 크기만큼 정사각형을 보았을 때 0이 하나라도 있는지 검사
                for row in range(idx):                              # 이중 for문 말고 행 단위로 읽어와서, 밑밑줄 in 구문으로 검사
                    if 0 <= i + idx - 1 < 10 and 0 <= j + idx - 1 < 10: # 밑줄에서 인덱스 에러가 나는 경우를 미리 제외
                        if 0 in arr[i+row][j:j+idx]:                        # 0이 하나라도 있으면, break
                            break
                    else:                                               # 정사각형 종이가 경계값을 벗어나도, break
                        break
                else:                                               # 모두 1인 경우, idx 사이즈의 색종이가 들어갈 수 있는 경우
                    for row in range(idx):                              # 색종이 붙이기(0으로 변경)
                        arr[i + row][j:j + idx] = [0] * idx
                    papers[idx] -= 1                                    # 붙인 색종이 갯수 감소
                    backtracking(n+1, papers, used+1)                   # 재귀호출
                    for row in range(idx):                              # 색종이 떼기(1으로 변경). 다음 for문(색종이 사이즈)의 재귀호출을 위해서
                        arr[i + row][j:j + idx] = [1] * idx
                    papers[idx] += 1                                    # 붙인 색종이 갯수 다시 복귀. 다음 for문(색종이 사이즈)의 재귀호출을 위해서
    else:                   # 해당 자리가 0이면, 바로 다음 자리로 넘어감
        backtracking(n + 1, papers[:], used)


arr = [list(map(int, input().split())) for _ in range(10)]      # 배열
papers = [0, 5, 5, 5, 5, 5]                                     # 남은 종이 수

mn = 26
backtracking(0, papers, 0)

if mn == 26:
    print(-1)
else:
    print(mn)


#################################################################################################
# def bfs(i, j):
#     q = deque()
#     visited[i][j] = 1
#     nodes = [(i, j)]    # 방문한 노드를 모두 저장하여, 노드리스트 형성
#     q.append((i, j))
#     while q:
#         i, j = q.popleft()
#         for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
#             ni = i + di
#             nj = j + dj
#             if 0 <= ni < 10 and 0 <= nj < 10 and not visited[ni][nj] and arr[ni][nj]:
#                 visited[ni][nj] = 1
#                 # visited[ni][nj] = visited[i][j] + 1
#                 nodes.append((ni, nj))
#                 q.append((ni, nj))
#     areas.append(nodes)  # 외부함수 변수 area에 노드리스트 추가
#
# def make_combinations(n, papers, combination):
#     # 종료조건
#     if n == A:
#         combinations.append(combination)
#         return
#     # 후보군 출력
#     N = len(areas[n])
#     for i in range(papers[1] + 1):
#         tmp = [0] * 6
#         M = N - 1 * i
#         if M < 0:
#             break
#         tmp[1] = i
#         for j in range(papers[2] + 1):
#             O = M - 4 * j
#             if O < 0:
#                 break
#             tmp[2] = j
#             for k in range(papers[3] + 1):
#                 P = O - 9 * k
#                 if P < 0:
#                     break
#                 tmp[3] = k
#                 for l in range(papers[4] + 1):
#                     Q= P - 16 * l
#                     if Q < 0:
#                         break
#                     tmp[4] = l
#                     for m in range(papers[5] + 1):
#                         R = Q - 25 * m
#                         if R == 0:
#                             # print(n, N, i, j, k, l, m)
#                             # print(tmp)
#                             papers_copy = papers[:]
#                             papers_copy[1] -= i
#                             papers_copy[2] -= j
#                             papers_copy[3] -= k
#                             papers_copy[4] -= l
#                             papers_copy[5] -= m
#                             combination_copy = deepcopy(combination)
#                             combination_copy.append(tmp)
#                             # print(combination_copy)
#                             make_combinations(n + 1, papers_copy, combination_copy)
#
# def pasting(n):
#     global result
#     if n == A:
#         sm = 0
#         for comb in combinations:
#             sm += sum(comb)
#         result = sm
#     for size in range(1, 6):
#         if combination[n][size]:
#             for _ in range(combination[n][size]):
#                 for node in areas[n]:
#                     i = node[0]
#                     j = node[1]
#                     flag = 0
#                     for di in range(size):
#                         for dj in range(size):
#                             if not arr[i+di][j+dj]:
#                                 flag = 1
#                                 break
#                         if flag:
#                             break
#                     else:
#                         for di in range(size):
#                             for dj in range(size):
#                                 arr[i + di][j + dj] = 0
#
#
#
# # 함수시작
# if __name__=='__main__':
#     arr = [list(map(int, input().split())) for _ in range(10)]
#     papers = [0, 5, 5, 5, 5, 5]
#
#     # 특이케이스
#     #   입력이 없을 경우
#     #   조합이 없을 경우
#
#     # [1]. 구역 만들기. areas = [[1구역 노드 리스트], [2구역 노드 리스트], [3구역 노드리스트], ...]
#     # [1]-1. arr를 탐색하면서 not visited인 지점 중 1인 곳을 잡는다
#     # [1]-2. bfs로 visited를 업데이트 하면서 1의 갯수를 센다. 구역별 노드 리스트를 형성
#     num_area = 0
#     areas = []
#     visited = [[0] * 10 for _ in range(10)]
#     for i in range(10):
#         for j in range(10):
#             if not visited[i][j] and arr[i][j]:
#                 bfs(i, j)
#                 num_area += 1
#     if not num_area:
#         print(0)
#         exit()
#     # pprint(areas)
#
#     # [2]. 구역 별 조합 만들기
#     # [2]-1. 구역별 크기와 남은 색종이수를 고려하여 조합 형성
#     combinations = []
#     A = len(areas)
#     combination = []
#     make_combinations(0, papers, combination)
#     if len(combinations) == 1:
#         print(-1)
#         exit()
#     # print(combinations)
#
#     # [2]-2. 조합의 총 길이(총 색종이 수)가 작은 순으로 정렬
#     def total_paper(comb):
#         paper = 0
#         for arr in comb:
#             paper += sum(arr)
#         return paper
#
#     combinations.sort(key=total_paper)
#     print(combinations)
#
#     # [2]-3. 백트래킹으로 구역의 모든 지점을 돌면서 큰 색종이부터 부착
#     result = -1
#     for combination in combinations:
#         pasting(0)
#         if result != -1:
#             break
#
#     print(result)