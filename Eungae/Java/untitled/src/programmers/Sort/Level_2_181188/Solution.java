package programmers.Sort.Level_2_181188;

import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        int answer = 1;

        // a, b중 compare가 정순이면 오름차순, 역순이면 내림차순
        Arrays.sort(targets, (a, b) -> {
            return a[1]-b[1];
        });
        int cur = targets[0][1]-1;
        for(int[] arr : targets){
            int s = arr[0];
            int e = arr[1];

            if(cur >= s && cur <= e) continue;

            answer++;
            cur = e-1;
        }
        System.out.println(Arrays.deepToString(targets));
        return answer;
    }
}