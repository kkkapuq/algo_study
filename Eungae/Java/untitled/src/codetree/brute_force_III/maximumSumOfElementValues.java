package codetree.brute_force_III;

import java.util.*;

public class maximumSumOfElementValues {

    public static void solution(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int answer = 0;
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        for (int i = 0; i < n; i++) {
            // j-1 인덱스로 가야됨
            int tempSum = 0;
            int position = i;
            for (int j = 0; j < m; j++) {
                tempSum += arr[position];
                position = arr[position] - 1;
            }
            answer = Math.max(tempSum, answer);
        }

        System.out.println(answer);
    }
}
