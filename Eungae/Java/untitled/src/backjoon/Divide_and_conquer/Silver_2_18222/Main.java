package backjoon.Divide_and_conquer.Silver_2_18222;

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long k = Long.parseLong(br.readLine());

        // 인덱스로 접근해야 하므로 k-1로 설정
        int answer = recursive(k-1);
        System.out.println(answer);
    }

    private static int recursive(long k) {
        if(k == 0)
            return 0;
        else if(k == 1)
            return 1;
        else if(k % 2 == 0)
            return recursive(k/2);
        else
            return 1 - recursive(k/2);
    }
}