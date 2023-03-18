if __name__ == "__main__":
    DISK, NUM, TURN = map(int, input().split())

    # 원판에 적힌 수는 1 이상 
    nums = []
    for _ in range(DISK):
        nums.append(list(map(int, input().split())))

    total_nums = DISK * NUM
    for _ in range(TURN):
        disk, is_counter_clock, step = map(int, input().split())

        cur_disk = disk # 주의 1. 원판 배수
        # 원판 돌리기
        while True:
            if cur_disk > DISK:
                break
            original_nums = nums[cur_disk - 1]
            if is_counter_clock:    # 반시계 방향 -> 왼쪽
                new_nums = original_nums[step:] + original_nums[:step]
            else:                   # 시계 방향 -> 오른쪽
                new_nums = original_nums[NUM-step:] + original_nums[:NUM-step]
            nums[cur_disk - 1] = new_nums
            cur_disk += disk

        # 주의 2. 같은 인접 숫자 모두 찾기(모든 케이스 고려)
        delete_nums = set()

        visited = [[0] * NUM for _ in range(DISK)]
        for i in range(DISK):
            for j in range(NUM):
                if visited[i][j] and not nums[ni][nj]:
                    continue

                # dfs
                stack = [(i, j)]
                visited[i][j] = 1
                while stack:
                    ci, cj = stack.pop()
                    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                        ni = ci + di
                        nj = (cj + dj) % NUM
                        if  0 <= ni < DISK and not visited[ni][nj] and nums[ni][nj]:
                            if nums[ci][cj] == nums[ni][nj]:
                                visited[ni][nj] = 1
                                stack.append((ni, nj))
                                delete_nums.add((ci, cj))
                                delete_nums.add((ni, nj))

        if delete_nums: # 인접 숫자 있을 경우, 모두 삭제
            total_nums -= len(delete_nums)
            for i, j in delete_nums:
                nums[i][j] = 0
        else:           # 인접 숫자 없을 경우, 업데이트
            sm = 0
            for disk in range(DISK):
                sm += sum(nums[disk])
            avg = sm / total_nums
            for disk in range(DISK):
                for idx in range(NUM):
                    if not nums[disk][idx]:
                        continue
                    if nums[disk][idx] > avg:
                        nums[disk][idx] -= 1
                        continue
                    if nums[disk][idx] < avg:
                        nums[disk][idx] += 1

        if not total_nums:  # 주의 3.모든 숫자를 지웠다면 반복문 탈출
            break
    
    sm = 0
    for disk in range(DISK):
        sm += sum(nums[disk])
    print(sm)

