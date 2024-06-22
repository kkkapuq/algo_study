package codetree.intermidiate_low.bfs.knight_movements;

import java.util.*;
import java.io.*;

/**
 * 문제 : 나이트
 * 소요 시간 : 20분
 * 링크 : https://www.codetree.ai/missions/2/problems/knight-movements/description
 */
public class Main {
    public static int n;
    public static int[][] grid, distances;
    public static boolean[][] visited;

    public static int r1, c1, r2, c2;
    public static int answer = 0;

    public static int[] dr = {-1, -2, -2, -1, 1, 2, 2, 1};
    public static int[] dc = {-2, -1, 1, 2, 2, 1, -1, -2};

    public static void main(String[] args) throws IOException {
        input();
        bfs(r1, c1, 0);
        if(r1 == r2 && c1 == c2){
            System.out.print(0);
        } else {
            System.out.print(distances[r2][c2] != 0 ? distances[r2][c2] : -1);
        }
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < n && c >= 0 && c < n;
    }

    public static boolean canGo(int r, int c) {
        if(!inRange(r, c) || visited[r][c])
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

            // System.out.println("===");
            // for(int[] arr : distances) {
            //     System.out.println(Arrays.toString(arr));
            // }
            // System.out.println("===");

            for(int i = 0; i < 8; i++){
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

        grid = new int[n][n];
        distances = new int[n][n];
        visited = new boolean[n][n];

        st = new StringTokenizer(br.readLine());
        r1 = Integer.parseInt(st.nextToken()) - 1;
        c1 = Integer.parseInt(st.nextToken()) - 1;
        r2 = Integer.parseInt(st.nextToken()) - 1;
        c2 = Integer.parseInt(st.nextToken()) - 1;
    }
}
