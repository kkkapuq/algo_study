package codetree.novice_mid.brute_force_II;

import java.util.Scanner;

public class StrangeBomb2 {
    public static void solution(){
        int[] bombs = new int[100];
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), k = sc.nextInt();

        for(int i = 0; i < n; i++){
            bombs[i] = sc.nextInt();
        }

        int answer = 0;

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(i == j)
                    continue;

                if(Math.abs(i-j) <= k && bombs[i] == bombs[j]){
                    answer = Math.max(bombs[i], answer);
                }

            }
        }

        System.out.println(answer != 0 ? answer : -1);
    }
}
