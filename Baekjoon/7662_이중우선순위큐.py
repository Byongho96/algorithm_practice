import sys
import heapq
from collections import defaultdict


if __name__ == '__main__':
    input = sys.stdin.readline

    for _ in range(int(input())):

        max_heap = []
        min_heap = []
        exist = defaultdict(int)    # 최대힙과 최소힙 동기화를 위한 기록용 dictionary
        
        for i in range(int(input())):
            mode, number = input().rstrip().split()
            number = int(number)
            
            if mode == 'I':
                heapq.heappush(max_heap, -number)
                heapq.heappush(min_heap, number)
                exist[number] += 1
                
            elif number > 0:
                while max_heap and not exist[-max_heap[0]]: # 최소힙과 동기화
                    heapq.heappop(max_heap)
                if max_heap:
                    exist[-heapq.heappop(max_heap)] -= 1

            else:
                while min_heap and not exist[min_heap[0]]:  # 최대힙과 동기화
                    heapq.heappop(min_heap)
                if min_heap:
                    exist[heapq.heappop(min_heap)] -= 1
    
        while max_heap and not exist[-max_heap[0]]: # 마지막 동기화
            heapq.heappop(max_heap)
        while min_heap and not exist[min_heap[0]]:  # 마지막 동기화
            heapq.heappop(min_heap)

        if min_heap and max_heap:
            print(-max_heap[0], min_heap[0])
        else:
            print('EMPTY')




# import sys
# from collections import defaultdict
# input = sys.stdin.readline

# # 우선순위 큐 구현을 위해 참고한 블로그 글: https://daimhada.tistory.com/108

# class MaxHeap:

#     # 생성자 함수
#     def __init__(self):
#         self.queue = []

#     # 삽입 함수
#     def insert(self, n):
#         self.queue.append(n)
#         current_index = len(self.queue) - 1
#         while 0 < current_index:
#             parent_index = self.parent(current_index)
#             if self.queue[parent_index] < self.queue[current_index]:
#                 self.swap(parent_index, current_index)
#                 current_index = parent_index
#             else:
#                 break

#     # 삭제 함수
#     def delete(self):
#         last_index = len(self.queue) - 1
#         if last_index < 0:
#             return -1
#         self.swap(0, last_index)
#         max_value = self.queue.pop()
#         self.maxHeapify(0)
#         return max_value
    

#     # heapify 정렬 함수
#     def maxHeapify(self, i):
#         left_index  = self.left_child(i)
#         right_index = self.right_child(i)
#         last_index = len(self.queue) - 1

#         max_index = i
#         if left_index <= last_index and self.queue[max_index] < self.queue[left_index]:
#             max_index = left_index
#         if right_index <= last_index and self.queue[max_index] < self.queue[right_index]:
#             max_index = right_index

#         if max_index != i:
#             self.swap(i, max_index)
#             self.maxHeapify(max_index)

#     # 그 외 함수
#     def swap(self, i, j):
#         self.queue[i], self.queue[j] = self.queue[j], self.queue[i]
    
#     def parent(self, i):
#         return (i - 1) // 2
    
#     def left_child(self, i):
#         return 2 * i + 1
    
#     def right_child(self, i):
#         return 2 * i + 2

#     # special methods
#     def __str__(self):
#         return str(self.queue)
    
#     def __getitem__(self, index):
#         return self.queue[index]
    
#     def __iter__(self):
#         self.index = 0
#         return self
    
#     def __next__(self):
#         if len(self.queue) <= self.index:
#             raise StopIteration
        
#         self.index += 1
#         return self.queue[self.index - 1]
    
#     def __contains__(self, item):
#         return item in self.queue
    
#     def __bool__(self):
#         return bool(self.queue)

# if __name__ == '__main__':

#     T = int(input())    # 테스트 횟수
#     for _ in range(T):

#         max_heap, max_trash = MaxHeap(), defaultdict(int)
#         min_heap, min_trash = MaxHeap(), defaultdict(int)

#         N = int(input())    # 연산 갯수
#         for _ in range(N):
#             mode, number = input().rstrip().split()
#             number = int(number)

#             if mode == 'I':
#                 max_heap.insert(number)
#                 min_heap.insert(-number)
            
#             elif number > 0:
#                 while max_heap and max_trash[max_heap[0]]:
#                     max_trash[max_heap[0]] -= 1
#                     max_heap.delete()
#                 if max_heap:
#                     min_trash[max_heap[0]] += 1
#                     max_heap.delete()

#             else:
#                 while min_heap and min_trash[-min_heap[0]]:
#                     min_trash[-min_heap[0]] -= 1
#                     min_heap.delete()
#                 if min_heap:
#                     max_trash[-min_heap[0]] += 1
#                     min_heap.delete()

#         while max_heap and max_trash[max_heap[0]]:
#             max_trash[max_heap[0]] -= 1
#             max_heap.delete()
#         while min_heap and min_trash[-min_heap[0]]:
#             min_trash[-min_heap[0]] -= 1
#             min_heap.delete()

#         if max_heap and min_heap:
#             print(max_heap[0], -min_heap[0])
#         else:
#             print('EMPTY')