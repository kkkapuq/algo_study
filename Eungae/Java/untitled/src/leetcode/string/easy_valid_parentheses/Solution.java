package leetcode.string.easy_valid_parentheses;

import java.util.*;

class Solution {
    public static boolean isValid(String s) {
        // 소, 중, 대괄호
        StringBuilder ssb = new StringBuilder();
        StringBuilder msb = new StringBuilder();
        StringBuilder lsb = new StringBuilder();
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            if(ch == '('){
                ssb.append('(');
            } else if(ch == '{'){
                msb.append('{');
            } else if(ch == '['){
                lsb.append('[');
            } else if(ssb.length() > 0 && ch == ')' && ssb.charAt(ssb.length()-1) == '(') {
                ssb.deleteCharAt(ssb.length()-1);
            } else if(msb.length() > 0 && ch == '}' && msb.charAt(msb.length()-1) == '{') {
                msb.deleteCharAt(msb.length()-1);
            } else if(lsb.length() > 0 && ch == ']' && lsb.charAt(lsb.length()-1) == '[') {
                lsb.deleteCharAt(lsb.length()-1);
            } else {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(isValid("([)]"));
    }
}