import java.util.*;

class Solution {
    public int[] solution(int[] sequence, int k) {        
        int l = 0, r = 0;
        int n = sequence.length;
        int sum = sequence[0];
        
        int[] answer = {0, n};
        
        // 합 >= k이면 왼쪽을 늘리고
        // 합 < k 이면 오른쪽을 늘린다.
        while(true){
            if(sum < k){
                r++;
                if(r == n)
                    break;
                sum += sequence[r];
            } else {
                if(sum == k){
                    if(r - l < answer[1] - answer[0]){
                        answer = new int[]{l, r};
                    }
                }
                sum -= sequence[l];
                l++;
            }
        }
        return answer;
    }
}