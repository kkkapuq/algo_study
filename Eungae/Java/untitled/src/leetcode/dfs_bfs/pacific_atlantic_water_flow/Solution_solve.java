package leetcode.dfs_bfs.pacific_atlantic_water_flow;

import java.util.*;

/**
 * 문제 : Pacific Atlantic Water Flow
 * 난이도 : Medium
 * 소요시간 : 100분
 */
class Solution_solve {
    static Queue<int[]> pq;
    static Queue<int[]> aq;
    static List<List<Integer>> list;
    static int M;
    static int N;

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};


    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        pq = new LinkedList<>();
        aq = new LinkedList<>();
        list = new ArrayList<>();
        M = heights.length;
        N = heights[0].length;

        // 양 옆 테두리 pq, aq에 넣어주기
        for(int i = 0; i < M; i++){
            pq.add(new int[]{i, 0});
            aq.add(new int[]{i, N-1});
        }

        // 태평양 행 넣어주기 (위 테두리)
        for(int i = 1; i < N; i++){
            pq.add(new int[]{0, i});
        }

        // 대서양 행 넣어주기 (아래 테두리)
        for(int i = 0; i < N-1; i++){
            aq.add(new int[]{M-1, i});
        }

        int pacificVisited[][] = pacificBfs(heights);
        int atlanticVisited[][] = atlanticBfs(heights);

        for(int i = 0; i < M; i++){
            for(int j = 0; j < N; j++){
                if(pacificVisited[i][j] == 1 && atlanticVisited[i][j] == 1){
                    List<Integer> temp = List.of(i, j);
                    list.add(temp);
                }
            }
        }

        return list;

    }

    public int[][] pacificBfs(int[][] heights){
        int[][] visited = new int[M][N];

        while(!pq.isEmpty()){
            int[] temp = pq.poll();
            int r = temp[0];
            int c = temp[1];
            visited[r][c] = 1;

            for(int i = 0; i < 4; i++){
                int nr = r + dr[i];
                int nc = c + dc[i];
                if(nr < 0 || nr >= M || nc < 0 || nc >= N || visited[nr][nc] == 1){
                    continue;
                }
                if(heights[nr][nc] >= heights[r][c]){
                    pq.add(new int[]{nr, nc});
                }
            }
        }
        return visited;
    }

    public int[][] atlanticBfs(int[][] heights){
        int[][] visited = new int[M][N];
        while(!aq.isEmpty()){
            int[] temp = aq.poll();
            int r = temp[0];
            int c = temp[1];
            visited[r][c] = 1;

            for(int i = 0; i < 4; i++){
                int nr = r + dr[i];
                int nc = c + dc[i];
                if(nr < 0 || nr >= M || nc < 0 || nc >= N || visited[nr][nc] == 1){
                    continue;
                }
                if(heights[nr][nc] >= heights[r][c]){
                    aq.add(new int[]{nr, nc});
                }
            }
        }
        return visited;
    }

    public static void main(String[] args) {
        Solution_solve solution = new Solution_solve();
        int[][] heights = {
                {1, 2, 2, 3, 5},
                {3, 2, 3, 4, 4},
                {2, 4, 5, 3, 1},
                {6, 7, 1, 4, 5},
                {5, 1, 1, 2, 4}
        };

        System.out.println(solution.pacificAtlantic(heights));
    }
}