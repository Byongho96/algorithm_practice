class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        answer = []
        
        for asteroid in asteroids:
            # asteroid moving right
            if asteroid > 0:
                answer.append(asteroid)
                continue

            # asteroid moving left
            while answer and answer[-1] > 0:
                if -asteroid > answer[-1]:
                    answer.pop()
                    continue
                if -asteroid == answer[-1]:
                    answer.pop()
                break
            else:
                answer.append(asteroid)

        return answer


