import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] supo1 = new int[]{1, 2, 3, 4, 5};
        int[] supo2 = new int[]{2, 1, 2, 3, 2, 4, 2, 5};
        int[] supo3 = new int[]{3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int n = answers.length;
        int[] scores = new int[3];
        List<Integer> list = new ArrayList<>();
        for(int i = 0; i < n; i++) {
            // 1번수포자
            if(answers[i] == supo1[i % supo1.length]){
                scores[0]++;
            }
            
            // 2번수포자
            if(answers[i] == supo2[i % supo2.length]){
                scores[1]++;
            }
            
            // 3번수포자
            if(answers[i] == supo3[i % supo3.length]){
                scores[2]++;
            }
        }
        
        // 최대점수 찾기
        int max = Integer.MIN_VALUE;
        for(int i = 0; i < 3; i++){
            max = Math.max(max, scores[i]);
        }
        
        // 최대점수랑 맞는사람 add
        for(int i = 0; i < 3; i++){
            if(scores[i] == max) {
                list.add(i+1);
            }
        }
        
        // 배열로 변환
        int[] answer = list.stream().mapToInt(Integer::intValue).toArray();
        
        return answer;
    }
}