package codetree.intermidiate_low.dfs.comfort_zone;

import java.util.*;
import java.io.*;

/**
 * 문제 : 안전 지대
 * 소요 시간 : 32분
 * 링크 : https://www.codetree.ai/missions/2/problems/comfort-zone/description
 */
public class Main {
    public static int n, m;
    public static int[][] grid;
    public static int[][] visited;
    public static int[] answer;
    public static int kNum;
    public static int maxNum = 0;
    public static int[] dr = {-1, 1, 0, 0};
    public static int[] dc = {0, 0, -1, 1};

    public static int maxK = 0;
    public static int maxAreas = 0;

    public static void main(String[] args) throws IOException {
        input();
        for(int k = 1; k <= maxNum; k++){
            visited = new int[n][m];
            kNum = 0;
            for(int i = 0; i < n; i++){
                for(int j = 0; j < m; j++){
                    if(canGo(i, j, k)){
                        dfs(i, j, k);
                        kNum++;
                    }
                }
            }
            answer[k] = kNum;
        }
        print();
    }

    public static void print() {
        for(int i = 1; i <= maxNum; i++){
            if(answer[i] > maxAreas){
                maxK = i;
                maxAreas = answer[i];
            }
        }

        System.out.print(maxK + " " + maxAreas);
    }

    public static boolean inRange(int r, int c){
        return r >= 0 && r < n && c >= 0 && c < m;
    }

    public static boolean canGo(int r, int c, int k) {
        if(grid[r][c] <= k){
            return false;
        } else if(visited[r][c] == 1){
            return false;
        }
        return true;
    }

    public static void dfs(int r, int c, int k) {
        visited[r][c] = 1;

        for(int i = 0; i < 4; i++){
            int nr = r + dr[i];
            int nc = c + dc[i];

            if(!inRange(nr, nc) || !canGo(nr, nc, k)){
                continue;
            }
            dfs(nr, nc, k);
        }
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        grid = new int[n][m];
        visited = new int[n][m];

        for(int i = 0; i < n; i++){
            int[] temp = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            int tempMax = Arrays.stream(temp).max().getAsInt();
            maxNum = Math.max(tempMax, maxNum);
            grid[i] = temp;
        }

        answer = new int[maxNum+1];
    }
}