package programmers.Sort.Level_2_181188;

import java.util.Arrays;

public class Solution2 {
    public int solution(int[][] targets) {
        double cur = -1;
        int answer = 0;

        Arrays.sort(targets, (a, b) -> {
            return a[1] - b[1];
        });

        for(int i = 0; i < targets.length; i++){
            if(cur < targets[i][0]){
                answer++;
                cur = targets[i][1] - 0.5;
            }
        }

        return answer;
    }
}
