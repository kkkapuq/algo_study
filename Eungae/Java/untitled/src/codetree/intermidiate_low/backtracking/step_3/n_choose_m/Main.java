package codetree.intermidiate_low.backtracking.step_3.n_choose_m;

import java.util.*;
import java.io.*;

/**
 * 문제 : n개중에서 m개 뽑기
 * 소요 시간 : 1시간
 * 링크 : https://www.codetree.ai/missions/2/problems/n-choose-m/description
 */
public class Main {
    public static int N, M;
    public static List<Integer> list = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        input();

        for(int i = 1; i <= N; i++){
            list.add(i);
            recursion(i, 1);
            list.remove(list.size()-1);
        }
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
    }

    public static void print() {
        for(int i = 0; i < list.size(); i++){
            System.out.print(list.get(i) + " ");
        }
        System.out.println();
    }

    public static void recursion(int lastNum, int cnt) {
        if(cnt == M){
            print();
            return;
        }

        for(int i = lastNum+1; i <= N; i++){
            list.add(i);
            recursion(i, cnt+1);
            list.remove(list.size()-1);
        }
    }

}