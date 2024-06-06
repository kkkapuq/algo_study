package codetree.intermidiate_low.dfs.graph_traversal;

import java.util.*;
import java.io.*;

/**
 * 문제 : 그래프 탐색
 * 소요 시간 : 10분
 * 링크 : https://www.codetree.ai/missions/2/problems/graph-traversal/description
 */

public class Main {
    public static int n, m;
    public static List<List<Integer>> graph = new ArrayList<>();
    public static boolean[] visited;
    public static int answer = 0;

    public static void main(String[] args) throws IOException {
        input();
        dfs(1);
        System.out.print(answer);
    }

    public static void dfs(int v) {
        visited[v] = true;

        for(int i = 0; i < graph.get(v).size(); i++) {
            int idx = graph.get(v).get(i);
            if(!visited[idx]){
                visited[idx] = true;
                answer++;
                dfs(idx);
            }
        }
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        visited = new boolean[n+1];

        for(int i = 0; i < n+1; i++){
            graph.add(new ArrayList<>());
        }

        for(int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph.get(a).add(b);
            graph.get(b).add(a);
        }
    }
}