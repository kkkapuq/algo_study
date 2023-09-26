package backjoon.Implementation.Silver_5_2828;

import java.io.*;

/**
 * 문제 : 사과 담기 게임
 * 링크 : https://www.acmicpc.net/problem/2828
 * 소요시간 : 18분
 */
public class Silver_V_2828 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter((new OutputStreamWriter(System.out)));

        String[] arr = br.readLine().split(" ");
        int n = Integer.parseInt(arr[0]);
        int m = Integer.parseInt(arr[1]);

        int s = 1, e = m, dist = 0;

        int j = Integer.parseInt(br.readLine());

        for (int i = 0; i < j; i++) {
            int apple = Integer.parseInt(br.readLine());

            if(apple < s){
                int movement = s - apple;
                s -= movement;
                e -= movement;
                dist += movement;
            } else if (apple > e) {
                int movement = apple - e;
                s += movement;
                e += movement;
                dist += movement;
            }
        }

        bw.write(Integer.toString(dist));

        br.close();
        bw.close();
    }
}
