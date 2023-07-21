package programmers.level2;

import java.util.*;

public class Problem172927 {
    public static int solution(int[] picks, String[] minerals) {
        int answer = 0;

        // 다이아/철/돌 을 캐는데 필요한 피로도, 다이아/철/돌 순임
        HashMap<String, int[]> tired = new HashMap<>();
        tired.put("diamond", new int[]{1, 5, 25});
        tired.put("iron", new int[]{1, 1, 5});
        tired.put("stone", new int[]{1, 1, 1});

        // 반례 : https://school.programmers.co.kr/questions/50674
        // 이걸 처음부터 내가 캘 수 있는 광물까지만 잘라놓고 시작해버리면됨
        int totalPicks = 5 * Arrays.stream(picks).sum();
        List<String> mineralsList = new ArrayList<>(Arrays.asList(minerals).subList(0, totalPicks));
        LinkedList<int[]> digList = new LinkedList<>();

        while (!mineralsList.isEmpty()) {
            // 5개씩 작업할 리스트를 생성해준다.
            List<String> workList = new ArrayList<>();
            while (workList.size() < 5) {
                if (!mineralsList.isEmpty()) {
                    workList.add(mineralsList.remove(0));
                } else {
                    break;
                }
            }

            // 곡괭이별 소모되는 피로도
            int dia = 0, iron = 0, stone = 0;

            // 곡괭이별로 5개를 캤을 때 피로도가 얼마나 소모되는지 계산한다.
            for (String mineral : workList) {
                dia += tired.get(mineral)[0];
                iron += tired.get(mineral)[1];
                stone += tired.get(mineral)[2];
            }

            // 다이아/철/돌 순으로 리스트에 넣어준다.
            digList.add(new int[]{dia, iron, stone});
        }

        // 돌/철/다이아 피로도 순으로 정렬되게 내림차순으로 설정
        digList.sort((a, b) -> {
            if (b[2] != a[2]) {
                return Integer.compare(b[2], a[2]);
            } else if (b[1] != a[1]) {
                return Integer.compare(b[1], a[1]);
            } else {
                return Integer.compare(b[0], a[0]);
            }
        });

        for (int index = 0; index < picks.length; index++) {
            for (int j = 0; j < picks[index]; j++) {
                // 돌 기준으로 피로도가 가장 많이 드는걸 현재 갖고있는 곡괭이중 젤 좋은 곡괭이로 캐는게 효율이 젤 좋음
                if (!digList.isEmpty()) {
                    answer += digList.removeFirst()[index];
                } else {
                    break;
                }
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        int[] picks = {0, 1, 1};
        String[] minerals = {"diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"};
        int result = solution(picks, minerals);
        System.out.println(result); // Output: 10
    }
}

