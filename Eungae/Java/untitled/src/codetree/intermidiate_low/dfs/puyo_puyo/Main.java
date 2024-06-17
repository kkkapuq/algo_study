package codetree.intermidiate_low.dfs.puyo_puyo;

import java.util.*;
import java.io.*;

/**
 * 문제 : 뿌요뿌요
 * 소요 시간 : 31분
 * 링크 : https://www.codetree.ai/missions/2/problems/puyo-puyo/description
 */
public class Main {
    public static int n;
    public static int[][] grid;
    public static int[][] visited;
    public static int[] answer;
    public static int blocks = 0;
    public static int maxBlocks = 0;
    public static int[] dr = {-1, 1, 0, 0};
    public static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        input();
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(canGo(i, j, grid[i][j])){
                    int explodedBlocks = dfs(i, j, grid[i][j], 1);
                    if(explodedBlocks >= 4) {
                        blocks++;
                    }
                    maxBlocks = Math.max(maxBlocks, explodedBlocks);
                }
            }
        }
        print();
    }

    public static void print() {
        System.out.print(blocks + " " + maxBlocks);
    }

    public static boolean inRange(int r, int c){
        return r >= 0 && r < n && c >= 0 && c < n;
    }

    public static boolean canGo(int r, int c, int k) {
        if(grid[r][c] != k){
            return false;
        } else if(visited[r][c] == 1){
            return false;
        }
        return true;
    }

    public static int dfs(int r, int c, int k, int depth) {
        visited[r][c] = 1;
        for(int i = 0; i < 4; i++){
            int nr = r + dr[i];
            int nc = c + dc[i];

            if(!inRange(nr, nc) || !canGo(nr, nc, k)){
                continue;
            }
            depth = dfs(nr, nc, k, depth+1);
        }
        return depth;
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        grid = new int[n][n];
        visited = new int[n][n];

        for(int i = 0; i < n; i++){
            int[] temp = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
            grid[i] = temp;
        }
    }
}
