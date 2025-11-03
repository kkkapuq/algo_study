package backjoon.Sort;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class BasicForm {
    public static void main(String[] args) {
        /**
         * 1차원 배열 정렬
         */
        int[] arr = new int[]{1, 5, 4, 2, 3};
        System.out.println("arr = " + Arrays.toString(arr));

        // 오름차순
        Arrays.sort(arr);
        System.out.println("arr = " + Arrays.toString(arr));

        // int[][] 형으로 내림차순
        Integer[] arr2 = Arrays.stream(arr).boxed().toArray(Integer[]::new);

        System.out.println("arr2 = " + Arrays.toString(arr2));

        /**
         * 2차원 배열 정렬
         */
        int[][] arr3 = new int[][]{
            {1, 3},
            {4, 1},
            {3, 4},
            {2, 2}
        };

        // 0번 인덱스를 기준으로 오름차순 정렬
        Arrays.sort(arr3, (o1, o2) -> o1[0] - o2[0]);
        System.out.println("arr3 = " + Arrays.deepToString(arr3));

        // 1번 인덱스를 기준으로 내림차순 정렬
        Arrays.sort(arr3, (o1, o2) -> o2[1] - o1[1]);
        System.out.println("arr3 = " + Arrays.deepToString(arr3));

        // 2차원 배열을 2차원 리스트로 변환
        List<List<Integer>> arrToList = Arrays.stream(arr3)
            .map(row -> Arrays.stream(row).boxed().toList())
            .toList();

        arrToList.forEach(System.out::println);

        // 2차원 리스트를 2차원 배열로 전환
        List<List<Integer>> listToArr = List.of(
            List.of(1, 2, 3, 4),
            List.of(4, 3, 2, 1),
            List.of(1, 3, 4, 2)
        );

        int[][] convertedArr = listToArr.stream()
            .map(list -> list.stream().mapToInt(Integer::intValue).toArray())
            .toArray(int[][]::new);

        Integer[][] IntegerArr = listToArr.stream()
            .map(list -> list.toArray(new Integer[list.size()]))
            .toArray(Integer[][]::new);

        System.out.println("convertedArr = " + Arrays.deepToString(convertedArr));
    }
}
