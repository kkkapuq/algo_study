import java.util.*;

class Solution {
    static List<int[]> list = new ArrayList<>();
    public int solution(String[][] bookTime) {
        int answer = 0;
                
        Arrays.sort(bookTime, Comparator.comparing(x -> x[0]));
        
        for(String[] str : bookTime){
            int sh = Integer.parseInt(str[0].split(":")[0]) * 60;
            int sm = Integer.parseInt(str[0].split(":")[1]);
            int s = sh+sm;
            
            int eh = Integer.parseInt(str[1].split(":")[0]) * 60;
            int em = Integer.parseInt(str[1].split(":")[1]);
            int e = eh+em;
            
            if(list.isEmpty()){
                list.add(new int[]{s, e});
            } else {
                int num = check(s, e);
                if(num == -1){
                    list.add(new int[]{s, e});
                } else {
                    list.set(num, new int[]{s, e});
                }
            }
        }
        answer = list.size();
        return answer;
    }
    
    public int check(int s, int e){
        for(int i = 0; i < list.size(); i++){
            int roomS = list.get(i)[0];
            int roomE = list.get(i)[1];
            // 종료 후 10분 이후보다 시작시간이 크면, 해당 방을 쓸 수 있다
            if(s >= roomE + 10){
                return i;
            }
        }
        return -1;
    }
}