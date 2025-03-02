import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	//	안내멘트 N번 재생 / 안내 멘트 길이 / 연결 요청 간격
	static int N, L, D;

	private static int calc() {
		int bell = 0;
		
		int totalMusicEnd = N*L + (N-1)*5;
		
//		벨이 울리는 시간 확인
		while(true) {
			bell += D;
			
//			모든 노래가 끝나면 바로 벨소리 들음
			if(bell >= totalMusicEnd)
				return bell;
			
			// 현재 벨 시간이 어느 구간에 있는지 확인
	        boolean duringMusic = false;
	        for (int i = 0; i < N; i++) {
	            int musicStart = i * (L + 5); // i번째 노래 시작 시간
	            int musicEnd = musicStart + L; // i번째 노래 끝 시간
	            
	            // 벨이 노래 중에 울리는지 확인
	            if (musicStart <= bell && bell < musicEnd) {
	                duringMusic = true;
	                break;
	            }
	        }
	        
	        // 조용한 구간에 벨이 울리면 들을 수 있음
	        if (!duringMusic) {
	            return bell;
	        }
	    }	
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer input = new StringTokenizer(bf.readLine());
		N = Integer.parseInt(input.nextToken());
		L = Integer.parseInt(input.nextToken());
		D = Integer.parseInt(input.nextToken());
		System.out.println(calc());
	}
}