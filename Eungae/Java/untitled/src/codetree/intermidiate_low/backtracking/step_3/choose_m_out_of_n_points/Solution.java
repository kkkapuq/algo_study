package codetree.intermidiate_low.backtracking.step_3.choose_m_out_of_n_points;

import java.util.*;
import java.io.*;


public class Solution {
    public static class Pair {
        int x, y;

        public Pair(int x, int y){
            this.x = x;
            this.y = y;
        }
    }

    public static int n, m;
    public static int answer = Integer.MAX_VALUE;
    public static List<Pair> pairList = new ArrayList<>();
    public static List<Pair> selectList = new ArrayList<>();

    public static void main(String[] args) throws IOException{
        input();
        find(0, 0);
        System.out.print((int) (answer));
    }

    public static int calc(){
        int dist = Integer.MIN_VALUE;

        for(int i = 0; i < selectList.size()-1; i++){
            Pair tempA = selectList.get(i);
            int ax = tempA.x;
            int ay = tempA.y;
            for(int j = i+1; j < selectList.size(); j++){
                Pair tempB = selectList.get(j);
                int bx = tempB.x;
                int by = tempB.y;

                int tempDist = (int) Math.pow(ax-bx, 2) + (int) Math.pow(ay-by, 2);

                // System.out.println("현재 A = " + ax + ", " + ay);
                // System.out.println("현재 B = " + bx + ", " + by);
                if(tempDist > dist)
                    dist = tempDist;
            }
        }
        return dist;
    }

    public static void find(int currIdx, int cnt){
        if(currIdx == n){
            if(cnt == m){
                answer = Math.min(answer, calc());
            }
            return;
        }

        selectList.add(pairList.get(currIdx));
        // 현재 좌표를 고른 경우
        find(currIdx+1, cnt+1);
        selectList.remove(selectList.size()-1);

        // 현재 좌표를 고르지 않은 경우
        find(currIdx+1, cnt);
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            pairList.add(new Pair(x, y));
        }
    }
}

