import java.util.*;
import java.io.*;

class Solution {
    // 정답 배열 선언
    public int[] answer = {0, 0};
    public int[] solution(int[][] arr) {
        
        // 분할정복 재귀함수 실행
        recursion(arr, 0, 0, arr.length);
        
        return answer;
    }
    
    
    public void recursion(int[][] arr, int r, int c, int size) {
        int mid = size / 2;
        int num = arr[r][c];
        for(int i = r; i < r+size; i++){
            for(int j = c; j < c+size; j++){
                // 만약 숫자가 맞지 않으면, 1, 2, 3, 4분면으로 분할 실행
                if(arr[i][j] != num){
                    recursion(arr, r, c+mid, mid);
                    recursion(arr, r, c, mid);
                    recursion(arr, r+mid, c, mid);
                    recursion(arr, r+mid, c+mid, mid);
                    return;
                }
            }
        }
        if(num == 0){
            answer[0]++;
        } else {
            answer[1]++;
        }
    }
}