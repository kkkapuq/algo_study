package programmers.hash.level_1_42576;

import java.util.Arrays;

/**
 * 문제 : 완주하지 못한 선수
 * 소요 시간 : 5분
 * 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42576
 */
public class SortSolution {
    public String SortSolution(String[] participant, String[] completion) {
        String answer = "";

        Arrays.sort(participant);
        Arrays.sort(completion);

        for(int i = 0; i < completion.length; i++){
            if(!participant[i].equals(completion[i])){
                answer = participant[i];
                break;
            }
        }
        answer = answer.equals("") ? participant[participant.length - 1] : answer;

        return answer;
    }
}
