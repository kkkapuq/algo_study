package codetree.intermidiate_low.bfs.stay_out_of_rain;

import java.util.*;
import java.io.*;

/**
 * 문제 : 비를 피하기
 * 소요 시간 : 38분
 * 링크 : https://www.codetree.ai/missions/2/problems/stay-out-of-rain/description
 */
public class Main {
    public static int n, h, m;
    public static int[][] grid, distances, answer;

    public static List<int[]> peoplePos = new ArrayList<>();
    public static List<int[]> exitPos = new ArrayList<>();
    public static boolean[][] visited;

    public static int[] dr = {-1, 1, 0, 0};
    public static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        input();

        for(int[] people : peoplePos){
            int r = people[0];
            int c = people[1];
            bfs(r, c, 0);
            int dist = findMin();
            answer[r][c] = dist == Integer.MAX_VALUE ? -1 : dist;

            distances = new int[n][n];
            visited = new boolean[n][n];
        }

        print();
    }

    public static void print() {
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                System.out.print(answer[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static int findMin() {
        int dist = Integer.MAX_VALUE;
        for(int[] exit : exitPos){
            int r = exit[0];
            int c = exit[1];
            if(distances[r][c] != 0){
                dist = Math.min(distances[r][c], dist);
            }
        }
        return dist;
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < n && c >= 0 && c < n;
    }

    public static boolean canGo(int r, int c) {
        if(!inRange(r, c) || grid[r][c] == 1 || visited[r][c])
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
        h = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        grid = new int[n][n];
        distances = new int[n][n];
        visited = new boolean[n][n];
        answer = new int[n][n];

        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < n; j++){
                int num = Integer.parseInt(st.nextToken());
                grid[i][j] = num;
                if(num == 2){
                    peoplePos.add(new int[]{i, j});
                } else if(num == 3){
                    exitPos.add(new int[]{i, j});
                }
            }
        }
    }
}