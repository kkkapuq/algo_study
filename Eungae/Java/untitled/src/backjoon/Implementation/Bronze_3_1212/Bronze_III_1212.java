package backjoon.Implementation.Bronze_3_1212;

import java.io.*;

/**
 * 문제 : 8진수 2진수
 * 링크 : https://www.acmicpc.net/problem/1212
 * 소요시간 : 30분
 */
public class Bronze_III_1212 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringBuilder stringBuilder = new StringBuilder();

        String str = br.readLine();
        int n = str.length();

        for (int i = 0; i < n; i++) {
            String a = Integer.toBinaryString(str.charAt(i) - '0');
            if(a.length() == 2 && i != 0)
                a = "0" + a;
            else if (i != 0 && a.length()==1)
                a = "00" + a;

            stringBuilder.append(a);
        }
        bw.write(stringBuilder.toString());

        bw.close();
        br.close();
    }
}
