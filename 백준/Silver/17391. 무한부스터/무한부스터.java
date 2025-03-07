import java.io.*;
import java.util.*;

public class Main {

   static int N, M;
   static int[][] maps, dp;
   static int[][] deltas = new int[][] {{0, 1}, {1, 0}};
   static boolean[][] visited;

   private static void calcMin(int startX, int startY) {
	   dp[startX][startY] = 0;
	      
	   for(int i=0;i<N;i++) {
		   for(int j=0;j<M;j++) {
			   for(int k=0;k<2;k++) {
				   int moveX = deltas[k][0];
				   int moveY = deltas[k][1];
//	    		   최대 움직일 수 있는 거리  
				   int move = maps[i][j];

				   while(move > 0) {  
//					   X, Y가 움직일 수 있는 최대거리부터 0까지 줄여가며 계산
					   int nowX = i+moveX*move; 
					   int nowY = j+moveY*move;
//					   보드판을 벗어나지 않는다면 
					   if(nowX>=0 && nowX<N && nowY>=0 && nowY<M)
//						   해당 X,Y 좌표에 처음 왔을 경우
						   if(dp[nowX][nowY] == -1)
							   dp[nowX][nowY] = dp[i][j]+1;
						   else {
//							   이미 방문한 적이 있어 값이 갱신되어 있는 경우
							   dp[nowX][nowY] = Math.min(dp[i][j]+1, dp[nowX][nowY]);
						   }
					   	move--;
	        		  }    			  
	    		  }
	    	  }
	      }	   
   }
   
   public static void main(String[] args) throws Exception {
      BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
      StringTokenizer size = new StringTokenizer(bf.readLine());
      N = Integer.parseInt(size.nextToken());
      M = Integer.parseInt(size.nextToken());
      
      maps = new int[N][M];
      for(int i=0;i<N;i++) {
         StringTokenizer line = new StringTokenizer(bf.readLine());
         for(int j=0;j<M;j++) {
            maps[i][j] = Integer.parseInt(line.nextToken());
         }
      }
      
      dp = new int[N][M];
      
      for(int i=0;i<N;i++) {
    	  for(int j=0;j<M;j++) {
    		  dp[i][j] = -1;
    	  }
      }
      
      calcMin(0, 0);
      System.out.println(dp[N-1][M-1]);
   }
}
