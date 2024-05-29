import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        int answer = 1;
        
        // 끝지점 기준 오름차순 정렬
        Arrays.sort(targets, (a, b) -> Integer.compare(a[1], b[1]));
        // System.out.println(Arrays.deepToString(targets));
        
        double pos = targets[0][1]-0.5;
        
        for(int i = 0; i < targets.length; i++){
            int start = targets[i][0];
            int end = targets[i][1];
            // System.out.println(i+1 + " 번 째 pos 값 = " + pos);
            if(start < pos && pos < end)
                continue;
            answer++;
            pos = end - 0.5;
            // System.out.println("현재 미사일 수 :" + answer);
        }
        
        return answer;
    }
}