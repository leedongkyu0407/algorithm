import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
	//입장 확인 학회원 -> 시작 시간 이전에 대화 기록 있음
	//퇴장 확인 학회원 -> 종료 시간 이후 스트리밍 종료 이전 대화 기록 있음
	//공백 기준 시각과 이름 분할
	//시간에서 : 기준 시간과 분 분할
	//분으로 모두 변환하여 계산
	//입장 학회원 배열 / 퇴장 학회원 배열 따로 관리 -> 무조건 런타임 에러 나는 듯
	//HashMap 사용
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		int Start = toMinute(st.nextToken());
		int End = toMinute(st.nextToken());
		int Quit = toMinute(st.nextToken());
		Map<String, Boolean> attend = new HashMap<>();
		
		int ans = 0;
		String input;
		while((input = bf.readLine()) != null) {
			
			st = new StringTokenizer(input);
			int m = toMinute(st.nextToken());
			String name = st.nextToken();
//			System.out.println("시간 : "+m+", 이름: "+name);
//			스트리밍 종료 이후는 확인할 필요 없음
			if (m > Quit) {
				break;
			}
//			입장 학회원 세팅
			if(m <= Start) {
				attend.put(name, true);
				continue;
			}
			
//			퇴장 학회원 확인
			if(End <=m && m <= Quit) {
				if(attend.containsKey(name) && attend.get(name)) {
					ans += 1;
//					System.out.println(name);
					//퇴장처리 -> 다시 확인 반복하지 않도록
					attend.put(name, false);
				}
			}
		}
		System.out.println(ans);
		
	}
	
	//HH:MM형식으로 들어온 인자 파싱 후 분으로 통일 메서드
	static int toMinute(String hm) {
		String[] input = hm.split(":");
		int h = Integer.parseInt(input[0]);
		int m = Integer.parseInt(input[1]);
		return h*60+m;
	}
}
