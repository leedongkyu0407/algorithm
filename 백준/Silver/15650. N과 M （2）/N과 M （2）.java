import java.io.*;
import java.util.*;

public class Main {
	static int N, M;
	static StringBuilder sb = new StringBuilder();
	static int[] arr;
	
	static void comb(int start, int depth) {
		if(depth == M) {
			for(int i=0;i<M;i++) {
				sb.append(arr[i]+1).append(" ");
			}
			sb.append("\n");
			return;
		}
		
		for(int i=start;i<N;i++	) {
			arr[depth] = i;
			comb(i+1, depth+1);
		}
	}
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		arr = new int[M];
		
		comb(0, 0);
		System.out.println(sb.toString());
	}
}
