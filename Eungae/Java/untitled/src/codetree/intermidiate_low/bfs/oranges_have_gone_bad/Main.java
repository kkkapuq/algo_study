package codetree.intermidiate_low.bfs.oranges_have_gone_bad;

import java.util.*;
import java.io.*;

/**
 * 문제 : 상한 귤
 * 소요 시간 : 25분
 * 링크 : https://www.codetree.ai/missions/2/problems/oranges-have-gone-bad/description
 */
public class Main {
    public static int n, k;
    public static int[][] grid, distances, answer;

    public static List<int[]> spoiledPos = new ArrayList<>();
    public static boolean[][] visited;

    public static Deque<int[]> q = new ArrayDeque<>();

    public static int[] dr = {-1, 1, 0, 0};
    public static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        input();

        for(int[] spoiled : spoiledPos){
            int r = spoiled[0];
            int c = spoiled[1];

            q.add(spoiled);

            visited[r][c] = true;
            distances[r][c] = 0;
        }
        bfs();
        print();
    }

    public static void print() {
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == 0){
                    System.out.print(-1 + " ");
                } else {
                    if(!visited[i][j])
                        System.out.print(-2 + " ");
                    else
                        System.out.print(distances[i][j] + " ");
                }
            }
            System.out.println();
        }
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < n && c >= 0 && c < n;
    }

    public static boolean canGo(int r, int c) {
        if(!inRange(r, c) || grid[r][c] == 0 || visited[r][c])
            return false;
        return true;
    }

    public static void bfs() {
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
        k = Integer.parseInt(st.nextToken());

        grid = new int[n][n];
        distances = new int[n][n];
        visited = new boolean[n][n];

        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < n; j++){
                int num = Integer.parseInt(st.nextToken());
                grid[i][j] = num;
                if(num == 2){
                    spoiledPos.add(new int[]{i, j});
                }
            }
        }
    }
}
