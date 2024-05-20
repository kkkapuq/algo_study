package codetree.intermidiate_low.backtracking.step_3.collect_coins_easy;

import java.util.*;
import java.io.*;

public class Main {
    public static int N;
    public static String[][] board;
    public static int answer = Integer.MAX_VALUE;
    public static int[] dr = new int[]{-1, 1, 0, 0};
    public static int[] dc = new int[]{0, 0, -1, 1};
    public static int r, c;

    public static void main(String[] args) throws IOException {
        input();
        findRoute(r, c, 0, 0, -1);

        answer = answer == Integer.MAX_VALUE ? -1 : answer;
        System.out.print(answer);
    }

    public static boolean inRange(int nr, int nc){
        return 0 <= nr && nr < N && 0 <= nc && nc < N;
    }

    // 매개변수 : (현재 r, 현재 c, 마지막으로 먹은 코인, 걸어온 거리)
    public static void findRoute(int curR, int curC, int curCoin, int len, int dir){
        // 끝지점에 도달했을 때, 코인을 최소 3개 먹은 경우만 return 처리해준다.
        if(board[curR][curC].equals("E")){
            if(curCoin >= 3){
                answer = Math.min(answer, len);
                return;
            }
        }

        // 만약 현재 도달한 곳이 다음 숫자 코인이라면 현재 코인을 갱신해준다.
        if(!board[curR][curC].equals("S") &&
                !board[curR][curC].equals("E") &&
                !board[curR][curC].equals(".") &&
                Integer.parseInt(board[curR][curC]) > curCoin){
            curCoin = Integer.parseInt(board[curR][curC]);
        }

        // 만약 현재 도달한 곳이 다음 숫자 코인이 아니라면 굳이 탐색할 필요가 없음, return.
        if(!board[curR][curC].equals("S") &&
                !board[curR][curC].equals("E") &&
                !board[curR][curC].equals(".") &&
                Integer.parseInt(board[curR][curC]) < curCoin){
            return;
        }

        // 사방을 탐색하며 다음 코인을 찾는다.
        for(int i = 0; i < 4; i++){
            int nr = curR + dr[i];
            int nc = curC + dc[i];

            // 다음 행선지가 범위 내에 있고, 이전에 방문한 곳이 아니라면 탐색을 진행한다.
            if(inRange(nr, nc) && !checkWentRoute(dir, i)) {
                findRoute(nr, nc, curCoin, len+1, i);
            }
        }
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

        board = new String[N][N];

        for(int i = 0; i < N; i++){
            String[] temp = Arrays.stream(br.readLine().split(""))
                    .toArray(String[]::new);
            board[i] = temp;
        }

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(board[i][j].equals("S")){
                    r = i;
                    c = j;
                    break;
                }
            }
        }
    }
}