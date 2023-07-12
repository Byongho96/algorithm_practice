class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_set = {'a', 'e', 'i', 'o', 'u'} # in 연산은 집합의 배열보다 빠름

        # 첫 구간 모음 수 계산
        vowels = 0 
        for idx in range(k):
            if s[idx] in vowel_set:
                vowels += 1
        mx_vowels = vowels

        # 슬라이딩 윈도우의 크기가 일정하므로, 하나의 인덱스로 계산
        for idx in range(k, len(s)):
            if s[idx] in vowel_set:
                vowels += 1
            if s[idx - k] in vowel_set:
                vowels -= 1

            mx_vowels = mx_vowels if mx_vowels > vowels else vowels # max 내장함수보다 if문이 조금 더 빠름

        return mx_vowels