import java.util.*;

class Solution {
    public int N;
    public List<Integer> selectList = new ArrayList<>();
    
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