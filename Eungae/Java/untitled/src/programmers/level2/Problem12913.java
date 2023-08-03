package programmers.level2;

import java.util.Arrays;
import java.util.stream.Stream;

public class Problem12913 {
    int solution(int[][] land) {
        int answer = 0;
        int n = land.length;

        for(int i = 1; i < land.length; i++){
            for (int j = 0; j < 4; j++) {
                int[] temp;
                if(j == 0)
                    temp = Arrays.copyOfRange(land[i-1], 1, 4);
                else if(j == 3)
                    temp = Arrays.copyOfRange(land[i-1], 0, 3);
                else {
                    int[] temp1, temp2;
                    temp1 = Arrays.copyOfRange(land[i-1], 0, j);
                    temp2 = Arrays.copyOfRange(land[i-1], j+1, 4);
                    temp = Stream.concat(Arrays.stream(temp1).boxed(), Arrays.stream(temp2).boxed())
                            .mapToInt(Integer::intValue)
                            .toArray();
                }
                land[i][j] = land[i][j] + Arrays.stream(temp).max().getAsInt();
            }
        }
        answer = Arrays.stream(land[n-1]).max().getAsInt();
        return answer;
    }

    public static void main(String[] args) {
        Problem12913 temp = new Problem12913();
        System.out.println(temp.solution(new int[][]{{1,2,3,5}, {5,6,7,8}, {4,3,2,1}}));
    }
}
