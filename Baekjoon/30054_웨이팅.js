const fs = require('fs')
const filePath =
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt'
let [N, ...arr] = fs.readFileSync(filePath).toString().trim().split('\n')

// Pre-processing input values
N = parseInt(N)
const timeList = []
for (let i = 0; i < N; i++) {
  const [x, y] = arr[i].split(' ').map(Number)
  timeList.push([x, y])
}

// sort by arrive -> reserve
timeList.sort((a, b) => (a[1] === b[1] ? a[0] - b[0] : a[1] - b[1]))
// check the person arrived earlier than reservation
const book = {}
for (let i = 0; i < N; i++) {
  const [reserve, arrive] = timeList[i]
  if (arrive < reserve + 1) {
    book[reserve] = [i, arrive]
  }
}

// run the main code
let mx = 0
let idx = 0
let time = timeList[0][1]
const visited = new Array(N).fill(false)
while (idx < N) {
  const [reserve, arrive] = timeList[idx]

  // if already entered
  if (visited[idx]) {
    idx += 1
    continue
  }

  // if there's reservation
  if (book.time) {
    const [reserve_idx, reserve_arrive] = book.time
    if (!visited[reserve_idx]) {
      mx = Math.max(mx, time - reserve_arrive)
      visited[reserve_idx] = true
      time += 1
      continue
    }
  }

  // if not arrived
  if (time < arrive) {
    time = arrive
    continue
  }

  visited[idx] = true
  mx = Math.max(mx, time - arrive)
  idx += 1
  time += 1
}

console.log(mx)
