package codetree.intermidiate_low.backtracking.n_permutations_of_k_with_repetition;

import java.util.*;
import java.io.*;

public class Main {
    public static int K;
    public static int N;
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

    public static void print(){
        for(int i : list){
            System.out.print(i + " ");
        }
        System.out.println();
    }

    public static void recursion(int num) {
        if(num >= N){
            print();
            return;
        }

        for(int i = 1; i <= K; i++){
            list.add(i);
            recursion(num+1);
            list.remove(list.size()-1);
        }
    }
}