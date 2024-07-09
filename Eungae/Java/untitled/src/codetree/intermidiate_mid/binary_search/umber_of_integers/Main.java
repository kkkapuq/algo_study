package codetree.intermidiate_mid.binary_search.umber_of_integers;

import java.util.*;
import java.io.*;

/**
 * 문제 : 숫자의 개수
 * 소요 시간 : 30분
 * 링크 : https://www.codetree.ai/missions/8/problems/umber-of-integers/description
 */
public class Main {
    public static int[] arr;
    public static int n, m;

    public static void main(String[] args) throws IOException {
        input();
    }

    public static void find(int target) {
        int l = 0;
        int r = n-1;
        int lowerIdx = n;
        int upperIdx = n;

        while(l <= r) {
            int mid = (l + r) / 2;
            if(arr[mid] >= target){
                r = mid -1;
                lowerIdx = Math.min(lowerIdx, mid);
            }
            else
                l = mid + 1;
        }

        l = 0;
        r = n-1;

        while(l <= r) {
            int mid = (l + r) / 2;
            if(arr[mid] > target){
                r = mid -1;
                upperIdx = Math.min(upperIdx, mid);
            }
            else
                l = mid + 1;
        }

        System.out.println(upperIdx - lowerIdx);
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        for(int i = 0; i < m; i++){
            int target = Integer.parseInt(br.readLine());
            find(target);
        }
    }
}