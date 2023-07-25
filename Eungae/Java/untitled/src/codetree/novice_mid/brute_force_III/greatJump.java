package codetree.novice_mid.brute_force_III;

import java.util.Scanner;

public class greatJump {
    public static int[] arr = new int[100];
    public static int n, k;

    public static boolean isPossible(int num){
        //마지막 인덱스로부터 k를 넘지않으면서 이동이 가능한가?
        int lastIdx = 0;

        for (int i = 1; i < n; i++) {
            if (arr[i] <= num) {
                if (i - lastIdx > k) {
                    return false;
                }
                lastIdx = i;
            }
        }
        return true;
    }

    public static int findJumpValue() {
        int result = 0;
        for (int i = Math.max(arr[0], arr[n - 1]); i < 100; i++) {
            if (isPossible(i)) {
                result = i;
                break;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        k = sc.nextInt();

        int result = findJumpValue();
        System.out.println(result);
    }
}
