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
	    			  
				   int move = maps[i][j];
	        		  
				   while(move > 0) {  
					   int nowX = i+moveX*move; 
					   int nowY = j+moveY*move;
					   if(nowX>=0 && nowX<N && nowY>=0 && nowY<M)
						   if(dp[nowX][nowY] == -1)
							   dp[nowX][nowY] = dp[i][j]+1;
						   else {
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