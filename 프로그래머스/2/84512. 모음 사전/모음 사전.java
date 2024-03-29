import java.util.*;

class Solution {
    static String[] words = {"A", "E", "I", "O", "U"};
    static List<String> list = new ArrayList<>();
    public int solution(String word) {
        int answer = 0;
        String str = "";

        dfs(str, 0);

        answer = list.indexOf(word);
        return answer;
    }

    public void dfs(String str, int len){
        list.add(str);
        if(len == 5)
            return;
        for(int i = 0; i < 5; i++){
            dfs(str + words[i], len+1);
        }
    }
}