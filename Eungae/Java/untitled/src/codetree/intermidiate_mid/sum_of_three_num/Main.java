package codetree.intermidiate_mid.sum_of_three_num;

import java.util.*;
import java.io.*;

/**
 * 문제 : 세 수의 합
 * 소요 시간 : 30분
 * 링크 : https://www.codetree.ai/missions/8/problems/sum-of-three-numbers/description
 */
public class Main {
    public static int n, k;
    public static int[] arr;
    public static int answer = 0;

    public static Map<Integer, Integer> map = new HashMap<>();

    public static void main(String[] args) throws IOException{
        input();
        find();
        System.out.print(answer);
    }

    public static void find() {
        for(int i = 0; i < n; i++){
            if(!map.containsKey(arr[i])){
                map.put(arr[i], -1);
            } else {
                map.put(arr[i], map.get(arr[i]) - 1);
            }

            for(int j = 0; j < i; j++){
                if(map.containsKey(k - arr[i] - arr[j]))
                    answer += map.get(k - arr[i] - arr[j]);
            }
        }
    }

    public static void input() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        arr = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        for(int i : arr) {
            int defaultValue = 0;
            map.put(i, map.getOrDefault(i, defaultValue) + 1);
        }
    }
}
