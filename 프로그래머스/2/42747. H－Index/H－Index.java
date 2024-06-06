import java.util.*;

class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);
        
        int answer = 0;
        int n = citations.length;
        for(int i = 0; i < n; i++){
            int temp = Math.min(citations[i], n-i);
            answer = Math.max(answer, temp);
        }
        return answer;
    }
}