package codetree.novice_mid.brute_force_III;

import java.util.Scanner;

public class findSmallestX {
    public static int[][] arr;
    public static void solution() {
        int answer = Integer.MAX_VALUE;
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        arr = new int[n][2];
        for(int i = 0; i < n; i++) {
            arr[i][0] = sc.nextInt();
            arr[i][1] = sc.nextInt();
        }

        for(int i = 1; i < 5001; i++){
            int x = i*2;
            boolean flag = true;
            for(int[] j : arr){
                if(x >= j[0] && x <= j[1]){
                    x *= 2;
                } else {
                    flag = false;
                    break;
                }
            }
            if(flag)
                answer = Math.min(answer, i);
        }
        System.out.println(answer);
    }
}
