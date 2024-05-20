package codetree.intermidiate_low.backtracking.step_3.collect_coins_easy;

import java.util.*;
import java.io.*;

class Pair {
    int x, y;

    public Pair(int x, int y){
        this.x = x;
        this.y = y;
    }
}

public class Solution {
    public static int N;
    public static int M = 3;
    public static final int MAX_N = 20;
    public static char[][] grid = new char[MAX_N][MAX_N];
    public static int answer = Integer.MAX_VALUE;
    public static final int COIN_NUM = 9;

    public static ArrayList<Pair> coinPos = new ArrayList<>();
    public static ArrayList<Pair> selectedPos = new ArrayList<>();

    public static Pair startPos;
    public static Pair endPos;

    public static int dist(Pair a, Pair b) {
        int ax = a.x;
        int ay = a.y;

        int bx = b.x;
        int by = b.y;

        return Math.abs(ax - bx) + Math.abs(ay - by);
    }

    public static void main(String[] args) throws IOException {
        input();
        findMinMoves(0, 0);

        answer = answer == Integer.MAX_VALUE ? -1 : answer;
        System.out.print(answer);
    }

    public static int calc() {
        int numMoves = dist(startPos, selectedPos.get(0));
        for(int i = 0; i < M-1; i++){
            numMoves += dist(selectedPos.get(i), selectedPos.get(i+1));
        }
        numMoves += dist(selectedPos.get(M-1), endPos);

        return numMoves;
    }

    public static void findMinMoves(int currIdx, int cnt){
        if(cnt == M){
            answer = Math.min(answer, calc());
            return;
        }

        if(currIdx == (int) coinPos.size())
            return;

        findMinMoves(currIdx+1, cnt);

        selectedPos.add(coinPos.get(currIdx));
        findMinMoves(currIdx+1, cnt+1);
        selectedPos.remove(selectedPos.size() - 1);
    }

    // 왔다갔다 무한루프를 방지하기 위한 함수
    private static boolean checkWentRoute(int dir, int i) {
        if(dir == 0 && i == 1) return true;
        if(dir == 1 && i == 0) return true;
        if(dir == 2 && i == 3) return true;
        if(dir == 3 && i == 2) return true;
        return false;
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        for(int i = 0; i < N; i++){
            String str = br.readLine();
            for(int j = 0; j < N; j++){
                grid[i][j] = str.charAt(j);
                if(grid[i][j] == 'S')
                    startPos = new Pair(i, j);
                if(grid[i][j] == 'E')
                    endPos = new Pair(i, j);
            }
        }

        // 동전을 오름차순으로 각 위치를 집어넣는다.
        // 이후에 증가하는 순서대로 방문하기 위함
        for(int num = 1; num <= COIN_NUM; num++){
            for(int i = 0; i < N; i++){
                for(int j = 0; j < N; j++){
                    if(grid[i][j] == num + '0')
                        coinPos.add(new Pair(i, j));
                }
            }
        }
    }
}
