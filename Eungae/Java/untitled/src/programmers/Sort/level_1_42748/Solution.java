package programmers.Sort.level_1_42748;

import java.util.*;

/**
 * 문제 : K번째 수
 * 소요 시간 : 10분
 * 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42748?language=java
 */
class Solution {

    public int[] solution(int[] array, int[][] commands) {
        int n = commands.length;
        int[] answer = new int[n];

        for(int i = 0; i < n; i++){
            int ii = commands[i][0] - 1;
            int jj = commands[i][1] - 1;
            int k = commands[i][2] - 1;
            int[] temp = sliceArray(array, ii, jj);

            Arrays.sort(temp);

            answer[i] = temp[k];
        }
        return answer;
    }

    public int[] sliceArray(int[] arr, int ii, int jj) {
        int n = jj - ii + 1;
        int[] temp = new int[n];

        for(int i = 0; i < n; i++){
            temp[i] = arr[ii];
            ii++;
        }

        return temp;
    }
}
