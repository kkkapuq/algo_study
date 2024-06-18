package codetree.intermidiate_low.bfs.determine_escapableness_with_4_ways;

import java.util.*;
import java.io.*;


/**
 * 문제 : 네 방향 탈출 가능 여부 판별하기
 * 소요 시간 : 15분
 * 링크 : https://www.codetree.ai/missions/2/problems/determine-escapableness-with-4-ways/introduction
 */

public class Main {
    public static int n, m;
    public static int[][] grid;
    public static boolean[][] visited;
    public static int answer = 0;
    public static int[] dr = {-1, 1, 0, 0};
    public static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        input();
        bfs(0, 0);
        System.out.print(visited[n-1][m-1] ? 1 : 0);
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < n && c >= 0 && c < m;
    }

    public static boolean canGo(int r, int c) {
        if(!inRange(r, c) || grid[r][c] == 0 || visited[r][c])
            return false;
        return true;
    }

    public static void bfs(int r, int c) {
        visited[r][c] = true;
        Deque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{r, c});

        while(!q.isEmpty()) {
            int[] cur = q.poll();
            int cr = cur[0];
            int cc = cur[1];

            for(int i = 0; i < 4; i++){
                int nr = cr + dr[i];
                int nc = cc + dc[i];

                if(!canGo(nr, nc)){
                    continue;
                } else {
                    visited[nr][nc] = true;
                    q.add(new int[]{nr, nc});
                }
            }
        }
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        grid = new int[n][m];
        visited = new boolean[n][m];

        for(int i = 0; i < n; i++){
            int[] temp = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            grid[i] = temp;
        }
    }
}