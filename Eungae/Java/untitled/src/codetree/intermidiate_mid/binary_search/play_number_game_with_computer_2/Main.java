package codetree.intermidiate_mid.binary_search.play_number_game_with_computer_2;

import java.util.*;
import java.io.*;

/**
 * 문제 : 컴퓨터와 함께하는 숫자 게임 2
 * 소요 시간 : 40분
 * 링크 : https://www.codetree.ai/missions/8/problems/play-number-game-with-computer-2/description
 */
public class Main {
    public static long a, b, m;
    public static long minCnt = Long.MAX_VALUE;
    public static long maxCnt = Long.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        input();
        find();
        System.out.print(minCnt + " " + maxCnt);
    }

    public static long binarySearch(long target) {
        long l = 1;
        long r = m;
        long cnt = 1;

        while(l <= r) {
            long mid = (l+r)/2;
            if(mid == target){
                return cnt;
            }
            if(mid > target)
                r = mid - 1;
            else
                l = mid + 1;
            cnt++;
        }
        return -1;
    }

    public static void find() {
        for(long i = a; i <= b; i++){
            long cnt = binarySearch(i);

            minCnt = Math.min(minCnt, cnt);
            maxCnt = Math.max(maxCnt, cnt);
        }
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        m = Long.parseLong(st.nextToken());

        st = new StringTokenizer(br.readLine());
        a = Long.parseLong(st.nextToken());
        b = Long.parseLong(st.nextToken());
    }
}
