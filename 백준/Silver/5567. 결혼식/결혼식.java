import java.io.*;
import java.util.*;

public class Main {

	static int N, M;
	static List<List<Integer>> graph = new ArrayList<>();
	static boolean[] isInvited;
	
	public static void main(String[] args) throws Exception {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(bf.readLine());
		M = Integer.parseInt(bf.readLine());
		
		for(int i=0;i<N+1;i++) {
			graph.add(new ArrayList<Integer>());
		}
		
		for(int i=0;i<M;i++) {
			StringTokenizer friend_input = new StringTokenizer(bf.readLine());
			int f1 = Integer.parseInt(friend_input.nextToken());
			int f2 = Integer.parseInt(friend_input.nextToken());
			graph.get(f1).add(f2);
			graph.get(f2).add(f1);		
		}
		
		isInvited = new boolean[N+1];
		bfs(new int[] {1, 0});
		int ans = 0;
		for(int i=2;i<N+1;i++) {
			if(isInvited[i])
				ans++;
		}
		System.out.println(ans);
	}
	
	private static void bfs(int[] start) {
		Queue<int[]> q = new ArrayDeque<int[]>();
		q.add(start);
		isInvited[start[0]] = true;
		
		int point = start[0];
		int depth = start[1];
		
		while(!q.isEmpty()) {
			
			int[] now = q.poll();
			
			point = now[0];
			depth = now[1];
			
			if(depth>=2)
				continue;
			
			for(int p:graph.get(point)) {
				if(!isInvited[p]) {
					isInvited[p] = true;
					q.add(new int[] {p, depth+1});					
				}
			}
		}
	}
}