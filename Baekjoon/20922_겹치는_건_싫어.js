// 1. 하나의 값을 입력받을 때
// const fs = require('fs');
// const input = fs.readFileSync("/dev/stdin").toString().trim();
// 2. 공백으로 구분된 한 줄의 값들을 입력받을 때
// const fs = require('fs');
// const input = fs.readFileSync("/dev/stdin").toString().trim().split(" ");
// 3. 여러 줄의 값들을 입력받을 때
// const fs = require('fs');
// const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
// 4. 첫 번째 줄에 자연수 n을 입력받고, 그 다음줄에 공백으로 구분된 n개의 값들을 입력받을 때
// const fs = require('fs');
// const [n, ...arr] = fs.readFileSync("/dev/stdin").toString().trim().split(/\s/);
// 5. 첫 번째 줄에 자연수 n을 입력받고, 그 다음줄부터 n개의 줄에 걸쳐 한 줄에 하나의 값을 입력받을 때
// const fs = require('fs');
// const [n, ...arr] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
// 6. 하나의 값 또는 공백으로 구분된 여러 값들을 여러 줄에 걸쳐 뒤죽박죽 섞여서 입력받을 때
//   ex) n 입력 - 공백으로 구분된 n개의 값 입력 - m 입력 - 여러 줄에 걸쳐 m개의 값 입력
// const fs = require('fs');
// const input = fs.readFileSync("/dev/stdin").toString().trim().split(/\s/);
// const n = input[0];
// const n_arr = input.slice(1, n+1);
// const [m, ...m_arr] = input.slice(n+1);
// 출처: https://overcome-the-limits.tistory.com/25 [Plus Ultra:티스토리]

const fs = require('fs')
let input = fs.readFileSync('input.txt').toString().trim().split("\n");
//let input = fs.readFileSync('./dev/stdin').toString().trim().split("\n");

const [N, K] = input[0].trim().split(' ')
const lst = input[1].split(" ").map(Number)
// console.log(input)
// console.log(lst)
let obj = new Object()
let [cnt, i, j] = [0, 0, 0]

for(j = 0; j < N; j++) {
    if (obj[lst[j]] === undefined) {
    obj[lst[j]] = 1
    } else {
        obj[lst[j]] += 1
    }
    // console.log(obj)
    if (obj[lst[j]] > K) {
        while (true) {
            obj[lst[i]] -= 1
            if (lst[i] === lst[j]) {
                i += 1
                break
            }
            i += 1
        }
    }
    cnt = Math.max(cnt, j - i + 1)
}

console.log(cnt)
