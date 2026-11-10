import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        Map<String, Integer> map = new HashMap<>();
        
        for(int i = 0; i < players.length; i++){
            map.put(players[i], i);
        }
        
        for(String calling : callings) {
            int idx = map.get(calling);
            
            if(idx > 0) {
                String frontRunner = players[idx-1];
                players[idx-1] = calling;
                players[idx] = frontRunner;
                
                map.put(calling, idx-1);
                map.put(frontRunner, idx);
            }
        }
        
        return players;
    }
}