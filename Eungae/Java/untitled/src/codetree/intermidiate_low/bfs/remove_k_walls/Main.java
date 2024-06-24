package codetree.intermidiate_low.bfs.remove_k_walls;

import java.util.*;
import java.io.*;

/**
 * 문제 : k개의 벽 없애기
 * 소요 시간 : 42분
 * 링크 : https://www.codetree.ai/missions/2/problems/remove-k-walls/description
 */
public class Main {
    public static int n, k;
    public static int[][] grid, distances;
    public static boolean[][] visited;
    public static int answer = Integer.MAX_VALUE;

    public static List<int[]> wallPos = new ArrayList<>();
    public static List<int[]> selectedWalls = new ArrayList<>();
    public static int r1, c1, r2, c2;

    public static int[] dr = {-1, 1, 0, 0};
    public static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        input();
        findMin(0, 0);
        if(answer == Integer.MAX_VALUE){
            System.out.print(-1);
        } else {
            System.out.print(r1 == r2 && c1 == c2 ? 0 : answer);
        }
    }

    public static void breakingWalls() {
        for(int[] wall : selectedWalls) {
            int r = wall[0];
            int c = wall[1];
            grid[r][c] = 0;
        }
    }

    public static void bfs() {
        Deque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{r1, c1});
        visited[r1][c1] = true;
        distances[r1][c1] = 0;

        while(!q.isEmpty()){
            int[] temp = q.poll();
            int r = temp[0];
            int c = temp[1];

            for(int i = 0; i < 4; i++){
                int nr = r + dr[i];
                int nc = c + dc[i];
                if(canGo(nr, nc)){
                    visited[nr][nc] = true;
                    distances[nr][nc] = distances[r][c] + 1;
                    q.add(new int[]{nr, nc});
                }
            }
        }
    }

    public static void restoreWalls() {
        for(int[] wall : selectedWalls) {
            int r = wall[0];
            int c = wall[1];
            grid[r][c] = 1;
        }

        visited = new boolean[n][n];
        distances = new int[n][n];
    }

    public static int calc() {
        int cnt = 0;
        breakingWalls();
        bfs();

        cnt = distances[r2][c2];
        restoreWalls();
        return cnt == 0 ? Integer.MAX_VALUE : cnt;
    }

    public static void findMin(int idx, int cnt){
        if(cnt > k)
            return;
        if(idx == wallPos.size()){
            if(cnt == k){
                answer = Math.min(answer, calc());
            }
            return;
        }

        selectedWalls.add(wallPos.get(idx));
        findMin(idx+1, cnt+1);
        selectedWalls.remove(selectedWalls.size()-1);
        findMin(idx+1, cnt);
    }

    public static boolean inRange(int r, int c){
        return r >= 0 && r < n && c >= 0 && c < n;
    }

    public static boolean canGo(int r, int c){
        if(!inRange(r, c) || grid[r][c] == 1 || visited[r][c])
            return false;
        return true;
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
                if(num == 1){
                    wallPos.add(new int[]{i, j});
                }
            }
        }

        st = new StringTokenizer(br.readLine());
        r1 = Integer.parseInt(st.nextToken()) - 1;
        c1 = Integer.parseInt(st.nextToken()) - 1;
        st = new StringTokenizer(br.readLine());
        r2 = Integer.parseInt(st.nextToken()) - 1;
        c2 = Integer.parseInt(st.nextToken()) - 1;
    }
}
