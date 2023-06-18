# 참고한 블로그: https://velog.io/@yejinh/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-LeetCode-Container-With-Most-Water-k7k3rxu6ip
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        length = len(height)
		
        # 투 포인터
        left = 0    # 왼쪽 포인터
        right = length - 1  # 오른쪽 포인터

        for _ in range(length - 1): # 반복 횟수를 알고 있다면, for문이 while문보다 근소하게 우수
            if height[left] < height[right]:
                max_area = max(max_area, (right - left) * height[left])
                left += 1
            else:
                max_area = max(max_area, (right - left) * height[right])
                right -= 1

        return max_area