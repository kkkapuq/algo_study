import java.util.*;

class Solution {
    static int[] dr = new int[]{-1, 1, 0, 0};
    static int[] dc = new int[]{0, 0, -1, 1};
    static Deque<int[]> deque;
    
    public int solution(int[][] maps) {
        deque = new ArrayDeque<>();
        int n = maps.length;
        int m = maps[0].length;
        deque.push(new int[]{n-1, m-1});
        
        while(!deque.isEmpty()){
            int[] position = deque.poll();
            int r = position[0];
            int c = position[1];
            
            for(int i = 0; i < 4; i++){
                int nr = dr[i] + r;
                int nc = dc[i] + c;
                
                if(nr < 0 || nc < 0 || nr >= n || nc >= m) {
                    continue;
                }
                
                if(maps[nr][nc] == 0){
                    continue;
                }
                
                if(maps[nr][nc] == 1){
                    deque.offer(new int[]{nr, nc});
                    maps[nr][nc] = maps[r][c] + 1;
                }
            }
        }
        int answer = maps[0][0];
        
        return answer == 1 ? -1 : answer;
    }
}