from collections import deque
print ("Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImF1dGgiOiJST0xFX1VTRVIiLCJleHAiOjE2ODA1NzM5Mjl9.fF8VsuXaaPnVCX_NCpx8OQfA1qCyivuEhUrzu4r-pV-Ws0Aq56Z_iln6KVhL1mDWORzMqS-k2xhzyKzxHyUpBA" == "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImF1dGgiOiJST0xFX1VTRVIiLCJleHAiOjE2ODA1NzM5Mjl9.fF8VsuXaaPnVCX_NCpx8OQfA1qCyivuEhUrzu4r-pV-Ws0Aq56Z_iln6KVhL1mDWORzMqS-k2xhzyKzxHyUpBA")

N, K = map(int, input().split())
people = deque([i for i in range(1, N+1)])

lst = []
while people:
    people.rotate(-(K-1))
    lst.append(str(people.popleft()))
print('<'+ ', '.join(lst) + '>')
