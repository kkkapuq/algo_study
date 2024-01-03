import java.io.*;
import java.util.*;

class Main {
    static List<List<Integer>> graph;
    static List<Boolean> visited = new ArrayList<>();
    static int N;
    static int M;
    static int V;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());

        graph = new ArrayList<List<Integer>>();
        for(int i = 0; i < N+1; i++){
            graph.add(new ArrayList<>());
            visited.add(false);
        }

        for(int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph.get(a).add(b);
            graph.get(b).add(a);
            Collections.sort(graph.get(a));
            Collections.sort(graph.get(b));
        }

        dfs(V);
        System.out.println(sb.toString());

        // dfs 에서 사용 후 초기화
        sb = new StringBuilder();
        visited = new ArrayList<>();
        for(int i = 0; i < N+1; i++){
            visited.add(false);
        }

        bfs(V);
        System.out.println(sb.toString());
    }

    public static void dfs(int v){
        visited.set(v, true);
        sb.append(Integer.toString(v) + " ");
        for(int i = 0; i < graph.get(v).size(); i++){
            int temp = graph.get(v).get(i);
            if(!visited.get(temp)){
                dfs(temp);
            }
        }
    }

    public static void bfs(int v){
        visited.set(v, true);
        Queue<Integer> q = new LinkedList<>();

        q.add(v);
        while(!q.isEmpty()){
            int temp = q.poll();
            sb.append(temp + " ");
            for (int i = 0; i < graph.get(temp).size(); i++) {
                int t = graph.get(temp).get(i);
                if(!visited.get(t)){
                    visited.set(t, true);
                    q.add(t);
                }
            }
        }

    }
}