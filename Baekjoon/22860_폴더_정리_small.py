from collections import defaultdict

folder_to_files = defaultdict(list) # 특정 폴더의 모든 하위 파일들을 memoization
sub_folders = defaultdict(list)     # 특정 폴더의 하위 폴더들을 저장
sub_files = defaultdict(list)       # 특정 폴더의 바로 아래 하위 파일들을 저장

def backtracking(folder):

    # memoization한 값이 있을 경우, 해당 값을 반환
    if folder_to_files[folder]:
        return folder_to_files[folder]
    
    # memoization한 값이 없을 경우
    files = []
    files.extend(sub_files[folder])         # 바로 아래 하위 파일들 먼저 추가
    for sub_folder in sub_folders[folder]:  # 하위 폴더들 모두 탐색
        files.extend(backtracking(sub_folder))

    folder_to_files[folder] = files # 계산 결과, 메모이제이션 후 결과값 반환
    return files

if __name__ == "__main__":
    N, M = map(int, input().split())

    # 파일/폴더 여부에 따라서 sub_folders와 sun_files를 업데이트
    for _ in range(N + M):
        parent, current, isFolder = input().split()
        if int(isFolder):
            sub_folders[parent].append(current)
        else:
            sub_files[parent].append(current)

    # 입력에 대한 출력
    Q = int(input())
    for _ in range(Q):
        folder = input().split('/')[-1] # 가장 마지막 폴더만이 고려해야하는 인자
        files = backtracking(folder)
        print(len(set(files)), len(files))