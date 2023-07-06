package codetree.brute_force_III;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class maximumDifferenceInNumbers {
    public static int n, k;
    public static int[] arr;


    public static int countNum(int l, int r){
        int cnt =0;
        for(int i = 0; i < n; i++){
            if(l <= arr[i] && arr[i] <= r)
                cnt++;
        }
        return cnt;
    }

    public static void solution(){

        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        k = sc.nextInt();

        arr = new int[n];
        for(int i = 0; i < n; i++)
            arr[i] = sc.nextInt();

        int answer = 0;
        for(int i = 1; i <= 10001; i++){
            answer = Math.max(answer, countNum(i, i+k));
        }

        System.out.println(answer);
    }
}
