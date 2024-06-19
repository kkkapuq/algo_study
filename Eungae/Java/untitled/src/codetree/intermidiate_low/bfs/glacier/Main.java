package codetree.intermidiate_low.bfs.glacier;

import java.util.*;
import java.io.*;

/**
 * 문제 : 빙하
 * 소요 시간 : 86분
 * 링크 : https://www.codetree.ai/missions/2/problems/glacier/description
 */
public class Main {
    public static int n, m;

    public static int[][] grid;
    public static boolean[][] visited;

    public static int time = 0;
    public static int meltedIceSize = 0;

    public static int[] dr = new int[]{-1, 1, 0, 0};
    public static int[] dc = new int[]{0, 0, -1, 1};

    public static void main(String[] args) throws IOException{
        input();
        while(isIceExists()){
            time++;
            List<int[]> waterPos = getWaterPos();
            meltedIceSize = calcMeltingIces();
            meltingIce(waterPos);
        }
        System.out.print(time + " " + meltedIceSize);
    }

    public static boolean isIceExists() {
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(grid[i][j] == 1)
                    return true;
            }
        }
        return false;
    }

    public static List<int[]> getWaterPos() {
        visited = new boolean[n][m];
        visited[0][0] = true;
        Deque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{0, 0});

        List<int[]> waterPos = new ArrayList<>();
        waterPos.add(new int[]{0, 0});

        while(!q.isEmpty()) {
            int[] temp = q.poll();
            int r = temp[0];
            int c = temp[1];

            for(int i = 0; i < 4; i++){
                int nr = r + dr[i];
                int nc = c + dc[i];

                if(canGo(nr, nc)) {
                    visited[nr][nc] = true;
                    waterPos.add(new int[]{nr, nc});
                    q.add(new int[]{nr, nc});
                }
            }
        }
        return waterPos;
    }

    public static int calcMeltingIces() {
        int cnt = 0;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(grid[i][j] == 1)
                    cnt++;
            }
        }
        return cnt;
    }

    public static void meltingIce(List<int[]> waterPos) {
        for(int[] pos : waterPos) {
            int r = pos[0];
            int c = pos[1];

            for(int i = 0; i < 4; i++){
                int nr = r + dr[i];
                int nc = c + dc[i];

                if(inRange(nr, nc) && grid[nr][nc] == 1){
                    grid[nr][nc] = 0;
                }
            }
        }
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < n && c >= 0 && c < m;
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
        m = Integer.parseInt(st.nextToken());

        grid = new int[n][m];
        visited = new boolean[n][m];

        for(int i = 0; i < n; i++){
            grid[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        }
    }
}