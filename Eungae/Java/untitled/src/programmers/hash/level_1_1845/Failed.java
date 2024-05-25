package programmers.hash.level_1_1845;

import java.util.*;

class Failed {
    public int N;
    public List<Integer> selectList = new ArrayList<>();
    public int answer = 0;

    public int solution(int[] nums) {
        N = nums.length;

        // 조합을 구하고 set 해서 set의 length가 최대인 것을 구하자.
        recursion(nums, 0, 0);

        return answer;
    }

    public int calc(int[] nums) {
        Set<Integer> set = new HashSet<>();

        for(int i : selectList){
            set.add(nums[i]);
        }

        return set.size();
    }

    public void recursion(int[] nums, int currIdx, int cnt) {
        if(currIdx == N+1){
            if(cnt == N/2){
                answer = Math.max(answer, calc(nums));
            }
            return;
        }

        // 현재 수를 골랐을 때
        selectList.add(currIdx);
        recursion(nums, currIdx+1, cnt+1);
        selectList.remove(selectList.size()-1);

        // 현재 수를 고르지 않았을 때
        recursion(nums, currIdx+1, cnt);
    }
}