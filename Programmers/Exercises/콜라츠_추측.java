class Solution {
    public int solution(int num) {
        int answer = 0;
        while (num != 1) {
        	answer += 1;
        	if (answer == 501) {
        		answer = -1;
        		break;
        	}
        	if (num % 2 == 1) {
        		num = num * 3 + 1;
        	} else {
        		num /= 2;
        	}
        }
        if (num != 1) {
        	answer = -1;
        }
        return answer;
    }
}