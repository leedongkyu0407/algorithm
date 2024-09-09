import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

	static int N, M;
	static ArrayList<Edge>[] graph;
	static boolean[] visited;

	static class Edge implements Comparable<Edge>{

		int home;
		int cost;
		
		Edge(int home, int cost){
			this.home = home;
			this.cost = cost;
		}
		
		@Override
		public int compareTo(Edge o) {
			return this.cost-o.cost;
		}
	}
	
	static int prim(int start) {		
		PriorityQueue<Edge> pq = new PriorityQueue<>();
		pq.add(new Edge(start, 0));
		
		int total = 0;
//		경로 중 가장 유지비가 큰 길 찾기
		int maxC = 0;
		while(!pq.isEmpty()) {
			Edge now = pq.poll();
			int home = now.home;
			int cost = now.cost;
			if(visited[home]) continue;
			
			visited[home] = true;
			total += cost;
			maxC = Math.max(maxC, cost);
			for (Edge nxt : graph[home]) {
				if(!visited[nxt.home]) pq.add(nxt);
			}
		}
		return total-maxC;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer input = new StringTokenizer(bf.readLine());
		N = Integer.parseInt(input.nextToken());
		M = Integer.parseInt(input.nextToken());
		
		graph = new ArrayList[N+1];
		for(int i=0;i<=N;i++) {
			graph[i] = new ArrayList<>();
		}
		visited = new boolean[N+1];
		for(int i=0;i<M;i++) {
			StringTokenizer line = new StringTokenizer(bf.readLine());
			int a = Integer.parseInt(line.nextToken());
			int b = Integer.parseInt(line.nextToken());
			int c = Integer.parseInt(line.nextToken());
//			양방향 그래프
			graph[a].add(new Edge(b, c));
			graph[b].add(new Edge(a, c));
		}
		
		System.out.println(prim(1));
	}
}