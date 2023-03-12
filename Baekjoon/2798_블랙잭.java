import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int M = sc.nextInt();
		
		int[] lst = new int[N];
		for(int i=0; i<N; i++) {
			lst[i] = sc.nextInt();
		}
		
		boolean flag = false; 
		int result = 0;
		for(int i=0; i<N-2; i++) {
			for(int j=i+1; j<N-1; j++) {
				for(int k=j+1; k<N; k++) {
					int sm = lst[i] + lst[j] + lst[k];
					if (sm < M) {
						result = Math.max(result, sm);
					} else if (sm == M) {
						result = M;
						flag = true;
						break;
					}
				}
				if (flag) {
					break;
				}
			}
			if (flag) {
				break;
			}
		}
		
		System.out.println(result);
	}

}