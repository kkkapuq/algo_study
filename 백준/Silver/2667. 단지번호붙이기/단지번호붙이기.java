import java.util.*;
import java.io.*;

class Main {
    static int[][] graph;
    static List<Integer> list = new ArrayList<>();
    static int[] dr = {1, -1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        graph = new int[N][N];

        for(int i = 0; i < N; i++){
            String str = br.readLine();
            for(int j = 0; j < N; j++){
                graph[i][j] = Character.getNumericValue(str.charAt(j));
            }
        }

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(graph[i][j] == 1){
                    list.add(dfs(i, j, 1));
                }
            }
        }

        sb.append(list.size());
        sb.append("\n");
        Collections.sort(list);
        for(int num : list){
            sb.append(num);
            sb.append("\n");
        }
        System.out.println(sb.toString());
    }

    public static int dfs(int r, int c, int cnt){
        graph[r][c] = 0;
        if(r < 0 || r >= N || c < 0 || c >= N)
            return cnt;

        for(int i = 0; i < 4; i++){
            int nr = r + dr[i];
            int nc = c + dc[i];
            // 범위 밖은 탐색 제외
            if(nr < 0 || nr >= N || nc < 0 || nc >= N)
                continue;
            if(graph[nr][nc] == 1)
                cnt = dfs(nr, nc, cnt+1);
        }

        return cnt;
    }
}