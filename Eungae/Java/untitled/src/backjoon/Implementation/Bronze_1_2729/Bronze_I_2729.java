package backjoon.Implementation.Bronze_1_2729;

import java.io.*;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Bronze_I_2729 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String[] arr = br.readLine().split(" ");
            String a = arr[0], b = arr[1];

            BigInteger a1 = new BigInteger(a, 2);
            BigInteger b1 = new BigInteger(b, 2);

            StringBuilder sb = new StringBuilder();

            BigInteger answer = a1.add(b1);
            sb.append(answer.toString(2) + "\n");

            bw.write(sb.toString());
        }
        br.close();
        bw.close();
    }
}
