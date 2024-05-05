def solution(H, W, blocks):
    # create the height map
    height_map = [[0] * W for _ in range(H)]
    for i, block in enumerate(blocks):
        for j in range(block):
            height_map[j][i] = 1

    # calculate the water
    water = 0
    for i in range(H):
        # find the left wall
        left_wall = -1
        for j in range(W):
            if height_map[i][j] == 1:
                left_wall = j
                break

        # find the right wall
        right_wall = -1
        for j in range(W - 1, -1, -1):
            if height_map[i][j] == 1:
                right_wall = j
                break

        # calculate the water
        for j in range(left_wall + 1, right_wall):
            if height_map[i][j] == 0:
                water += 1

    return water

if __name__ == "__main__":
    H, W = map(int, input().split())
    blocks = list(map(int, input().split()))

    answer = solution(H, W, blocks)
    print(answer)