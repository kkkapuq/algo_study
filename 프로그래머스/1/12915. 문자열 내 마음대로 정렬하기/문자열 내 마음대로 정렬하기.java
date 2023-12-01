import java.util.*;

class Solution {
    public static String[] solution(String[] strings, int n) {
        String[] answer = new String[strings.length];

        // [문자, 문자열, 인덱스]로 구성된 2차원 배열을 만들고, 0번-1번 우선순위로 정렬 시킨다.
        StringIndex[] temp = new StringIndex[strings.length];
        for (int i = 0; i < strings.length; i++) {
            temp[i] = new StringIndex(strings[i].charAt(n), strings[i], i);
        }
        Arrays.sort(temp, Comparator.comparing(StringIndex::getChar).thenComparing(StringIndex::getString));

        // 이렇게 생성된 2차원 배열을 for문 돌면서 answer에 넣어주기
        for (int i = 0; i < temp.length; i++) {
            answer[i] = temp[i].getString();
        }

        return answer;
    }
}

class StringIndex {
    private char character;
    private String string;
    private int index;

    public StringIndex(char character, String string, int index) {
        this.character = character;
        this.string = string;
        this.index = index;
    }

    public char getChar() {
        return character;
    }

    public String getString() {
        return string;
    }

    public int getIndex() {
        return index;
    }
}