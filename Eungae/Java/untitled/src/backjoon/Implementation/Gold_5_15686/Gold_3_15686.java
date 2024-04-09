package backjoon.Implementation.Gold_5_15686;

import java.util.*;
import java.io.*;

class Gold_3_15686 {
    public static int n, m;
    public static int[][] graph;
    public static List<int[]> houses = new ArrayList<>();
    public static List<int[]> chickens = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        graph = new int[n][n];

        int answer = 0;

        // 맵 생성
        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < n; j++){
                int position = Integer.parseInt(st.nextToken());
                if(position == 1){
                    houses.add(new int[]{i, j});
                } else if(position == 2){
                    chickens.add(new int[]{i, j});
                }
                graph[i][j] = position;
            }
        }

        // 각 치킨집마다 모든 집까지의 거리를 구하고, 최솟값을 갱신해준다.
        List<Object> chickenList = new ArrayList<>();

        for(int i = 0; i < chickens.size(); i++){
            int[] chicken = chickens.get(i);
            List<Integer> tempList = new ArrayList<>();
            int distance = Integer.MAX_VALUE;
            for(int j = 0; j < houses.size(); j++){
                int[] house = houses.get(j);
                int temp = getDistance(chicken, house);
                distance = Math.min(temp, distance);
            }

            // 치킨집마다 집을 다 돌면서 결과를 list에 넣어준다.
            tempList.add(distance);
            Collections.sort(tempList);
            int sum = 0;
            for(int k = 0; i < m; k++){
                sum += tempList.get(k);
            }
            chickenList.add(chicken);
            chickenList.add(sum);
        }

        // 치킨거리가 가까운 m개의 치킨집 선정
//        Collections.sort(chickenList);
//        for(int i = 0; i < m; i++){
//
//        }

        // 각 집마다 모든 치킨집까지의 거리를 구하고, 최솟값을 갱신해준다.
        List<Integer> list = new ArrayList<>();

        for(int[] house : houses){
            int distance = Integer.MAX_VALUE;
            for(int[] chicken : chickens){
                int temp = getDistance(house, chicken);
                distance = Math.min(temp, distance);
            }
            // 집마다 치킨집을 다 돌면서 결과를 list에 넣어준다.
            list.add(distance);
        }

        // 오름차순 정렬시켜서 m개만큼만 answer에 더해주기
        Collections.sort(list);
        for(int i = 0; i < m; i++){
            answer += list.get(i);
        }

        System.out.println(answer);
    }

    // 집과 치킨집의 거리를 구하는 함수
    public static int getDistance(int[] position1, int[] position2){
        return Math.abs(position1[0] - position2[0]) + Math.abs(position1[1] - position2[1]);
    }
}