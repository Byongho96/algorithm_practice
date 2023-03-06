from collections import defaultdict

def solution(query_lst, folder_lst, file_lst):
    for query in query_lst:
        files = []
        files.extend(file_lst[query])
        folders = folder_lst[query]
        for folder in folders:
            files.extend(file_lst[folder])
        
        print(len(set(files)), end=' ')
        print(len(files))

if __name__ == "__main__":
    N, M = map(int, input().split())
    folder_lst = defaultdict(list)
    file_lst = defaultdict(list)

    for _ in range(N + M):
        parent, current, isFolder = input().split()
        if int(isFolder):
            folder_lst[parent].append(current)
        else:
            file_lst[parent].append(current)

    Q = int(input())
    query_lst = []
    for _ in range(Q):
        folder = input().split('/')[-1]
        query_lst.append(folder)

    solution(query_lst, folder_lst, file_lst)