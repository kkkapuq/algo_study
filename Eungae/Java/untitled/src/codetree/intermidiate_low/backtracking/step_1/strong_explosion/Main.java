package codetree.intermidiate_low.backtracking.step_1.strong_explosion;

import java.util.*;
import java.io.*;

/**
 * 문제 : 강력한 폭발
 * 소요시간 : 1시간 4분
 * 링크 : https://www.codetree.ai/missions/2/problems/strong-explosion/description
 */
public class Main {
    public static int N;
    public static int K = 0;
    public static int[][] board;
    public static int[][] copiedBoard;
    public static List<Integer> bombs = new ArrayList<>();
    public static List<int[]> coordinates = new ArrayList<>();
    public static int answer = -1;

    public static void main(String[] args) throws IOException {
        input();
        setBombs(0);
        System.out.print(answer);
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        board = new int[N][N];

        // 맵 입력
        for(int i = 0; i < N; i++){
            int[] temp = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
            board[i] = temp;
        }

        // 좌표 저장
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(board[i][j] == 1) {
                    coordinates.add(new int[]{i, j});
                    // 폭탄을 놓을 수 있는 공간의 수 갱신
                    K++;
                }
            }
        }
    }

    public static void calculate() {
        int temp = 0;
        copiedBoard = new int[N][N];

        // 계산에 사용될 보드 복사
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                copiedBoard[i][j] = board[i][j];
            }
        }

        for(int i = 0; i < coordinates.size(); i++){
            // bombs와 coordinates는 1:1 대응을 이룬다.
            // 즉, coordinates[i] 의 폭탄번호는 bombs[i]이다. 번호에 맞게 계산해주자.
            if(bombs.get(i) == 1){
                bombOne(coordinates.get(i));
            } else if(bombs.get(i) == 2){
                bombTwo(coordinates.get(i));
            } else {
                bombThree(coordinates.get(i));
            }
        }

        // 정답 갱신
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(copiedBoard[i][j] == 9)
                    temp += 1;
            }
        }
        answer = Math.max(answer, temp);
    }

    // 폭탄별로 폭발 범위가 다르므로, 따로 계산해서 폭발시키는 범위를 copiedBoard에 갱신해준다.
    public static void bombOne(int[] position){
        int[] dr = new int[]{-2, -1, 1, 2};
        int[] dc = new int[]{0, 0, 0, 0};
        int r = position[0];
        int c = position[1];

        // 폭탄을 놓는 자리 폭발처리
        copiedBoard[r][c] = 9;

        for(int i = 0; i < 4; i++){
            int nr = r + dr[i];
            int nc = c + dc[i];

            if(nr < 0 || nr >= N || nc < 0 || nc >= N)
                continue;

            copiedBoard[nr][nc] = 9;
        }
    }

    public static void bombTwo(int[] position){
        int[] dr = new int[]{-1, 1, 0, 0};
        int[] dc = new int[]{0, 0, -1, 1};
        int r = position[0];
        int c = position[1];

        // 폭탄을 놓는 자리 폭발처리
        copiedBoard[r][c] = 9;

        for(int i = 0; i < 4; i++){
            int nr = r + dr[i];
            int nc = c + dc[i];

            if(nr < 0 || nr >= N || nc < 0 || nc >= N)
                continue;

            copiedBoard[nr][nc] = 9;
        }
    }

    public static void bombThree(int[] position){
        int[] dr = new int[]{-1, -1, 1, 1};
        int[] dc = new int[]{-1, 1, -1, 1};
        int r = position[0];
        int c = position[1];

        // 폭탄을 놓는 자리 폭발처리
        copiedBoard[r][c] = 9;

        for(int i = 0; i < 4; i++){
            int nr = r + dr[i];
            int nc = c + dc[i];

            if(nr < 0 || nr >= N || nc < 0 || nc >= N)
                continue;
            copiedBoard[nr][nc] = 9;
        }
    }

    public static void setBombs(int num) {
        if(num >= K){
            calculate();
            return;
        }

        for(int i = 1; i < 4; i++){
            bombs.add(i);
            setBombs(num+1);
            bombs.remove(bombs.size()-1);
        }
    }
}
