import java.util.*;

class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        int cycle = 0;
        int n = score.length;
        
        Arrays.sort(score);
        
        while(n - (m * cycle) >= m) {
            int min = 10;
            for(int i = n - (m * cycle) - 1; i >= n - m - (m * cycle); i--) {
                min = Math.min(min, score[i]);
            }
            answer += min * m;
            cycle++;
        }
        
        return answer;
    }
}