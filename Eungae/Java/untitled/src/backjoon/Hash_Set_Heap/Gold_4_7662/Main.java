package backjoon.Hash_Set_Heap.Gold_4_7662;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 문제 : 이중 우선순위 큐
 * 링크 : https://www.acmicpc.net/problem/7662
 * 소요시간 : 풀이참조
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for (int tc = 0; tc < T; tc++) {
            int k = Integer.parseInt(br.readLine());
            SortedMap<Integer, Integer> treeMap = new TreeMap<>();

            for (int i = 0; i < k; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                String order = st.nextToken();
                int num = Integer.parseInt(st.nextToken());

                if (order.equals("I")) {
                    // 이 수가 map에 저장된 수라면 value에 1씩 더해주고, 아니라면 0을 넣어준다는 뜻
                    treeMap.put(num, treeMap.getOrDefault(num, 0) + 1);
                } else if (order.equals("D")) {
                    if (treeMap.size() == 0) {
                        continue;
                    }
                    // 삭제해야 하는 수를 가져온다.
                    int key;
                    if (num == -1) {
                        key = treeMap.firstKey();
                    } else {
                        key = treeMap.lastKey();
                    }
                    // 만약 2개 이상이여도 하나만 삭제한다.
                    if (treeMap.get(key) > 1) {
                        treeMap.put(key, treeMap.get(key)-1);
                    } else {
                        treeMap.remove(key);
                    }
                }
            }

            if (treeMap.size() == 0) {
                sb.append("EMPTY\n");
            } else {
                sb.append(treeMap.lastKey() + " " + treeMap.firstKey() + "\n");
            }
        }
        System.out.println(sb.toString());
    }
}
