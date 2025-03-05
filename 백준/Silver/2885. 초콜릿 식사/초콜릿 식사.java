import java.io.*;
import java.util.*;

public class Main {

	static int K;
	
	public static void main(String[] args) throws Exception {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		K = Integer.parseInt(bf.readLine());
		
		int t = 1;
		
		while(t<K) {
			t*=2;
		}
		
		int cnt = 0;
		int temp=t;
		
		if(temp!=K) {
			while(K != 0) {
				temp /= 2;
				if (K >= temp) {
					K -= temp;
				}
				cnt++;
			}
		}
		System.out.println(t+" "+cnt);
	}
}
