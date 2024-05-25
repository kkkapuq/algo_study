package programmers.hash.level_1_42576;

import java.util.*;

/**
 * 문제 : 완주하지 못한 선수
 * 소요 시간 : 34분
 * 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42576
 */
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";

        Map<String, Integer> map = new HashMap<>();

        for(int i = 0; i < completion.length; i++){
            if(map.containsKey(completion[i])){
                map.put(completion[i], map.get(completion[i])+1);
            } else {
                map.put(completion[i], 1);
            }
        }

        for(int i = 0; i < participant.length; i++){
            if(!map.containsKey(participant[i])){
                answer = participant[i];
                break;
            }
            map.put(participant[i], map.get(participant[i])-1);
        }

        Iterator<Map.Entry<String, Integer>> iter = map.entrySet().iterator();
        while(iter.hasNext()){
            Map.Entry<String, Integer> entry = iter.next();
            if(entry.getValue() < 0){
                answer = entry.getKey();
                break;
            }
        }
        return answer;
    }
}
