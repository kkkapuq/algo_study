import java.util.*;

class Solution {
    public String solution(String s, String skip, int index) {
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            int count = 0;
            while(count < index) {
                // 1. 다음 알파벳으로 이동
                c++;
                // 2. 알파벳 순환처리
                if(c > 'z') {
                    c = 'a';
                }
                // 3. skip 문자가 아니라면 정답처리 및 count 증가
                if(!isSkipped(skip, c)){
                    count++;
                }
            }
            sb.append(String.valueOf(c));
        }
        return sb.toString();
    }
    
    private boolean isSkipped(String skip, char c) {
        if(skip.indexOf(c) != -1){
            return true;
        }
        return false;
    }
}