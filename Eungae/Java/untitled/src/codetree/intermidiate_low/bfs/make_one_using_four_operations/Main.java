package codetree.intermidiate_low.bfs.make_one_using_four_operations;

import java.util.*;
import java.io.*;

/**
 * 문제 : 4가지 연산으로 1 만들기
 * 소요 시간 : 45분
 * 링크 : https://www.codetree.ai/missions/2/problems/make-one-using-four-operations/description
 */
public class Main {
    public static int n;
    public static int[] visited = new int[10000000];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        Deque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{n, 0});
        visited[0] = 1;

        while(!q.isEmpty()){
            int[] temp = q.poll();
            int num = temp[0];
            int cnt = temp[1];

            if(num == 1){
                System.out.print(cnt);
                break;
            }

            if(visited[num-1] == 0) {
                q.add(new int[]{num-1, cnt+1});
                visited[num-1] = visited[num] + 1;
            }
            if(visited[num+1] == 0) {
                q.add(new int[]{num+1, cnt+1});
                visited[num+1] = visited[num] + 1;
            }

            if(num % 2 == 0 && visited[num/2] == 0) {
                q.add(new int[]{num/2, cnt+1});
                visited[num/2] = visited[num] + 1;
            }
            if(num % 3 == 0 && visited[num/3] == 0) {
                q.add(new int[]{num/3, cnt+1});
                visited[num/3] = visited[num] + 1;
            }
        }
    }
}
