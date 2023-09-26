package backjoon.Implementation.Silver_3_1913;

import java.io.*;

/**
 * 문제 : 달팽이
 * 링크 : https://www.acmicpc.net/problem/1913
 * 소요시간 : 58분
 */
public class Silver_III_1913 {
    public static boolean inRange(int x, int y, int n){
        return x >= 0 && x < n && y >= 0 && y < n;
    }

    public static boolean end(int x, int y, int n){
        return !inRange(x, y, n);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int target = Integer.parseInt(br.readLine());
        int xx = 0, yy = 0;
        int[][] arr = new int[n][n];

        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};

        // 현재 위치 초기화
        int x = n/2, y = n/2;
        int cdir = 0;
        int moveNum = 1;
        int cnt = 1;

        while(!end(x, y, n)){
            for(int i = 0; i < moveNum; i++){
                arr[x][y] = cnt;
                cnt++;

                x += dx[cdir];
                y += dy[cdir];
                if(end(x, y, n))
                    break;
            }
            cdir = (cdir + 1) % 4;
            if(cdir == 0 || cdir == 2)
                moveNum++;
        }

        // 표 출력
        for(int i = 0; i < n; i++){
            StringBuilder sb = new StringBuilder();
            for(int j = 0; j < n; j++){
                sb.append(arr[i][j] + " ");
                if(arr[i][j] == target){
                    xx = i+1;
                    yy = j+1;
                }

            }
            sb.append("\n");
            bw.write(sb.toString());
        }

        bw.write(xx + " " + yy);

        bw.close();
        br.close();
    }
}
