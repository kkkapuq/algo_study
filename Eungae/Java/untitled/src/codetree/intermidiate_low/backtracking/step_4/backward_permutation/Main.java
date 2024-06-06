package codetree.intermidiate_low.backtracking.step_4.backward_permutation;

import java.util.*;
import java.io.*;

public class Main {
    public static int n;
    public static List<Integer> list = new ArrayList<>();
    public static boolean[] visited;

    public static void main(String[] args) throws IOException{
        input();
        recursion(n);
    }

    public static void recursion(int currNum) {
        if(currNum == 0) {
            print();
            return;
        }

        for(int i = n; i >= 1; i--) {
            if(visited[i])
                continue;
            visited[i] = true;
            list.add(i);

            recursion(currNum-1);
            list.remove(list.size()-1);

            visited[i] = false;
        }
    }

    public static void print() {
        for(int i : list) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

    public static void input() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        visited = new boolean[n+1];
    }
}
