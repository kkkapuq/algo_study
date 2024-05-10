package codetree.intermidiate_low.backtracking.step_1.calculations_with_alphabet;

import java.util.*;
import java.io.*;

/**
 * 문제 : 알파벳과 수식 연산
 * 소요 시간 : 93분
 * 링크 : https://www.codetree.ai/missions/2/problems/calculations-with-alphabet/explanation
 */
public class Main {
    public static List<Character> nums = new ArrayList<>();
    public static String str;
    public static int answer = Integer.MIN_VALUE;

    // a~f 중 몇개의 알파벳이 나왔는지 저장하는 변수
    public static int N = 0;
    // a~f까지 무슨 수를 넣을지 정하는 리스트, 인덱스별로 a~f의 수를 의미
    public static List<Integer> selectedNums = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        input();

        // 한자릿수인 경우는
        if(str.length() == 1){
            System.out.print(4);
        } else {
            recursion(0);
            System.out.print(answer);
        }
    }

    // 알파벳을 숫자로 치환
    public static String convert() {
        String temp = str;
        // System.out.println("변환 전 수식 = " + str);
        for(int i = 0; i < selectedNums.size(); i++){
            for(int j = 0; j < temp.length(); j++){
                String s = temp.substring(j, j+1);

                if(s.equals("a")){
                    temp = temp.replace("a", selectedNums.get(i).toString());
                    break;
                } else if(s.equals("b")){
                    temp = temp.replace("b", selectedNums.get(i).toString());
                    break;
                } else if(s.equals("c")){
                    temp = temp.replace("c", selectedNums.get(i).toString());
                    break;
                } else if(s.equals("d")){
                    temp = temp.replace("d", selectedNums.get(i).toString());
                    break;
                } else if(s.equals("e")){
                    temp = temp.replace("e", selectedNums.get(i).toString());
                    break;
                } else if(s.equals("f")){
                    temp = temp.replace("f", selectedNums.get(i).toString());
                    break;
                }
            }
            // System.out.println("한 사이클 치환 이후 temp값 = " + temp);
        }
        return temp;
    }

    public static void calculate() {
        String strs = convert();

        // System.out.println("현재 수식 = " + strs);
        int temp = strs.charAt(0) - '0';
        char oper = strs.charAt(1);

        for(int i = 1; i < strs.length(); i++){
            if(strs.charAt(i) == '+'){
                oper = '+';
            } else if(strs.charAt(i) == '-'){
                oper = '-';
            } else if(strs.charAt(i) == '*'){
                oper = '*';
            } else {
                if(oper == '+'){
                    temp += strs.charAt(i) - '0';
                } else if(oper == '-'){
                    temp -= strs.charAt(i) - '0';
                } else {
                    temp *= strs.charAt(i) - '0';
                }
            }
        }
        answer = Math.max(answer, temp);
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        str = br.readLine();
        char[] chars = str.toCharArray();
        for(int i = 0; i < chars.length; i++){
            if(chars[i] == '+' || chars[i] == '-' || chars[i] == '*')
                continue;
            else {
                if(!nums.contains(chars[i]))
                    N++;
                nums.add(chars[i]);
            }
        }
    }

    public static void recursion(int num) {
        if(num == N){
            calculate();
            return;
        }

        for(int i = 1; i <= 4; i++){
            selectedNums.add(i);
            // System.out.println("현재 골라진 수들 = " + selectedNums.toString());
            recursion(num+1);
            selectedNums.remove(selectedNums.size()-1);
            // System.out.println("remove 이후 골라진 수들 = " + selectedNums.toString());
        }
    }
}