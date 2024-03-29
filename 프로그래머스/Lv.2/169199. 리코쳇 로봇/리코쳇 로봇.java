import java.util.*;

class Solution {
    static int[] dr = new int[]{-1, 1, 0, 0};
    static int[] dc = new int[]{0, 0, -1, 1};

    public int solution(String[] board) {
        int answer = -1;

        int n = board.length;
        int m = board[0].length();
        int max = n*m;

        Queue<int[]> q = new LinkedList<>();
        // 거리를 계산하는 2차원배열
        int[][] dist = new int[n][m];

        for(int i = 0; i < n; i++){
            for(int j = 0 ; j < m; j++){
                if(board[i].charAt(j) == 'R'){
                    q.add(new int[]{i, j, 0});
                    dist[i][j] = 0;
                } else {
                    // 거리 초기화
                    dist[i][j] = max;
                }
            }
        }

        while(!q.isEmpty()){
            int[] position = q.poll();
            int r = position[0];
            int c = position[1];
            int d = position[2];

            if(board[r].charAt(c) == 'G')
                return d;

            for(int i = 0; i < 4; i++){
                int nr = r;
                int nc = c;

                if(nr < 0 || nr >= n || nc < 0 || nc >= m || board[nr].charAt(nc) == 'D'){
                    continue;
                }

                // 쭈욱 미끄러지면서 이동 가능한 위치 찾기
                while(nr + dr[i] >= 0 && nr + dr[i] < n &&
                        nc + dc[i] >= 0 && nc + dc[i] < m &&
                        board[nr + dr[i]].charAt(nc + dc[i]) != 'D'){
                    nr += dr[i];
                    nc += dc[i];
                }

                if(dist[nr][nc] > d+1){
                    dist[nr][nc] = d+1;
                    q.add(new int[]{nr, nc, d+1});
                }
            }
        }
        return answer;
    }
}