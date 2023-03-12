import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

class Heap:
    def __init__(self):
        self.heap = [0] * 1001
        self.last = 0
    def insert(self, micro):         # micro = [num, i, j, d]
        self.last += 1
        self.heap[self.last] = micro
        cur = self.last
        while cur != 1:
            par = self.par(cur)
            if self.heap[par][0] < self.heap[cur][0]:
                self.swap(par, cur)
                cur = par
            else:
                break
    def delete(self):
        if self.last:
            self.swap(1, self.last)
            max_value = self.heap[self.last]
            self.last -= 1
            self.maxHeapify(1)
            return max_value
        return [0, 0, 0, 0]     # pop할게 없을 때는, num=0인 형태를 반환
    def maxHeapify(self, cur):
        left = self.left(cur)
        right = self.right(cur)
        mx_idx = cur
        if left <= self.last and self.heap[mx_idx][0] < self.heap[left][0]:
            mx_idx = left
        if right <= self.last and self.heap[mx_idx][0] < self.heap[right][0]:
            mx_idx = right
        if mx_idx != cur:
            self.swap(cur, mx_idx)
            self.maxHeapify(mx_idx)
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    def __str__(self):
        string = ''
        for i in range(1001):
            string += str(self.heap[i])
        return string

    @staticmethod
    def par(i):
        return i // 2
    @staticmethod
    def left(i):
        return 2 * i
    @staticmethod
    def right(i):
        return 2 * i + 1

dir = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
opposite = {1: 2, 2: 1, 3: 4, 4: 3}

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    micro = Heap()                      # heapd로 micro형성. 가장 양이 많은 미생물 순으로 뽑아내기 위해서
    for _ in range(K):
        i, j, num, d = map(int, input().split())
        micro.insert([num, i, j, d])    # [미생물 수, 행, 렬, 방향] 리스트로 heappush

    for _ in range(M):
        tmp = {}                        # 미생물들을 움직인 후, 바로 insert하지 말고 합치기 처리를 위해서 임시 저장 딕셔너리
        for idx in range(K):            # 최대 K번 반복
            num, i, j, d = micro.delete()
            if num:                     # 제대로 미생물이 pop된 경우
                di, dj = dir[d]             # 딕셔너리로 방향 정보 읽어옴
                i += di                     # 방향 업데이트
                j += dj
                if i == 0 or i == N-1 or j == 0 or j == N-1:    # 약품 처리 구간에 있는 경우
                    num //= 2
                    d = opposite[d]
                if num:                                         # 미생물이 아직 죽지 않은 경우
                    if not tmp.get((i, j)):                         # 미생물의 위치(i, j)를 key로 딕셔너리 업데이트
                        tmp[(i, j)] = (num, d)
                    else:                                           # 이미 해당 위치에 미생물이 존재하는 경우
                        num_pre, d = tmp[(i, j)]
                        num_pre += num                                  # 미생물의 갯수를 합침
                        tmp[(i, j)] = (num_pre, d)                      # 방향은 그대로 유지. becuase 힙 구조로 미생물이 큰 순으로 뽑았기 때문
            else:                       # 모든 미생물이 이미 pop된 경우, 반복문 탈출
                break
        for i, j in tmp:                                        # 임시 tmp에 있는 미생물들 heappush
            num, d = tmp[(i, j)]
            micro.insert([num, i, j, d])

    result = 0
    while True:                     # 미생물 더하기
        num, *res = micro.delete()
        if num:
            result += num
        else:                           # 모두 pop된 경우
            break

    print(f'#{tc} {result}')