import java.util.*;
import java.io.*;

public class Main {
	static Stack<Integer> stack = new Stack<Integer>();

	   private static void calc(String input) {
		   for(int i=0;i<input.length();i++) {
		         char c = input.charAt(i);
		         
		         if(c == '(') {
		            stack.push(-1);
		         } else if(c == ')') {
		        	int sum = 0;
		        	
		            while(!stack.isEmpty() && stack.peek()!=-1) {
		               sum += stack.pop();
		            }
		            
		            if(!stack.isEmpty()) {
		            	stack.pop();
		            }
		            
		            stack.push(sum);
		         }
		         
		         else if('2'<=c && c<='9'){
		            if(!stack.isEmpty()) {
		            	int num = c - '0';
		            	int temp = stack.pop();
		            	stack.push(num*temp);
		            }
		         } else {
		            if(c == 'H') {
		               stack.push(1);
		            }
		            else if(c == 'C') {
		               stack.push(12);
		            }
		            else if(c == 'O') {
		               stack.push(16);
		            }
		         }
		      }
	   }
	   
   public static void main(String[] args) throws Exception {
      BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
      String input = bf.readLine();
      
      calc(input);
      int ans=0;
      while(!stack.isEmpty()) {
         ans += stack.pop();
      }
      System.out.println(ans);
   }
   
}