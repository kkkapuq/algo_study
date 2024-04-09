package leetcode.dfs_bfs.pacific_atlantic_water_flow;

import java.util.*;

/**
 * 문제 : Pacific Atlantic Water Flow
 * 난이도 : Medium
 * 소요시간 : 100분
 */
class Solution {
    static Queue<int[]> pq;
    static Queue<int[]> aq;
    static List<List<Integer>> list = new ArrayList<>();
    static int M;
    static int N;

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};


    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        M = heights.length;
        N = heights[0].length;

        for(int i = 0; i < M; i++){
            for(int j = 0; j < N; j++){
                pq = new LinkedList<>();
                aq = new LinkedList<>();
                int[][] copy = heights.clone();
                if(pacificBfs(i, j, copy) && atlanticBfs(i, j, copy)){
                    List<Integer> temp = new ArrayList<>();
                    temp.add(i);
                    temp.add(j);
                    list.add(temp);
                }
            }
        }

        return list;

    }

    public boolean pacificBfs(int r, int c, int[][] heights){
        pq.add(new int[]{r, c});

        while(!pq.isEmpty()){
            int[] temp = pq.poll();
            r = temp[0];
            c = temp[1];

            // 태평양과 인접한 칸이라면 true return
            if((r == 0 && c >= 0 && c < N) || (c == 0 && r >= 0 && r < M)){
                return true;
            }

            for(int i = 0; i < 4; i++){
                int nr = r + dr[i];
                int nc = c + dc[i];
                if(nr < 0 || nr >= M || nc < 0 || nc >= N){
                    continue;
                }
                if(heights[nr][nc] <= heights[r][c]){
                    pq.add(new int[]{nr, nc});
                }
            }
        }
        return false;
    }

    public boolean atlanticBfs(int r, int c, int[][] heights){
        aq.add(new int[]{r, c});
        while(!aq.isEmpty()){
            int[] temp = aq.poll();
            r = temp[0];
            c = temp[1];

            // 대서양과 인접한 칸이라면 true return
            if((r == M-1 && c >= 0 && c < N) || (c == N-1 && r >= 0 && r < M)){
                return true;
            }

            for(int i = 0; i < 4; i++){
                int nr = r + dr[i];
                int nc = c + dc[i];
                if(nr < 0 || nr >= M || nc < 0 || nc >= N){
                    continue;
                }
                if(heights[nr][nc] <= heights[r][c]){
                    aq.add(new int[]{nr, nc});
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
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