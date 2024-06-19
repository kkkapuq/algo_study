package codetree.intermidiate_low.bfs.clear_stones_well;

import java.io.*;
import java.util.*;

/**
 * 문제 : 돌 잘 치우기
 * 소요시간 : 45분
 * 링크 : https://www.codetree.ai/missions/2/problems/clear-stones-well/description
 */
public class Main {
    public static int n, m, k;
    public static int sr, sc;
    public static int[][] grid;
    public static boolean[][] visited;
    public static int[][] coordinates;
    public static List<int[]> selectedStones = new ArrayList<>();
    public static List<int[]> stonePos = new ArrayList<>();

    public static int[] dr = {-1, 1, 0, 0};
    public static int[] dc = {0, 0, -1, 1};

    public static int answer = 0;

    public static void main(String[] args) throws IOException {
        input();
        findMax(0, 0);
        System.out.print(answer);
    }

    public static int calc() {
        // 선택된 돌들을 0으로 치환
        for (int i = 0; i < m; i++) {
            int r = selectedStones.get(i)[0];
            int c = selectedStones.get(i)[1];

            grid[r][c] = 0;
        }

        // bfs 하기 전에 visited 초기화
        visited = new boolean[n][n];

        // 시작점들 bfs 수행
        for (int i = 0; i < k; i++) {
            int r = coordinates[i][0];
            int c = coordinates[i][1];

            bfs(r, c);
        }

        // 선택된 돌들을 1로 치환 (원복)
        for (int i = 0; i < m; i++) {
            int r = selectedStones.get(i)[0];
            int c = selectedStones.get(i)[1];

            grid[r][c] = 1;
        }

        // 방문한 곳 cnt해주기
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j])
                    cnt++;
            }
        }

        return cnt;
    }

    public static void findMax(int idx, int cnt) {
        if(idx == stonePos.size()) {
            if(cnt == m){
                answer = Math.max(answer, calc());
            }
            return;
        }

        selectedStones.add(stonePos.get(idx));
        findMax(idx+1, cnt+1);
        selectedStones.remove(selectedStones.size()-1);
        findMax(idx+1, cnt);
    }

    public static void bfs(int r, int c) {
        Deque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{r, c});
        visited[r][c] = true;

        while (!q.isEmpty()) {
            int[] temp = q.poll();
            int cr = temp[0];
            int cc = temp[1];

            for (int i = 0; i < 4; i++) {
                int nr = cr + dr[i];
                int nc = cc + dc[i];
                if (canGo(nr, nc)) {
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
        if (!inRange(r, c) || grid[r][c] == 1 || visited[r][c])
            return false;
        return true;
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        grid = new int[n][n];
        visited = new boolean[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                grid[i][j] = Integer.parseInt(st.nextToken());
                if (grid[i][j] == 1)
                    stonePos.add(new int[]{i, j});
            }
        }

        coordinates = new int[k][2];
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            sr = Integer.parseInt(st.nextToken()) - 1;
            sc = Integer.parseInt(st.nextToken()) - 1;

            coordinates[i] = new int[]{sr, sc};
        }
    }
}

