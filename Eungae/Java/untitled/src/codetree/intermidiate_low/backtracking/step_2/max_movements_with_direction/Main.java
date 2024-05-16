package codetree.intermidiate_low.backtracking.step_2.max_movements_with_direction;

import java.util.*;
import java.io.*;

/**
 * 문제 : 방향에 맞춰 최대로 움직이기
 * 소요 시간 : 41분
 * 링크 : https://www.codetree.ai/missions/2/problems/max-movements-with-direction/description
 */
import java.util.*;
import java.io.*;

public class Main {

    public static int N;
    public static int[][] board;
    public static int[][] dirBoard;
    public static int[] dr = new int[]{0, -1, -1, 0, 1, 1, 1, 0, -1};
    public static int[] dc = new int[]{0, 0, 1, 1, 1, 0, -1, -1, -1};
    public static int[] position = new int[]{0, 0};
    public static int answer;

    public static void main(String[] args) throws IOException  {
        input();
        recursion(0);
        System.out.println(answer);
    }

    public static boolean inRange(int x, int y){
        return 0 <= x && x < N && 0 <= y && y < N;
    }

    public static boolean canGo(int x, int y, int prevNum){
        return inRange(x, y) && board[x][y] > prevNum;
    }

    public static void recursion(int cnt) {
        answer = Math.max(answer, cnt);

        int r = position[0];
        int c = position[1];
        int dir = dirBoard[r][c];

        for(int i = 0; i < N; i++){
            int nr = r + dr[dir] * i;
            int nc = c + dc[dir] * i;
            if(canGo(nr, nc, board[r][c])){
                position[0] = nr;
                position[1] = nc;
                recursion(cnt+1);
            }
        }
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        // 숫자가 적힌 보드 생성
        board = new int[N][N];

        for(int i = 0; i < N; i++){
            int[] temp = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
            board[i] = temp;
        }

        // 방향 보드 생성
        dirBoard = new int[N][N];
        for(int i = 0; i < N; i++){
            int[] temp = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
            dirBoard[i] = temp;
        }

        // 현재 내 위치 설정
        int[] temp = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        position = temp;

        // 인덱스 계산을 위한 마이너스 연산
        temp[0]--;
        temp[1]--;
    }
}