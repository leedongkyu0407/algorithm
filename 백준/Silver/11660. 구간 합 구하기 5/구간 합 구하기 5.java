import java.io.*;
import java.util.*;

public class Main {

	static int N, M;
	static int[][] board;
	static StringBuilder sb = new StringBuilder();
	
	static void sumStack() {
		for(int i=1;i<N+1;i++) {
			for(int j=1;j<N+1;j++) {
				board[i][j] += (board[i][j-1] + board[i-1][j] - board[i-1][j-1]);
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		board = new int[N+1][N+1];
		
		for(int i=1;i<N+1;i++) {
			st = new StringTokenizer(bf.readLine());
			for(int j=1;j<N+1;j++) {
				board[i][j] = Integer.parseInt(st.nextToken());				
			}
		}
		
		sumStack();
		
		for(int i=0;i<M;i++) {
			st = new StringTokenizer(bf.readLine());
			int y1 = Integer.parseInt(st.nextToken());
			int x1 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			
			int result = board[y2][x2]-board[y2][x1-1] - board[y1-1][x2] + board[y1-1][x1-1]; 
			sb.append(result).append("\n");
		}
		System.out.println(sb);
	}
}
