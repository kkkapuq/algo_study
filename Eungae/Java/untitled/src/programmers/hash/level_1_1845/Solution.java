package programmers.hash.level_1_1845;

import java.util.*;

/**
 * 문제 : 폰켓몬
 * 소요 시간 : 20분
 * 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/1845
 */
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
