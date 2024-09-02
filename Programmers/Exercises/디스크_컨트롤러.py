import heapq

def solution(jobs):
    jobs.sort()
    N = len(jobs)

    total = 0
    j_idx = 1
    cur_t = jobs[0][0]
    heap = [[-jobs[0][0] + jobs[0][1], jobs[0][1]]]    # 대기(-요청) + 소요시간, 소요시간 
    while heap:
        wt, ct = heapq.heappop(heap)
        total += (cur_t + wt)
        cur_t += ct
            
        while j_idx < N:
            job = jobs[j_idx]
            if job[0] > cur_t:
                break
            heapq.heappush(heap, [-job[0] + job[1], job[1]])
            j_idx += 1
        
    return total // N

answer = solution([[0, 3], [1, 9], [2, 6]])
print(answer)    # 9