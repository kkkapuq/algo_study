package codetree.intermidiate_low.backtracking.step_2.n_permutations_of_k_with_repetition_under_constraint;

import java.util.*;
import java.io.*;

public class Main {
    public static int N, K;
    public static List<Integer> list = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        input();
        recursion(0);
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        K = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
    }

    public static void print() {
        for(int i = 0; i < list.size(); i++){
            System.out.print(list.get(i) + " ");
        }
    }

    public static void recursion(int num){
        if(num == N){
            print();
            System.out.println();
            return;
        }

        for(int i = 1; i <= K; i++){
            if(num >= 2 &&
                    i == list.get(list.size()-1) &&
                    i == list.get(list.size()-2)) {
                continue;
            }
            list.add(i);
            recursion(num + 1);
            list.remove(list.size()-1);
        }
    }
}
