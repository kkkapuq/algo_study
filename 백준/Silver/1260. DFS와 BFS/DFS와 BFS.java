import java.util.*;
import java.io.*;

class Main {
    public static int n, m, v;
    public static List<List<Integer>> graph = new ArrayList<>();
    public static boolean[] visited;
    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        input();
        dfs(v);
        System.out.println(sb.toString());
        init();
        bfs(v);
        System.out.println(sb.toString());
    }

    public static void dfs(int start) {
        visited[start] = true;
        sb.append(start + " ");
        for(int i = 0; i < graph.get(start).size(); i++) {
            int temp = graph.get(start).get(i);
            if(!visited[temp])
                dfs(temp);
        }
    }

    public static void init() {
        visited = new boolean[n+1];
        sb = new StringBuilder();
    }

    public static void bfs(int start) {
        visited[start] = true;
        Queue<Integer> deque = new LinkedList<>();
        deque.add(start);

        while(!deque.isEmpty()) {
            int temp = deque.poll();
            sb.append(temp + " ");
            for(int i = 0; i < graph.get(temp).size(); i++){
                int t = graph.get(temp).get(i);
                if (!visited[t]) {
                    visited[t] = true;
                    deque.add(t);
                }
            }
        }
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        v = Integer.parseInt(st.nextToken());

        visited = new boolean[n+1];

        for(int i = 0; i < n+1; i++){
            graph.add(new ArrayList<>());
            visited[i] = false;
        }

        for(int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph.get(a).add(b);
            graph.get(b).add(a);
            Collections.sort(graph.get(a));
            Collections.sort(graph.get(b));
        }
    }
}