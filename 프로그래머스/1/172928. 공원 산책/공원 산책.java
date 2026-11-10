import java.util.*;

class Solution {
    
    public int[] solution(String[] park, String[] routes) {
        int[] position = new int[]{0, 0};
        
        // 시작 위치 탐색
        for(int i = 0; i < park.length; i++) {
            int idx = park[i].indexOf('S');

            if(idx != -1) {
                position = new int[]{i, idx};
                break;
            }
        }
        
        for(int i = 0; i < routes.length; i++) {
            String[] route = routes[i].split(" ");
            String direction = route[0];
            int amount = Integer.parseInt(route[1]);
            
            int nr = position[0];
            int nc = position[1];
            boolean possible = true;
            
            for(int j = 0; j < amount; j++){ 
                if(direction.equals("E")) {
                    nc++;
                } else if(direction.equals("W")) {
                    nc--;
                } else if(direction.equals("S")) {
                    nr++;
                } else if(direction.equals("N")) {
                    nr--;
                }
                if(!isPossible(nr, nc, park)) {
                    possible = false;
                    break;
                }
            }
            
            if(possible) {
                position = new int[]{nr, nc};
            }
        }
        
        return position;
    }
    
    private boolean isPossible(int nr, int nc, String[] park) {
        int x = park.length;
        int y = park[0].length();
        
        if(nr < 0 || nc < 0 || nr >= x || nc >= y) {
            return false;
        }
        if(park[nr].charAt(nc) == 'X') {
            return false;
        }
        return true;
    }
}