package codetree.intermidiate_mid.binary_search.first_appear_number;

import java.util.*;
import java.io.*;

/**
 * 문제 : 가장 먼저 나오는 숫자
 * 소요 시간 : 20분
 * 링크 : https://www.codetree.ai/missions/8/problems/first-appear-number/description
 */
public class Main {
    public static int[] arr;
    public static int n, m;

    public static void main(String[] args) throws IOException {
        input();
    }

    public static int find(int target) {
        int l = 0;
        int r = n-1;
        int minIdx = n;

        while(l <= r) {
            int mid = (l + r) / 2;
            if(arr[mid] >= target){
                r = mid -1;
                minIdx = Math.min(minIdx, mid);
            }
            else
                l = mid + 1;
        }
        return minIdx;
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int[] temp = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        for(int t : temp) {
            int idx = find(t);
            if(idx < n && arr[idx] == t)
                System.out.println(idx+1);
            else
                System.out.println(-1);
        }
    }
}