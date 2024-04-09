package backjoon.brute_force.silver_1_15651;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Silver_1_15651 {
    static int N, M;
    static int[] selected;
    static StringBuilder sb = new StringBuilder();

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        selected = new int[M+1];
    }

    public static void recursion(int k) {
        if (k == M+1){
            // selected[1...M] 배열이 새롭게 탐색된 결과
            for(int i = 1; i <= M; i++){
                sb.append(selected[i]).append(' ');
            }
            sb.append('\n');
        } else {
            for (int i = 1; i <= N; i++){
                selected[k] = i;
                // k+1 번 ~ M 번을 모두 탐색하는 일이 남음
                recursion(k+1);
                selected[k] = 0;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        input();
        recursion(1);
        System.out.println(sb.toString());
    }

}
