import java.util.*;

class Solution {
    public long solution(long n) {
        long answer = 0;
        String s = Long.toString(n);
        String[] arr = s.split("");
        
        Arrays.sort(arr, Collections.reverseOrder());
        
        StringBuilder sb = new StringBuilder();
        for(String str : arr) {
            sb.append(str);
        }
        
        return Long.parseLong(sb.toString());
    }
}