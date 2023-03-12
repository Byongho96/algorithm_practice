import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> arrLst = new ArrayList<Integer>(); // arrLst 선언
        
        for (int n: arr) {
        	if (n % divisor == 0) {
        		arrLst.add(n);
        	}
        }
        if (arrLst.size() == 0) {
            arrLst.add(-1);
        }
        
        int[] answer = arrLst.stream().mapToInt(i->i).toArray();  // arrLst -> int[]
        Arrays.sort(answer);
            
        return answer;
    }
}