package programmers.hash.level_1_1845;

import java.util.*;

public class Solution {
    public int N;

    public int solution(int[] nums) {
        N = nums.length;

        Set<Integer> set = new HashSet<>();
        for(int i : nums){
            set.add(i);
        }

        int answer = Math.min(N/2, set.size());

        return answer;
    }
}
