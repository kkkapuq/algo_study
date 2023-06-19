package codetree.brute_force_II;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

/**
 * 문제 : 스승의 은혜 3
 * 난이도 : 실력체크
 * 링크 : https://www.codetree.ai/missions/5/problems/the-grace-form-teacher-3/
 */
public class theGraceFormTeacher3 {
    public static void solution(){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(), b = sc.nextInt();
        int[][] students = new int[n][3];

        int answer = 0;
        // 입력
        for(int i = 0; i < n; i++){
            students[i][0] = sc.nextInt();
            students[i][1] = sc.nextInt();
            students[i][2] = students[i][0] + students[i][1];
        }

        // 총계액 기준으로 정렬
        Arrays.sort(students, Comparator.comparingInt(arr -> arr[2]));

        for(int i = 0; i < n; i++){
            int money = (students[i][0] / 2) + students[i][1];
            int temp = 0;
            if(money > b)
                continue;
            else
                temp++;
            for(int j = 0; j < n; j++){
                if(i==j)
                    continue;
                money += students[j][0] + students[j][1];
                if(money > b)
                    break;
                else
                    temp++;
            }
            answer = Math.max(temp, answer);
        }
        System.out.println(answer);
    }
}
