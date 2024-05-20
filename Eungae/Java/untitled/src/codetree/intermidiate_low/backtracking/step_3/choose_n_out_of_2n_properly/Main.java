package codetree.intermidiate_low.backtracking.step_3.choose_n_out_of_2n_properly;

import java.util.*;
import java.io.*;


public class Main {
    public static int n;
    public static int[] arr;
    public static int answer = Integer.MAX_VALUE;

    public static List<Integer> list = new ArrayList<>();
    public static List<Integer> idxList = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        input();
        find(0, 0);
        System.out.print(answer);
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        arr = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

    }

    public static int calc() {
        // 집합 A의 합
        int sum1 = list.stream()
                .mapToInt(Integer::intValue)
                .sum();

        // 집합 A 이외의 수 집합 B의 합
        int sum2 = 0;
        for(int i = 0; i < arr.length; i++){
            if(!idxList.contains(i))
                sum2 += arr[i];
        }

        return Math.abs(sum1 - sum2);
    }

    public static void find(int currIdx, int cnt){
        if(currIdx == 2*n){
            if(cnt == n){
                answer = Math.min(answer, calc());
            }
            return;
        }

        int num = arr[currIdx];

        // 고른 수와 해당 인덱스를 더해줌
        list.add(num);
        idxList.add(currIdx);

        // 현재 수를 고른 경우
        find(currIdx+1, cnt+1);
        list.remove(list.size()-1);
        idxList.remove(idxList.size()-1);

        // 현재 수를 고르지 않은 경우
        find(currIdx+1, cnt);
    }
}
