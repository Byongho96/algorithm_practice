from collections import defaultdict

class Solution:
    def backtracking(self, W, w, words, letters, score):
        # update the answer
        self.answer = max(self.answer, score)

        # end condition
        if w > W - 1:
            return

        # traverse candidates
        for i in range(w, W):
            word = words[i]

            # if the word is already used
            if word['used']:
                continue

            # check the remaining letters can make the word
            letters_copy = letters.copy()
            for ltr, cnt in word['letters'].items():
                if cnt > letters_copy[ltr]:
                    break
                letters_copy[ltr] -= cnt

            else:
                word['used'] = True
                score += word['score']
                self.backtracking(W, i + 1, words, letters_copy, score)
                word['used'] = False
                score -= word['score']
            
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # transform words info into dictonary
        W = len(words)
        words_lst = [{} for _ in range(W)]
        for i in range(W):
            word = words[i]
            word_dict = {
                'used': False,
                'letters' : defaultdict(int),
                'score': 0,
            }
            for c in word:
                word_dict['letters'][c] += 1
                word_dict['score'] += score[ord(c) - ord('a')]
            words_lst[i] = word_dict

        # transform lettes info into dictonary
        letters_dict = defaultdict(int)
        for letter in letters:
            letters_dict[letter] += 1

        # backtracking
        self.answer = 0
        self.backtracking(W, 0, words_lst, letters_dict, 0)

        return self.answer