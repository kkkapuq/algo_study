package programmers.dfs_bfs.level_2_250136;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution2 {
    public int[] dr = new int[]{-1, 1, 0, 0};
    public int[] dc = new int[]{0, 0, -1, 1};

    public int n, m;
    public Set<Integer> candidates = new HashSet<>();
    public int solution(int[][] land) {
        int answer = 0;

        n = land.length;
        m = land[0].length;

        int[] oils = new int[m];

        // 열 하나씩 뚫으면서 dfs를 수행해나간다.
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                // 석유를 발견하면 dfs 수행
                if(land[i][j] == 1){
                    int amount = dfs(j, i, land, 1);
                    candidates.add(j);
                    for(int candidate : candidates){
                        oils[candidate] += amount;
                    }
                }
            }
        }
        answer = Arrays.stream(oils).max().getAsInt();

        return answer;
    }

    public int dfs(int r, int c, int[][] land, int cnt) {
        // 방문처리
        land[r][c] = 0;

        for(int i = 0; i < 4; i++){
            int nr = r + dr[i];
            int nc = c + dc[i];
            if(nr < 0 || nr >= n || nc < 0 || nc >= m){
                continue;
            }
            if(land[nr][nc] == 1){
                cnt = dfs(nr, nc, land, cnt+1);
            }
        }
        return cnt;
    }

    public static void main(String[] args) {
        Solution2 solution = new Solution2();
        int[][] param = new int[][]{{0, 0, 0, 1, 1, 1, 0, 0}, {0, 0, 0, 0, 1, 1, 0, 0}, {1, 1, 0, 0, 0, 1, 1, 0}, {1, 1, 1, 0, 0, 0, 0, 0}, {1, 1, 1, 0, 0, 0, 1, 1}};
        System.out.println(solution.solution(param));
    }
}