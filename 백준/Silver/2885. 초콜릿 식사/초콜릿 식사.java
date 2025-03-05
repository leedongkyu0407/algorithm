import java.io.*;
import java.util.*;

public class Main {

	static int K;
	
	public static void main(String[] args) throws Exception {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		K = Integer.parseInt(bf.readLine());
		
		int t = 1;
		
//		초콜릿의 크기가 K보다 커지도록
		while(t<K) {
			t*=2;
		}
		
		int cnt = 0;
		int temp=t;
		
//		K가 1,2,4,8...이 아닐 때
		if(temp!=K) {
			while(K != 0) {
				temp /= 2;
//				반으로 가른 게 K개보다 작거나 같으면 사용
				if (K >= temp) {
					K -= temp;
				}
//				쪼개기
				cnt++;
			}
		}
		System.out.println(t+" "+cnt);
	}
}
