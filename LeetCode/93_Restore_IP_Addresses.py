from typing import List

class Solution:
    def __init__(self):
        self.answer = []

    def backtracking(self, N, n:int, step:int, ip: str):
        # 종료조건
        if step == 3:
            if n == N:
                self.answer.append(ip)
            return

        # 가지치기
        if (N - n) < 3- step: # 남은 ip주소부분이 적은 경우
            return

        if (N - n) > (3 -step) * 3: # 남은 ip주소부분이 많은 경우
            return

        # 후보군 출력
        for i in range(1, 4):
            if n + i <= N  and ((self.s[n] != '0' and 0 < int(self.s[n:n + i]) < 256) or self.s[n:n + i] == '0'):
                self.backtracking(N, n + i, step + 1, ip + '.' + self.s[n:n + i])

    def restoreIpAddresses(self, s: str) -> List[str]:
        N = len(s)
        if N < 4 or N > 12: # 불가능한 값 제거
            return  []
        
        self.answer = [] # 초기화
        self.s = s  # 메모리 절약을 위해 인스턴스 변수 할당

        # 백트래킹
        for i in range(1, 4):
            if (s[0] != '0' and 0 < int(s[:i]) < 256) or s[:i] == '0':
                self.backtracking(N, i, 0, s[:i])
                
        return self.answer