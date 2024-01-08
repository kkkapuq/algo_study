import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        Map<String, Integer> map = new HashMap<>();
        for(int i = 0; i < players.length; i++){
            map.put(players[i], i);
        }
        
        for(String s : callings){
            int current = map.get(s);
            int before = current - 1;
            
            String temp = players[before];
            players[before] = s;
            players[current] = temp;
            
            map.put(s, before);
            map.put(temp, current);
        }
        return players;
    }
}