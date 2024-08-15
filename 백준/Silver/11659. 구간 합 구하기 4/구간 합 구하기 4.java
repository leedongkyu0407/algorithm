import java.io.*;
import java.util.*;

public class Main {
	
	static int N, M;
	static int[] board;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		board = new int[N+1];
		
		st = new StringTokenizer(bf.readLine());
		for(int i=1;i<=N;i++) {
			board[i] = Integer.parseInt(st.nextToken())+board[i-1];
		}
		
		for(int i=0;i<M;i++) {
			st = new StringTokenizer(bf.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			
			int result = board[end]-board[start-1];
			sb.append(result).append("\n");
		}
		System.out.println(sb.toString());
	}
}
