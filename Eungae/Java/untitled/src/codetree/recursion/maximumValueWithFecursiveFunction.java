package codetree.recursion;

import java.util.Scanner;

public class maximumValueWithFecursiveFunction {
    public static int[] nums = new int[100];

    public static void solution(){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        for(int i = 0; i < n; i++){
            nums[i] = sc.nextInt();
        }
        System.out.println(recursion(n-1));
    }

    public static int recursion(int n){
        if(n == 0)
            return nums[0];
        return Math.max(recursion(n-1), nums[n]);
    }
}
