package codetree.novice_mid.brute_force_III;


import java.util.Scanner;

public class studyCafeKeepingDistance5 {
    public static int n;
    public static char[] arr;

    public static int getDist(){
        int minDist = n;
        for(int i = 0; i < n; i++)
            for(int j = i+1; j < n; j++)
                if(arr[i] == '1' && arr[j] == '1')
                    minDist = Math.min(minDist, Math.abs(j-i));
        return minDist;
    }

    public static void solution(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        arr = sc.next().toCharArray();

        int answer = 0;

        for(int i = 0; i < n; i++){
            int distance = 0;
            for(int j = 0; j < n; j++){
                if(arr[i] == '0'){
                    arr[i] = '1';
                    answer = Math.max(answer, getDist());
                    arr[i] = '0';
                }
            }
        }
        System.out.println(answer);
    }
}
