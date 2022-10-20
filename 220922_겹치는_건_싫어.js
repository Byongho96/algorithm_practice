const fs = require('fs')
let input = fs.readFileSync('./dev/stdin').toString()
input = input.split('\n')

const [N, K] = input[0].split(' ')
const lst = input.slice(1).map(Number)

let obj = new Object()
let [cnt, i, j] = [0, 0, 0]

for(j=0; j=N; j++) {
  if (obj[lst[j]]) {

  } 
  // obj[]
}
for j in range(N):
    dic[lst[j]] += 1
    if dic[lst[j]] > K:
        while True:
            dic[lst[i]] -= 1
            if lst[i] == lst[j]:
                i += 1
                break
            i += 1
    cnt = max(cnt, j - i + 1)

print(cnt)