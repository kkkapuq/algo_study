import java.io.*;
import java.util.*;

public class Main {
    static int[] drdc = {-1, 1};
    static String[][] arr;
    static int N;

    // arr값 바꿔주기
    public static void swap(int i, int j, int ii, int jj) {
        String temp = arr[i][j];
        arr[i][j] = arr[ii][jj];
        arr[ii][jj] = temp;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int answer = 0;
        N = Integer.parseInt(br.readLine());
        arr = new String[N][N];

        for (int i = 0; i < N; i++) {
            char[] temp = br.readLine().toString().toCharArray();
            for (int j = 0; j < temp.length; j++) {
                arr[i][j] = String.valueOf(temp[j]);
            }
        }

        // 가로줄 바꾸기
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N-1; j++) {
                swap(i, j, i, j+1);

                // 가로줄에서 먹을 수 있는 최댓값 + 세로줄에서 먹을 수 있는 최댓값으로 update해가며 비교해준다.
                int tempMax = Math.max(findHorizon(), findVertical());
                answer = Math.max(answer, tempMax);

                // swap한 결과 원상복구
                swap(i, j, i, j+1);
            }
        }

        // 세로줄 바꾸기
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N-1; j++) {
                swap(j, i, j+1, i);

                // 세로줄에서 먹을 수 있는 최댓값 + 세로줄에서 먹을 수 있는 최댓값으로 update해가며 비교해준다.
                int tempMax = Math.max(findHorizon(), findVertical());
                answer = Math.max(answer, tempMax);

                // swap한 결과 원상복구
                swap(j, i, j+1, i);
            }
        }
        System.out.println(answer);

    }

    // 가로줄 탐색
    public static int findHorizon(){
        int maximum = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int temp = 0;
                // 첫 열 예외처리
                if(j == 0){
                    int idx = j;
                    // 오른쪽으로 쭉 뻗어나간다
                    while (idx < N - 1 && arr[i][idx].equals(arr[i][idx+1])) {
                        idx++;
                        temp++;
                    }
                } else {
                    // 왼쪽으로 쭉 뻗어나간다.
                    int idx = j;
                    while (idx > 0 && arr[i][idx].equals(arr[i][idx-1])) {
                        idx--;
                        temp++;
                    }

                    idx = j;
                    // 오른쪽으로 쭉 뻗어나간다
                    while (idx < N - 1 && arr[i][idx].equals(arr[i][idx+1])) {
                        idx++;
                        temp++;
                    }
                }
                // 만약 maximum이 0이 아니라면, 좌우 탐색을 통해 얻은 사탕이 있다는 의미이므로, 탐색을 시작한 idx의 사탕만큼 1을 더해줘야함
                if(temp != 0){
                    temp++;
                }
                maximum = Math.max(maximum, temp);
            }
        }
        return maximum;
    }

    // 세로줄 탐색
    public static int findVertical(){
        int maximum = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int temp = 0;
                // 첫 행 예외처리
                if(i == 0){
                    int idx = j;
                    // 아래로 쭉 뻗어나간다.
                    while (idx < N - 1 && arr[idx][i].equals(arr[idx+1][i])) {
                        idx++;
                        temp++;
                    }
                } else {
                    // 위로 쭉 뻗어나간다.
                    int idx = j;
                    while (idx > 0 && arr[idx][i].equals(arr[idx-1][i])) {
                        idx--;
                        temp++;
                    }

                    idx = j;
                    // 아래로 쭉 뻗어나간다.
                    while (idx < N - 1 && arr[idx][i].equals(arr[idx+1][i])) {
                        idx++;
                        temp++;
                    }
                }
                // 만약 maximum이 0이 아니라면, 좌우 탐색을 통해 얻은 사탕이 있다는 의미이므로, 탐색을 시작한 idx의 사탕만큼 1을 더해줘야함
                if(temp != 0){
                    temp++;
                }
                maximum = Math.max(maximum, temp);
            }
        }
        return maximum;
    }
}
