package programmers.Sort.Level_2_181188;

import java.util.*;

/**
 * 문제 : 요격 시스템
 * 소요 시간 : 30분
 * 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181188
 */
class Solution3 {
    public int solution(int[][] targets) {
        int answer = 1;

        // 끝지점 기준 오름차순 정렬
        Arrays.sort(targets, Comparator.comparingInt(a -> a[1]));
        System.out.println(Arrays.deepToString(targets));

        double pos = targets[0][1]-0.5;

        for(int i = 0; i < targets.length; i++){
            int start = targets[i][0];
            int end = targets[i][1];
            System.out.println(i+1 + " 번 째 pos 값 = " + pos);
            if(start < pos && pos < end)
                continue;
            answer++;
            pos = end - 0.5;
            System.out.println("현재 미사일 수 :" + answer);
        }

        return answer;
    }
}