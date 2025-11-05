package backjoon.Two_Pointer.Gold_4_1806;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static int n, s;
    private static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        arr = new int[n];

        s = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int answer = Integer.MAX_VALUE;

        int start = 0, end = 0;
        int sum = arr[start];

        while(start <= end && end < n) {
            if (sum >= s) {
                answer = Math.min(answer, end - start + 1);
                sum -= arr[start];
                start++;
            } else {
                end++;
                if(end == n){
                    break;
                }
                sum += arr[end];
            }
        }

        if (answer == Integer.MAX_VALUE) {
            System.out.println(0);
        } else {
            System.out.println(answer);
        }
    }
}
