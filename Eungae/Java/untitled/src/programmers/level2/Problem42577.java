package programmers.level2;

import java.util.*;

public class Problem42577 {
    public boolean solution(String[] phoneBook) {
        // 정렬을 사용한 풀이, 이게 더 효율이 좋음
//        Arrays.sort(phoneBook);
//
//        for (int i = 0; i < phoneBook.length - 1; i++) {
//            int n = phoneBook[i].length();
//            if (phoneBook[i+1].length() >= n && phoneBook[i + 1].substring(0, n).equals(phoneBook[i])) {
//                return false;
//            }
//        }
//        return true;
        // 맵을 사용한 풀이
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
