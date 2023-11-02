const fs = require('fs')
const filePath =
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt'
let [N, string] = fs.readFileSync(filePath).toString().trim().split('\n')

N = parseInt(N)

// list for logging the data
const count_log = new Array(N + 1).fill(0)

let mx = 0
const stack = []

let c = null
let si = null
for (let i = 0; i < N; i++) {
  c = string[i]
  if (c === '(') {
    stack.push(i)
  } else if (stack.length > 0) {
    si = stack.pop()
    count_log[i + 1] = i - si + 1 + count_log[si]
    mx = Math.max(mx, count_log[i + 1])
  }
}

console.log(mx)
