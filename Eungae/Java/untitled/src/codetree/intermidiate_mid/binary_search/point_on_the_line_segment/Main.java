package codetree.intermidiate_mid.binary_search.point_on_the_line_segment;

import java.util.*;
import java.io.*;

/**
 * 문제 : 선분 위의 점
 * 소요 시간 : 40분
 * 링크 : https://www.codetree.ai/missions/8/problems/point-on-the-line-segment/description
 */
public class Main {
    public static int[] dotArr;
    public static int[][] lineArr;
    public static int n, m;

    public static void main(String[] args) throws IOException {
        input();
    }

    public static int findMin(int start) {
        int l = 0;
        int r = n-1;
        int minIdx = n;

        while(l <= r) {
            int mid = (l + r) / 2;
            if(dotArr[mid] >= start){
                r = mid - 1;
                minIdx = Math.min(minIdx, mid);
            }
            else
                l = mid + 1;
        }
        return minIdx;
    }

    public static int findMax(int end) {
        int l = 0;
        int r = n-1;
        int minIdx = n;

        while(l <= r) {
            int mid = (l + r) / 2;
            if(dotArr[mid] > end){
                r = mid - 1;
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

        dotArr = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        Arrays.sort(dotArr);

        lineArr = new int[m][2];

        for(int i = 0; i < m; i++){
            lineArr[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            int start = lineArr[i][0];
            int end = lineArr[i][1];

            int cnt = 0;

            int min = findMin(start);
            int max = findMax(end);

            System.out.println(max - min);
        }
    }
}
