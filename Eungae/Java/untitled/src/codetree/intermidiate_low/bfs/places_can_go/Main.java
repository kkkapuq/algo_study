package codetree.intermidiate_low.bfs.places_can_go;

import java.io.*;
import java.util.*;

/**
 * 문제 : 갈 수 있는 곳들
 * 소요 시간 : 44분
 * 링크 : https://www.codetree.ai/missions/2/problems/places-can-go/description
 */
public class Main {
    public static int n, k;
    public static int[][] grid;
    public static int[][] visitedGrid;
    public static boolean[][] visited;
    public static int answer = 0;
    public static int[][] coordinates;
    public static int[] dr = {-1, 1, 0, 0};
    public static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException{
        input();
        for(int i = 0; i < k; i++){
            int r = coordinates[i][0];
            int c = coordinates[i][1];

            // visited 초기화
            // visited = new boolean[n][n];
            bfs(r, c);
        }

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++){
                if(visitedGrid[i][j] == 2){
                    answer++;
                }
            }
        }

        System.out.print(answer);
    }

    public static void bfs(int r, int c) {
        Deque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{r, c});
        visited[r][c] = true;
        visitedGrid[r][c] = 2;

        while(!q.isEmpty()) {
            int[] temp = q.poll();
            int cr = temp[0];
            int cc = temp[1];

            for(int i = 0; i < 4; i++){
                int nr = cr + dr[i];
                int nc = cc + dc[i];
                if(canGo(nr, nc)){
                    visitedGrid[nr][nc] = 2;
                    visited[nr][nc] = true;
                    q.add(new int[]{nr, nc});
                }
            }
        }
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < n && c >= 0 && c < n;
    }

    public static boolean canGo(int r, int c) {
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
        visited = new boolean[n][n];
        visitedGrid = new int[n][n];

        for(int i = 0; i < n; i++){
            int[] temp = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            grid[i] = temp;
            visitedGrid[i] = temp;
        }

        coordinates = new int[k][2];
        for(int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            // 인덱스 맞추기 위해 -1 처리
            coordinates[i] = new int[]{r-1, c-1};
        }
    }
}
