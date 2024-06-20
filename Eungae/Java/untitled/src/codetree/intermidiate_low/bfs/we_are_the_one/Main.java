package codetree.intermidiate_low.bfs.we_are_the_one;
import java.util.*;
import java.io.*;

/**
 * 문제 : 우리는 하나
 * 소요 시간 : 90분
 * 링크 : https://www.codetree.ai/missions/2/problems/we-are-the-one/description
 */
public class Main {
    public static int n, k, u, d;

    public static int[][] grid;
    public static boolean[][] visited;
    public static List<int[]> cities = new ArrayList<>();
    public static List<int[]> selectedCities = new ArrayList<>();

    public static int[] dr = new int[]{-1, 1, 0, 0};
    public static int[] dc = new int[]{0, 0, -1, 1};

    public static int answer = 0;

    public static void main(String[] args) throws IOException{
        input();
        findMax(0, 0);
        System.out.print(answer);
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < n && c >= 0 && c < n;
    }

    public static boolean heightPossible(int r, int c, int nr, int nc) {
        int gap = Math.abs(grid[r][c] - grid[nr][nc]);
        return gap >= u && gap <= d ? true : false;
    }

    public static boolean canGo(int r, int c, int nr, int nc) {
        if(!inRange(nr, nc) || !heightPossible(r, c, nr, nc) || visited[nr][nc])
            return false;
        return true;
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        u = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());

        grid = new int[n][n];
        visited = new boolean[n][n];

        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < n; j++){
                grid[i][j] = Integer.parseInt(st.nextToken());
                cities.add(new int[]{i, j});
            }
        }
    }

    public static void bfs(int[] city) {
        Deque<int[]> q = new ArrayDeque<>();
        int r = city[0];
        int c = city[1];
        q.add(new int[]{r, c});

        visited[r][c] = true;

        while(!q.isEmpty()) {
            int[] temp = q.poll();
            int cr = temp[0];
            int cc = temp[1];

            for(int i = 0; i < 4; i++){
                int nr = cr + dr[i];
                int nc = cc + dc[i];
                if(canGo(cr, cc, nr, nc)){
                    visited[nr][nc] = true;
                    q.add(new int[]{nr, nc});
                }
            }
        }
    }

    public static int calc() {
        visited = new boolean[n][n];
        int cnt = 0;

        for(int[] city : selectedCities) {
            bfs(city);
        }

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(visited[i][j]){
                    cnt++;
                }
            }
        }

        return cnt;
    }

    public static void findMax(int idx, int cnt) {
        if(cnt > k)
            return;

        if(idx == n*n) {
            if(cnt == k) {
                answer = Math.max(answer, calc());
            }
            return;
        }

        selectedCities.add(cities.get(idx));
        findMax(idx+1, cnt+1);
        selectedCities.remove(selectedCities.size()-1);
        findMax(idx+1, cnt);
    }
}