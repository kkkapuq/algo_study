package codetree.intermidiate_low.bfs.move_to_max_k_times;

import java.io.*;
import java.util.*;

/**
 * 문제 : K번 최댓값으로 이동하기
 * 소요 시간 : 70분
 * 링크 : https://www.codetree.ai/missions/2/problems/move-to-max-k-times/description
 */
public class Main {
    public static int n, k;
    public static int sr, sc;
    public static int[][] grid;
    public static boolean[][] visited;
    public static List<int[]> list = new ArrayList<>();

    public static int[] dr = {-1, 1, 0, 0};
    public static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException{
        input();
        for(int i = 0; i < k; i++){
            visited = new boolean[n][n];
            list = new ArrayList<>();
            if(!bfs(sr, sc, grid[sr][sc]))
                break;

            // bfs가 1회 끝나고 나면, 정렬을 통해 시작위치를 재설정한다.
            // 값 내림차순, 행 오름차순, 열 오름차순 으로 진행
            Collections.sort(list, (a, b) -> {
                if(a[0] != b[0]) {
                    return Integer.compare(b[0], a[0]);
                } else if(a[1] != b[1]) {
                    return Integer.compare(a[1], b[1]);
                } else {
                    return Integer.compare(a[2], b[2]);
                }
            });

            // for(int[] arr : list) {
            //     System.out.println(Arrays.toString(arr));
            // }
            sr = list.get(0)[1];
            sc = list.get(0)[2];
            // System.out.println("재설정된 시작 좌표 : " + sr + " " + sc);
        }
        System.out.print(sr+1);
        System.out.print(" ");
        System.out.print(sc+1);
    }

    public static boolean bfs(int r, int c, int cur) {
        Deque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{r, c});
        visited[r][c] = true;

        // 이동할 수 있는지 없는지 판단하는 플래그 값
        boolean flag = false;

        while(!q.isEmpty()) {
            int[] temp = q.poll();
            int cr = temp[0];
            int cc = temp[1];

            for(int i = 0; i < 4; i++){
                int nr = cr + dr[i];
                int nc = cc + dc[i];
                if(canGo(nr, nc, cur)){
                    flag = true;
                    visited[nr][nc] = true;

                    // bfs로 갈 수 있는 곳들을 모두 모으기 위한 리스트에 더해줌
                    // [값, 행, 렬] 로 들어감
                    // System.out.println("bfs에서 들어갈 값과 좌표" + grid[nr][nc] + ", " + nr +", " + nc );
                    list.add(new int[]{grid[nr][nc], nr, nc});
                    q.add(new int[]{nr, nc});
                }
            }
        }
        return flag;
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < n && c >= 0 && c < n;
    }

    public static boolean canGo(int r, int c, int cur) {
        if(!inRange(r, c) || grid[r][c] >= cur || visited[r][c])
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

        for(int i = 0; i < n; i++){
            int[] temp = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            grid[i] = temp;
        }

        st = new StringTokenizer(br.readLine());
        sr = Integer.parseInt(st.nextToken()) - 1;
        sc = Integer.parseInt(st.nextToken()) - 1;
    }
}