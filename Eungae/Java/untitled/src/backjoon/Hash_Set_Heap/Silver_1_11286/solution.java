package backjoon.Hash_Set_Heap.Silver_1_11286;
import java.sql.Array;
import java.util.*;
import java.io.*;

/**
 * 문제 : 절댓값 힙
 * 링크 : https://www.acmicpc.net/problem/111286
 * 소요시간 : 40분
 */
public class solution {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        Queue<Integer> pq = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                // 절댓값이 낮은 순서대로 넣어준다.
                if (Math.abs(o1) > Math.abs(o2)) {
                    // 내림차순으로 넣으려면
                    return Math.abs(o1) - Math.abs(o2);
                } else if (Math.abs(o1) == Math.abs(o2)) {
                    // 둘이 절대값이 같으면 음수로
                    return o1 - o2;
                } else {
                    // else 예외 처리
                    return -1;
                }
            }
        });


        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int temp = Integer.parseInt(st.nextToken());
            if(temp == 0){
                if (pq.isEmpty()) {
                    bw.write("0\n");
                } else {
                    bw.write(pq.poll().toString()+"\n");
                }
            } else {
                pq.add(temp);
            }
        }

        bw.close();
        br.close();
    }
}
