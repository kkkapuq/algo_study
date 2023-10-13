package backjoon.Hash_Set_Heap.Gold_4_7662;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * 문제 : 이중 우선순위
 * 링크 : https://www.acmicpc.net/problem/7662
 * 소요시간 : 38분
 */
public class Failed {
    public static void failed() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 0; tc < T; tc++) {
            int k = Integer.parseInt(br.readLine());
            // 최소 힙, 우선순위가 낮은 순서대로
            Queue<Integer> minQ = new PriorityQueue<>();
            // 최대 힙, 우선순위가 높은 순서대로
            Queue<Integer> maxQ = new PriorityQueue<>(Collections.reverseOrder());
            for (int i = 0; i < k; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                String order = st.nextToken();
                int num = Integer.parseInt(st.nextToken());

                if (order.equals("I")) {
                    minQ.add(num);
                    maxQ.add(num);
                } else if (order.equals("D")) {
                    if (minQ.isEmpty() || maxQ.isEmpty()) {
                        continue;
                    }
                    // 최솟값 삭제
                    if (num == -1) {
                        minQ.poll();
                    }
                }
            }

        }
    }
}
