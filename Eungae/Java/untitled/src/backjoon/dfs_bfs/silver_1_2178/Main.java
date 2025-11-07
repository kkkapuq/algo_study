package backjoon.dfs_bfs.silver_1_2178;

import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.Array;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    private static int n, m;
    private static int[][] arr;
    private static boolean[][] visited;
    private static int[] dr = new int[]{-1, 1, 0, 0};
    private static int[] dc = new int[]{0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n][m];
        visited = new boolean[n][m];
        visited[0][0] = true;

        for(int i = 0; i < n; i++){
            String str = br.readLine();
            for (int j = 0; j < m; j++) {
                arr[i][j] = str.charAt(j) - '0';
            }
        }

        bfs(0, 0);
        System.out.println(arr[n-1][m-1]);
    }

    private static void bfs(int r, int c) {
        Deque<int[]> deque = new ArrayDeque<>();
        deque.add(new int[]{r, c});

        while (!deque.isEmpty()) {
            int[] current = deque.poll();
            int nowR = current[0];
            int nowC = current[1];

            for (int i = 0; i < 4; i++) {
                int nextR = nowR + dr[i];
                int nextC = nowC + dc[i];

                if (nextR >= n || nextR < 0 || nextC >= m || nextC < 0) {
                    continue;
                }
                if (visited[nextR][nextC] || arr[nextR][nextC] == 0) {
                    continue;
                }

                deque.add(new int[]{nextR, nextC});
                arr[nextR][nextC] = arr[nowR][nowC] + 1;
                visited[nextR][nextC] = true;
            }

        }

    }
}
