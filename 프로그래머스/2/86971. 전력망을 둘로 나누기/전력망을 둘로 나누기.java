import java.util.*;

class Solution {
    static List<Integer>[] graph;
    static int min;
    
    public int solution(int n, int[][] wires) {
        graph = new ArrayList[n+1];
        min = Integer.MAX_VALUE;
        
        for(int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }
        
        for(int i = 0; i < wires.length; i++){
            int a = wires[i][0];
            int b = wires[i][1];
            graph[a].add(b);
            graph[b].add(a);
        }
        
        for(int i = 0; i < wires.length; i++) {
            int a = wires[i][0];
            int b = wires[i][1];
            boolean[] visited = new boolean[n+1];
            
            graph[a].remove(Integer.valueOf(b));
            graph[b].remove(Integer.valueOf(a));
            
            int cnt = dfs(1, visited);
            int diff = Math.abs(cnt - (n - cnt));
            min = Math.min(min, diff);
            
            graph[a].add(b);
            graph[b].add(a);
        }
        return min;
    }
    
    public int dfs(int v, boolean[] visited){
        visited[v] = true;
        int cnt = 1;
        
        for(int next : graph[v]){
            if(!visited[next]){
                cnt += dfs(next, visited);
            }
        }
        return cnt;
    }
}