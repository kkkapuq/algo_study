package backjoon.Two_Pointer.Silver_3_2559;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 문제 : 수열
 * 난이도 : 실버 3
 * 소요 시간 : 35분
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] arr = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        // 투포인터로 풀어보자
        int l = 0, r = k;
        // 정답 초기화
        int tempSum = Arrays.stream(arr, l, r).sum();
        int answer = tempSum;

        while(r < n){
            // 다음 r 포인터 값을 더해주고, 이전에 있던 l값은 빼준다.
            tempSum += arr[r++];
            tempSum -= arr[l++];
            answer = Math.max(answer, tempSum);
        }
        System.out.println(answer);
    }
}