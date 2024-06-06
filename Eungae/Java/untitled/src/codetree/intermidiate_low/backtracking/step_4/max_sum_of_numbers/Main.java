package codetree.intermidiate_low.backtracking.step_4.max_sum_of_numbers;

import java.util.*;
import java.io.*;

/**
 * 문제 : 수들의 합 최대화하기
 * 소요 시간 : 36분
 * 링크 : https://www.codetree.ai/missions/2/problems/max-sum-of-numbers/description
 */
public class Main {
    public static int n;
    public static int[][] grid;
    public static boolean[] visited;
    public static int answer = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        input();
        recursion(0, 0);
        System.out.print(answer);
    }

    public static void recursion(int currNum, int sum){
        if(currNum == n){
            answer = Math.max(answer, sum);
            return;
        }

        for(int i = 0; i < n; i++){
            if(visited[i])
                continue;

            visited[i] = true;

            recursion(currNum+1, sum + grid[currNum][i]);

            visited[i] = false;
        }
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringTokenizer st;

        grid = new int[n][n];
        visited = new boolean[n];

        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < n; j++){
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }
    }
}