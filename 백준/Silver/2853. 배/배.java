import java.io.*;

public class Main {

	static int N;
	static int[] days;
	static boolean[] visited;

	private static int countShip() {
		int first = days[0];
		int count = 0;
		
		for(int i=1;i<N;i++) {
			int gap = days[i]-first;
			if(visited[i]!=true) {
				count++;
				visited[i] = true;
				for(int j=i+1;j<N;j++) {
					if(visited[j]==false && (days[j]-first)%gap==0) {
						visited[j] = true;
					}
				}
			}
		}
		return count;
	}
	
	public static void main(String[] args) throws Exception{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(bf.readLine());
		days = new int[N];
		visited = new boolean[N];
		
		for(int i=0;i<N;i++) {
			days[i] = Integer.parseInt(bf.readLine());
		}
	
		System.out.println(countShip());
	}
}
