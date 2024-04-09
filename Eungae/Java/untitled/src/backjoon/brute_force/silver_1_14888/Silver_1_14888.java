package backjoon.brute_force.silver_1_14888;

import java.util.*;
import java.io.*;

class Silver_1_14888 {
    static int max = Integer.MIN_VALUE;
    static int min = Integer.MAX_VALUE;

    static int N;
    static int[] nums, operators, order;

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        nums = new int[N];
        operators = new int[4];
        order = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++){
            nums[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < 4; i++){
            operators[i] = Integer.parseInt(st.nextToken());
        }
    }

    // 피연산자 2개와 연산자가 주어졌을 때 계산해주는 함수
    static int calculator(int operand1, int operator, int operand2){
        // value, order[i], num[i+1]
        if (operator == 0) // +
            return operand1 + operand2;
        else if (operator == 1) // -
            return operand1 - operand2;
        else if (operator == 2) // *
            return operand1 * operand2;
        else // /
            return operand1 / operand2;
    }


    // order[1...N-1] 에 연산자들이 순서대로 저장될 것이다.
    static void rec_func(int k, int value) {
        if (k == N) {
            // 완성된 식에 맞게 계산을 해서 정답에 갱신하는 작업
            max = Math.max(max, value);
            min = Math.min(min, value);
        } else {
            // k 번째 연산자는 무엇을 선택할 것인가?
            for (int cand = 0; cand <= 3; cand++){
                if (operators[cand] >= 1){
                    operators[cand]--;
                    rec_func(k + 1, calculator(value, cand, nums[k + 1]));
                    operators[cand]++;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        input();
        rec_func(0, nums[0]);
        System.out.println(max);
        System.out.println(min);
    }
}
