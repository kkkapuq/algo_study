package programmers.level2;

import java.util.Collections;
import java.util.LinkedList;

public class Problem42587 {
    public int solution(int[] priorities, int location) {
        int answer = 0;

        LinkedList<int[]> q = new LinkedList<int[]>();
        for (int i = 0; i < priorities.length; i++)
            q.add(new int[]{i, priorities[i]});

        LinkedList<Integer> q2 = new LinkedList<Integer>();
        for (int i : priorities)
            q2.add(i);

        while (q.size() > 0) {
            int rank = Collections.max(q2);
            int[] temp1 = q.removeFirst();
            int temp2 = q2.removeFirst();

            int idx = temp1[0], priority = temp1[1];
            if (priority < rank) {
                q.add(temp1);
                q2.add(temp2);
            } else {
                if (idx == location) {
                    answer += 1;
                    break;
                } else {
                    answer += 1;
                }
            }
        }
        return answer;
    }
}
