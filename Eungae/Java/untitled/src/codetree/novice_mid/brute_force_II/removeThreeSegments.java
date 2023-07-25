package codetree.novice_mid.brute_force_II;


import java.util.Scanner;

public class removeThreeSegments {
    public static void solution(){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // 개행문자 삭제
        sc.nextLine();
        int[][] lines = new int[n][2];
        for(int i = 0; i < n; i++){
            String s = sc.nextLine();
            String[] temp = s.split(" ");
            lines[i][0] = Integer.parseInt(temp[0]);
            lines[i][1] = Integer.parseInt(temp[1]);
        }

        int answer = 0;

        for(int i = 0; i < n; i++){
            for(int j = i+1; j < n; j++){
                for(int k = j+1; k < n; j++){
                    int[] arr = new int[100];
                    boolean flag = true;

                    for(int l = 0; l < n; l++){
                        if(l==i || l ==k || l==j)
                            continue;
                        for(int m = lines[l][0]; m < lines[l][1]+1; m++){
                            arr[m]++;
                            if(arr[m] > 1)
                                flag = false;
                        }
                    }
                    if(flag)
                        answer++;
                }
            }
        }
        System.out.println(answer);
    }
}
