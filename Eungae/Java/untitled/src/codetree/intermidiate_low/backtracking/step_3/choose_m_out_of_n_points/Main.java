package codetree.intermidiate_low.backtracking.step_3.choose_m_out_of_n_points;

import java.util.*;
import java.io.*;

/**
 * 문제 : n개의 점 중 m개 고르기
 * 소요 시간 : 80분
 * 링크 : https://www.codetree.ai/missions/2/problems/choose-m-out-of-n-points/description
 */

class Pair {
    int x, y;

    public Pair(int x, int y){
        this.x = x;
        this.y = y;
    }
}

public class Main {
    public static int n, m;
    public static int answer = Integer.MAX_VALUE;
    public static int maxDist;
    public static List<Pair> pairList = new ArrayList<>();
    public static List<Pair> selectList = new ArrayList<>();
    // 고른 애들 중에서 가장 먼 점 찾을때 쓰는 리스트
    public static List<Pair> tempList = new ArrayList<>();

    public static void main(String[] args) throws IOException{
        input();
        find(0, 0);
        System.out.print(answer);
    }

    public static void find(int currIdx, int cnt){
        if(currIdx == n){
            if(cnt == m){
                // 여기서 계속 최대거리를 초기화시켜줬어야 했음, 이거때문에 오래걸림
                maxDist = Integer.MIN_VALUE;
                findPairs(0, 0);
                answer = Math.min(answer, maxDist);
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

    public static int getDist(int ax, int ay, int bx, int by){
        // System.out.println("현재 A = " + ax + ", " + ay);
        // System.out.println("현재 B = " + bx + ", " + by);
        // System.out.println("최대거리 = " + ((int) Math.pow(ax-bx, 2) + (int) Math.pow(ay-by, 2)));
        return (int) Math.pow(ax-bx, 2) + (int) Math.pow(ay-by, 2);
    }

    public static void findPairs(int currIdx, int cnt){
        if(currIdx == m){
            if(cnt == 2){
                Pair a = tempList.get(0);
                Pair b = tempList.get(1);
                maxDist = Math.max(maxDist, getDist(a.x, a.y, b.x, b.y));
            }
            return;
        }

        tempList.add(selectList.get(currIdx));
        findPairs(currIdx+1, cnt+1);
        tempList.remove(tempList.size()-1);

        findPairs(currIdx+1, cnt);
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
