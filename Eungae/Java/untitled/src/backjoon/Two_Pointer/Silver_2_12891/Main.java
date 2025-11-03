package backjoon.Two_Pointer.Silver_2_12891;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    private static int s, p;
    private static String DNA;
    private static int[] arr = new int[4]; // A C G T
    private static int[] currentArr = new int[4]; // A C G T
    private static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        s = Integer.parseInt(st.nextToken());
        p = Integer.parseInt(st.nextToken());
        DNA = br.readLine();
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < 4; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        for(int i = 0; i < p; i++){
            if(DNA.charAt(i) == 'A') {
                currentArr[0]++;
            } else if(DNA.charAt(i) == 'C') {
                currentArr[1]++;
            } else if(DNA.charAt(i) == 'G') {
                currentArr[2]++;
            } else if(DNA.charAt(i) == 'T') {
                currentArr[3]++;
            }
        }

        if(isPossible()) {
            answer++;
        }

        for(int i = p; i < s; i++) {
            if(DNA.charAt(i-p) == 'A') {
                currentArr[0]--;
            } else if(DNA.charAt(i-p) == 'C') {
                currentArr[1]--;
            } else if(DNA.charAt(i-p) == 'G') {
                currentArr[2]--;
            } else if(DNA.charAt(i-p) == 'T') {
                currentArr[3]--;
            }

            if(DNA.charAt(i) == 'A') {
                currentArr[0]++;
            } else if(DNA.charAt(i) == 'C') {
                currentArr[1]++;
            } else if(DNA.charAt(i) == 'G') {
                currentArr[2]++;
            } else if(DNA.charAt(i) == 'T') {
                currentArr[3]++;
            }

            if(isPossible()) {
                answer++;
            }
        }
        System.out.println(answer);
    }

    private static boolean isPossible() {
        for(int i = 0; i < 4; i++){
            if(arr[i] > currentArr[i]) {
                return false;
            }
        }
        return true;
    }
}
