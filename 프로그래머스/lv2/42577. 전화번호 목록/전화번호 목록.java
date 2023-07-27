import java.util.*;

class Solution {
    public boolean solution(String[] phoneBook) {
        Arrays.sort(phoneBook);

        for (int i = 0; i < phoneBook.length - 1; i++) {
            int n = phoneBook[i].length();
            if (phoneBook[i+1].length() >= n && phoneBook[i + 1].substring(0, n).equals(phoneBook[i])) {
                return false;
            }
        }
        return true;
    }
}