import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Solution {

	static StringBuilder sb = new StringBuilder();
	static int N;
	static String D;
	static int[][] board;
	static HashMap<String, Integer> map = new HashMap<>();

	static void play() {
		int d = map.get(D);
		if(d==3) {
			board = rotateLeft();
		} 
		else {
			for(int i=0;i<d;i++) {
				board = rotateRight();
			}
		}
		
		game();
		
		if(d==3) {
			board = rotateRight();
		}
		else {
			for(int i=0;i<d;i++) {
				board = rotateLeft();
			}
		}
	}
	
	static int[][] rotateRight() {
		int[][] arr = new int[N][N];
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				arr[j][N-i-1] = board[i][j];
			}
		}
		return arr;
	}
	
	static int[][] rotateLeft() {
		int[][] arr = new int[N][N];
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				arr[N-j-1][i] = board[i][j];
			}
		}
		return arr;
	}
	
	static void game() {
		for(int x=0;x<N;x++) {
//			자리를 채울 블럭의 인덱스
			int targetIdx = 0;
//			현재 열만 사용하기 위해 따로 저장
			int[] arr = new int[N];	
//			이미 합쳐진 적 있는지 확인
			boolean[] isMerged = new boolean[N];
			
			for(int y=0;y<N;y++) {
				arr[y] = board[y][x];
			}
			
			for(int y=0;y<N;y++) {
				if(arr[y] == 0) continue;
				
				if(arr[y] !=0) {
//					이전 값과 같으면 합치기
					if(targetIdx>0 && arr[targetIdx-1] == arr[y] && !isMerged[targetIdx-1]) {
						arr[targetIdx-1] *= 2;
						arr[y] = 0;
//						합친 블럭임을 표시
						isMerged[targetIdx-1] = true;
					}
					else {						
						arr[targetIdx] = arr[y];
//						앞자리가 0이어서 이동한 경우
						if(targetIdx != y) {
							arr[y] = 0;
						}
						targetIdx++;
					}
				}
			}
//			열 하나에 대해 작업이 끝나면 다시 보드에 저장
			for(int y=0;y<N;y++) {
				board[y][x] = arr[y];
			}
		}
	}
	
	static void setMap() {
		map.put("up", 0);
		map.put("left", 1);
		map.put("down", 2);
		map.put("right", 3);
	}

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(bf.readLine());
		
		for(int t=1;t<=T;t++) {
			StringTokenizer input = new StringTokenizer(bf.readLine());
			N = Integer.parseInt(input.nextToken());
			D = input.nextToken();
			board = new int[N][N];
			
			for(int i=0;i<N;i++) {
				StringTokenizer line = new StringTokenizer(bf.readLine());
				for(int j=0;j<N;j++) {
					board[i][j] = Integer.parseInt(line.nextToken());
				}
			}
			setMap();
			play();
			
			sb.append("#").append(t).append("\n");
			
			for(int i=0;i<N;i++) {
				for(int j=0;j<N;j++) {
					sb.append(board[i][j]).append(" ");
				}
				sb.append("\n");
			}
			
		}
		System.out.println(sb.toString());
	}
	
}