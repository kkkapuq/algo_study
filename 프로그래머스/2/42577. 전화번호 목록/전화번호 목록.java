import java.util.*;

class Solution {
    public boolean solution(String[] phoneBook) {
        Map map = new HashMap();
        for (String s : phoneBook) {
            map.put(s, 1);
        }
        for (String s : phoneBook) {
            String temp = "";
            for (char c : s.toCharArray()) {
                temp += c;
                if (map.containsKey(temp) && !s.equals(temp)) {
                    return false;
                }
            }
        }
        return true;
    }
}