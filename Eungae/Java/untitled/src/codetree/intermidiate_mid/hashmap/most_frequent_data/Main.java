package codetree.intermidiate_mid.hashmap.most_frequent_data;

import java.util.*;
import java.io.*;

/**
 * 문제 : 가장 많은 데이터
 * 소요 시간 : 10분
 * 링크 : https://www.codetree.ai/missions/8/problems/most-frequent-data/description
 */
public class Main {
    public static Map<String, Integer> map = new HashMap<>();

    public static void main(String[] args) throws IOException{
        input();
        int max = calc();
        System.out.print(max);
    }

    public static int calc() {
        int value = 0;

        for(Map.Entry<String, Integer> entry : map.entrySet()) {
            int temp = entry.getValue();
            value = Math.max(value, temp);
        }

        return value;
    }

    public static void input() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int defaultValue = 0;
        for(int i = 0; i < n; i++){
            String str = br.readLine();
            map.put(str, map.getOrDefault(str, defaultValue) + 1);
        }
    }
}