package codetree.intermidiate_low.dfs.determine_escapableness_with_2_ways;

import java.util.*;
import java.io.*;

/**
 * 문제 : 두 방향 탈출 가능 여부 판별하기
 * 소요 시간 : 41분
 * 링크 : https://www.codetree.ai/missions/2/problems/determine-escapableness-with-2-ways/description
 */
public class Main {
    public static int n, m;
    public static int[][] grid;
    public static int[][] visited;
    public static int answer = 0;
    public static int[] dr = {1, 0};
    public static int[] dc = {0, 1};

    public static void main(String[] args) throws IOException {
        input();
        dfs(0, 0);
        System.out.print(answer);
    }

    public static boolean inRange(int r, int c){
        return r >= 0 && r < n && c >= 0 && c < m;
    }

    public static void dfs(int r, int c) {
        visited[r][c] = 1;
        if(answer == 1 || (r == n-1 && c == m-1)) {
            answer = 1;
            return;
        }


        for(int i = 0; i < 2; i++){
            int nr = r + dr[i];
            int nc = c + dc[i];

            if(!inRange(nr, nc) || grid[nr][nc] == 0 || visited[nr][nc] == 1){
                continue;
            }

            dfs(nr, nc);
        }
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        grid = new int[n][m];
        visited = new int[n][m];

        for(int i = 0; i < n; i++){
            int[] temp = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
            grid[i] = temp;
        }
    }
}