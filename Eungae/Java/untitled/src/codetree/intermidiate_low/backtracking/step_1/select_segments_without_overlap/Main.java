package codetree.intermidiate_low.backtracking.step_1.select_segments_without_overlap;

import java.util.*;
import java.io.*;

/**
 * 문제 : 겹치지 않게 선분 고르기
 * 소요 시간 : 72분
 * 링크 : https://www.codetree.ai/missions/2/problems/select-segments-without-overlap/submissions
 */
public class Main {
    public static int N;
    public static int answer = 0;
    public static List<int[]> list = new ArrayList<>();
    public static List<int[]> selectedSegs = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        input();
        recursion(0);
        System.out.print(answer);
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            int[] temp = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
            list.add(temp);
        }
    }

    public static boolean overlapped(int[] a, int[] b){
        return (a[0] <= b[0] && b[0] <= a[1]) || (a[0] <= b[1] && b[1] <= a[1]) ||
                (b[0] <= a[0] && a[0] <= b[1]) || (b[0] <= a[1] && a[1] <= b[1]);
    }

    public static boolean possible() {
        for(int i = 0; i < selectedSegs.size(); i++){
            for(int j = i+1; j < selectedSegs.size(); j++){
                if(overlapped(selectedSegs.get(i), selectedSegs.get(j)))
                    return false;
            }
        }
        return true;
    }

    public static void recursion(int num){
        if(num == N){
            if(possible())
                answer = Math.max(answer, selectedSegs.size());
            return;
        }
        selectedSegs.add(list.get(num));
        recursion(num + 1);
        selectedSegs.remove(selectedSegs.size() - 1);
        recursion(num + 1);
    }
}