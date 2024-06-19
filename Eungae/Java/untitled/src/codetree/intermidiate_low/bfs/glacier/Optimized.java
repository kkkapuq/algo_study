package codetree.intermidiate_low.bfs.glacier;

import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;
import java.util.Collections;

class Pair {
    int x, y;
    public Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Optimized {
    public static final int MAX_M = 200;
    public static final int MAX_N = 200;
    public static final int DIR_NUM = 4;

    public static final int WATER = 0;
    public static final int GLACIER = 1;

    // 전역 변수 선언:
    public static int n, m;

    public static int[][] a = new int[MAX_N][MAX_M];

    // bfs에 필요한 변수들 입니다.
    public static Queue<Pair> q = new LinkedList<>();
    public static boolean[][] visited = new boolean[MAX_N][MAX_N];
    public static int cnt;

    public static Queue<Pair> glaciersToMelt = new LinkedList<>();

    public static int[] dx = new int[]{1, -1, 0, 0};
    public static int[] dy = new int[]{0, 0, 1, -1};

    // 소요 시간과 가장 마지막으로 녹은 빙하의 수를 저장합니다.
    public static int elapsedTime, lastMeltCnt;

    // 범위가 격자 안에 들어가는지 확인합니다.
    public static boolean inRange(int x, int y) {
        return 0 <= x && x < n && 0 <= y && y < m;
    }

    // 범위를 벗어나지 않으면서 물이여야 하고 방문한적이
    // 없어야 갈 수 있습니다.
    public static boolean canGo(int x, int y) {
        return inRange(x, y) && a[x][y] == WATER && !visited[x][y];
    }

    // 범위를 벗어나지 않으면서 빙하여야 하고 이미
    // 선택된 적이 없어야 중복 없이 녹아야할 빙하 목록에
    // 해당 빙하를 문제 없이 추가할 수 있습니다.
    public static boolean isGlacier(int x, int y) {
        return inRange(x, y) && a[x][y] == GLACIER && !visited[x][y];
    }

    // 아직 방문해보지 못한 빙하에 둘러쌓여 있지 않은 물 영역을 더 탐색해주는 BFS입니다.
    public static void BFS() {
        while(!q.isEmpty()) {
            // queue에서 가장 먼저 들어온 원소를 뺍니다.
            Pair currPos = q.poll();
            int x = currPos.x, y = currPos.y;

            // queue에서 뺀 원소의 위치를 기준으로 4 방향을 확인합니다.
            for(int dir = 0; dir < DIR_NUM; dir++) {
                int nx = x + dx[dir], ny = y + dy[dir];

                // 아직 방문한 적 없는 물이 있는 곳이라면 Queue에 추가합니다.
                if(canGo(nx, ny)) {
                    q.add(new Pair(nx, ny));
                    visited[nx][ny] = true;
                }
                // 만약 아직 방문하지 않은 빙하가 있는 곳이라면
                else if(isGlacier(nx, ny)) {
                    // 빙하에 둘러쌓여 있지 않은 물에 인접한 빙하이므로 이번에 녹아야 할 빙하이므로
                    // 따로 저장해줍니다.
                    // 중복되어 같은 빙하 정보가 기록되는 것을 막기위해
                    // 이때에도 visited 값을 true로 설정해줍니다.
                    glaciersToMelt.add(new Pair(nx, ny));
                    visited[nx][ny] = true;
                }
            }
        }
    }

    // 녹여야 할 빙하들을 녹여줍니다.
    public static void melt() {
        while(!glaciersToMelt.isEmpty()) {
            Pair pos = glaciersToMelt.poll();
            int x = pos.x, y = pos.y;

            a[x][y] = WATER;
        }
    }

    //
    public static boolean simulate() {
        // 빙하에 둘러쌓여 있지 않은 물의 영역을 넓혀보며
        // 더 녹일 수 있는 빙하가 있는지 봅니다.
        BFS();

        // 더 녹일 수 있는 빙하가 없다면 시뮬레이션을 종료합니다.
        if((int) glaciersToMelt.size() == 0)
            return false;

        // 더 녹일 빙하가 있다면 답을 갱신해주고
        // 그 다음 시뮬레이션에서는 해당 빙하들의 위치를 시작으로
        // 빙하에 둘러쌓여 있지 않은 물의 영역을 더 탐색할 수 있도록 queue에
        // 녹아야 할 빙하들의 위치를 넣어줍니다.
        elapsedTime++;
        lastMeltCnt = (int) glaciersToMelt.size();
        q = new LinkedList<> (glaciersToMelt);

        // 녹아야 할 빙하들을 녹여줍니다.
        melt();

        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 입력:
        n = sc.nextInt();
        m = sc.nextInt();

        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
                a[i][j] = sc.nextInt();

        // 처음에는 (0, 0) 에서 시작하여 초기 빙하에 둘러쌓여 있지 않은 물들을 찾을 수 있도록 합니다.
        q.add(new Pair(0, 0));
        visited[0][0] = true;

        boolean isGlacierExist = false;

        do {
            // 빙하에 둘러쌓여 있지 않은 물의 영역을 넓혀보며 더 녹일 수 있는 빙하가 있는지 봅니다.
            isGlacierExist = simulate();
        } while(isGlacierExist); // 더 녹일 빙하가 남아있는 한 계속 반복합니다.

        // 출력:
        System.out.print(elapsedTime + " " + lastMeltCnt);
    }
}