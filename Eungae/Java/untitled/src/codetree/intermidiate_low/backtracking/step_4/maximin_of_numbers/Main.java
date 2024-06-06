package codetree.intermidiate_low.backtracking.step_4.maximin_of_numbers;

import java.util.*;
import java.io.*;

/**
 * 문제 : 수들 중 최솟값 최대화하기
 * 소요 시간 : 10분
 * 링크 : https://www.codetree.ai/missions/2/problems/maximin-of-numbers/description
 */
public class Main {
    public static int n;
    public static int[][] grid;
    public static boolean[] visited;
    public static List<Integer> list = new ArrayList<>();
    public static int answer = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        input();
        recursion(0);
        System.out.print(answer);
    }

    public static void recursion(int currNum){
        if(currNum == n){
            int temp = Collections.min(list);
            answer = Math.max(answer, temp);
            return;
        }

        for(int i = 0; i < n; i++){
            if(visited[i])
                continue;

            visited[i] = true;

            list.add(grid[currNum][i]);
            recursion(currNum+1);
            list.remove(list.size()-1);

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