import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        String str = s;
        while(s.length() > 1){
            int index = 0;
            char c = s.charAt(index);
            int xCount = 1;
            int notxCount = 0;
            while(xCount != notxCount && index < s.length()-1){
                index++;
                if(s.charAt(index) == c){
                    xCount++;
                } else {
                    notxCount++;
                }
            }
            answer++;
            s = s.substring(index+1);
        }
        if(s.length() == 1) answer++;
        return answer;
    }
}