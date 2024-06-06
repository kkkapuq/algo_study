package programmers.Sort.level_2_42747;

import java.util.*;

/**
 * 문제 : H-Index
 * 소요 시간 : 50분
 * 링크 :
 */
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
