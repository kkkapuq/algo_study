package codetree.intermidiate_low.backtracking.step_2.yutnori_1d;

/**
 * 문제 : 1차원 윷놀이
 * 소요 시간 : 30분
 * 링크 : https://www.codetree.ai/missions/2/problems/yutnori-1d/description
 */
import java.util.*;
import java.io.*;

public class Main {
    public static int N, M, K;
    public static int[] scores;
    public static int[] yuts;
    public static int answer = 0;

    public static void main(String[] args) throws IOException {
        input();
        recursion(0);
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        scores = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        yuts = new int[K];
        for(int i = 0; i < K; i++){
            yuts[i] = 1;
        }
    }

    public static int calc() {
        int temp = 0;
        for(int yut : yuts){
            if(yut >= M){
                temp++;
            }
        }
        return temp;
    }

    public static void recursion(int cnt){
        answer = Math.max(answer, calc());

        if(cnt == N){
            return;
        }

        for(int i = 0; i < K; i++){
            // 이미 m을 넘은 친구는 계산하지 않는다.
            if(yuts[i] >= M){
                continue;
            }
            yuts[i] += scores[cnt];
            recursion(cnt + 1);
            yuts[i] -= scores[cnt];
        }
    }
}
