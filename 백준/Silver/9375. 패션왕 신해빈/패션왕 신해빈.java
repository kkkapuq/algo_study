
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for (int tc = 0; tc < t; tc++) {
            int n = Integer.parseInt(br.readLine());
            Map<String, Integer> map = new HashMap<>();
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                String wear = st.nextToken(), category = st.nextToken();
                // 만약 해당 옷 종류가 없으면 2로 넣어주고(아무것도 안입은 경우를 계산하기 위해)
                if (!map.containsKey(category)) {
                    map.put(category, 2);
                } else {
                    // 옷 종류가 있다면 +1 해서 넣어준다.
                    map.put(category, map.get(category)+1);
                }
            }
            // 맵을 순회하면서 값 더해주기
            int cnt = 1;
            for (String str : map.keySet()) {
                cnt *= map.get(str);
            }
            System.out.println(cnt-1);
        }
    }
}
