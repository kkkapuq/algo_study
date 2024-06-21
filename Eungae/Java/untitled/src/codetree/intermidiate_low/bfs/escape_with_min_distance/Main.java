package codetree.intermidiate_low.bfs.escape_with_min_distance;

import java.util.*;
import java.io.*;

/**
 * 문제 : 최소 경로로 탈출하기
 * 소요 시간 : 18분
 * 링크 : https://www.codetree.ai/missions/2/problems/escape-with-min-distance/description
 */
public class Main {
    public static int n, m;
    public static int[][] grid, distances;
    public static boolean[][] visited;

    public static int[] dr = {-1, 1, 0, 0};
    public static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        input();
        bfs(0, 0, 0);
        System.out.print(distances[n-1][m-1] != 0 ? distances[n-1][m-1] : -1);
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < n && c >= 0 && c < m;
    }

    public static boolean canGo(int r, int c) {
        if(!inRange(r, c) || grid[r][c] == 0 || visited[r][c])
            return false;
        return true;
    }

    public static void bfs(int sr, int sc, int dist) {
        Deque<int[]> q = new ArrayDeque<>();
        visited[sr][sc] = true;
        distances[sr][sc] = dist;
        q.add(new int[]{sr, sc});

        while(!q.isEmpty()) {
            int[] temp = q.poll();
            int r = temp[0];
            int c = temp[1];

            for(int i = 0; i < 4; i++){
                int nr = r + dr[i];
                int nc = c + dc[i];

                if(canGo(nr, nc)) {
                    distances[nr][nc] = distances[r][c] + 1;
                    q.add(new int[]{nr, nc});
                    visited[nr][nc] = true;
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
        distances = new int[n][m];
        visited = new boolean[n][m];

        for(int i = 0; i < n; i++){
            grid[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        }
    }
}
