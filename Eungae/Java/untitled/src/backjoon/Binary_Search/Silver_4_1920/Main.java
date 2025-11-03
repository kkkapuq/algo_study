package backjoon.Binary_Search.Silver_4_1920;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 문제 : 수 찾기
 * 난이도 : 실버 4
 */
public class Main {
    private static int n;
    private static int m;
    private static List<Integer> listA = new ArrayList<>();
    private static List<Integer> listB = new ArrayList<>();

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());

        while (st.hasMoreTokens()) {
            listA.add(Integer.parseInt(st.nextToken()));
        }

        Collections.sort(listA);

        st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());

        while (st.hasMoreTokens()) {
            listB.add(Integer.parseInt(st.nextToken()));
        }

        StringBuilder sb = new StringBuilder();

        for (int i : listB) {
            if (isExists(i)) {
                sb.append("1\n");
            } else {
                sb.append("0\n");
            }
        }
        System.out.println(sb);
    }

    private static boolean isExists(int number) {
        int start = 0;
        int end = listA.size()-1;

        while(start <= end) {
            int mid = (start + end) / 2;

            if(number < listA.get(mid)){
                end = mid - 1;
            } else if(number > listA.get(mid)){
                start = mid + 1;
            } else {
                return true;
            }
        }
        return false;
    }
}
