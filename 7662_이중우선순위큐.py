# 우선순위 큐 구현을 위해 참고한 블로그 글: https://daimhada.tistory.com/108

class MaxHeap:

    # 생성자 함수
    def __init__(self):
        self.queue = []

    # 삽입 함수
    def insert(self, n):
        self.queue.append(n)
        current_index = len(self.queue) - 1
        while 0 < current_index:
            parent_index = self.parent(current_index)
            if self.queue[parent_index] < self.queue[current_index]:
                self.swap(parent_index, current_index)
                current_index = parent_index
            else:
                break

    # 삭제 함수
    def delete(self):
        last_index = len(self.queue) - 1
        if last_index < 0:
            return -1
        self.swap(0, last_index)
        max_value = self.queue.pop()
        self.maxHeapify(0)
        return max_value
    

    # heapify 정렬 함수
    def maxHeapify(self, i):
        left_index  = self.left_child(i)
        right_index = self.right_child(i)
        last_index = len(self.queue) - 1

        max_index = i
        if left_index <= last_index and self.queue[max_index] < self.queue[left_index]:
            max_index = left_index
        if right_index <= last_index and self.queue[max_index] < self.queue[right_index]:
            max_index = right_index

        if max_index != i:
            self.swap(i, max_index)
            self.maxHeapify(max_index)

    def swap(self, i, j):
        self.queue[i], self.queue[j] = self.queue[j], self.queue[i]
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2

    def __str__(self):
        return str(self.queue)
    
    def __iter__(self):
        
    


if __name__ == '__main__':

    T = int(input())    # 테스트 횟수
    for _ in range(T):
        max_heap = MaxHeap()
        print(max_heap)
        N = int(input())    # 연산 갯수
        for _ in range(N):
            operation = input().split()
            mode, number = operation[0], int(operation[1])

            if mode == 'I':
                max_heap.insert(number)
                continue
            
            if number > 0:
                max_heap.delete()
                continue
            
            
        mx = -(2**32 + 1)
        mn = (2**32 + 1)

        
        if mx == -(2**32 + 1):
            print('EMPTY')
        else:
            print(mx, mn)


