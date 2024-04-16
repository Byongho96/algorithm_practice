class Solution:
    def compress(self, chars: List[str]) -> int:
        N = len(chars)
        cnt = 1
        for idx in range(N - 1, -1, -1):
            if idx and chars[idx - 1] == chars[idx]:
                cnt += 1
                chars.pop(idx)
            elif cnt > 1:
                for num in str(cnt)[::-1]:
                    chars.insert(idx + 1, num)
                cnt = 1

        return len(chars)