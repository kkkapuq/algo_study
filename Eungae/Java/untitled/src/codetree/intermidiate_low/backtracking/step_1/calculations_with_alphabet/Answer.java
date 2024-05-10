package codetree.intermidiate_low.backtracking.step_1.calculations_with_alphabet;

import java.util.*;
import java.io.*;

public class Answer {
    public static final int INT_MIN = Integer.MIN_VALUE;
    public static final int MAX_N = 6;

    public static int n = 6;

    public static String expression;
    public static int[] num = new int[MAX_N];
    public static int ans = INT_MIN;

    public static void main(String[] args) throws IOException {
        input();
        recursion(0);
        System.out.print(ans);
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        expression = br.readLine();
    }

    public static int conv(int idx) {
        return num[expression.charAt(idx) - 'a'];
    }

    public static int calc() {
        int length = expression.length();
        int value = conv(0);
        for(int i = 2; i < length; i += 2){
            if(expression.charAt(i-1) == '+')
                value += conv(i);
            else if(expression.charAt(i-1) == '-')
                value -= conv(i);
            else
                value *= conv(i);
        }
        return value;
    }

    public static void recursion(int cnt){
        if(cnt == n) {
            ans = Math.max(ans, calc());
            return;
        }

        for(int i = 1; i <= 4; i++){
            num[cnt] = i;
            recursion(cnt+1);
        }
    }
}
