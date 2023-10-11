import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(st.nextToken());

        while(T-- > 0) {
            Set<Integer> note = new HashSet<>();
            int n = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            for(int i = 0; i < n; i++) {
                note.add(Integer.parseInt(st.nextToken()));
            }

            int m = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            for(int i = 0; i < m; i++) {
                int num = Integer.parseInt(st.nextToken());
                if(note.contains(num)) {
                    sb.append("1\n");
                }else {
                    sb.append("0\n");
                }
            }
        }
        System.out.println(sb.toString());
    }
}