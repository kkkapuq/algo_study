package codetree.brute_force_III;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;


class greatJumpTest {

    @Test
    void isPossibleTest() {
        greatJump temp = new greatJump();
        // 예상 결과가 true인 경우
        temp.arr = new int[]{2, 3, 5, 4, 1}; // 임의의 배열을 설정해줍니다.
        temp.n = 5;
        temp.k = 2;
        assertTrue(temp.isPossible(4));

        // 예상 결과가 false인 경우
        temp.arr = new int[]{2, 3, 5, 4, 1}; // 임의의 배열을 설정해줍니다.
        temp.n = 5;
        temp.k = 3;
        assertFalse(temp.isPossible(2));
    }

    @Test
    void findJumpValueTest() {
        greatJump temp = new greatJump();

        // 예상 결과가 4인 경우
        temp.arr = new int[]{2, 3, 5, 4, 1}; // 임의의 배열을 설정해줍니다.
        temp.n = 5;
        temp.k = 2;
        int result1 = temp.findJumpValue();
        assertEquals(4, result1);

        // 예상 결과가 2인 경우
        temp.arr = new int[]{2, 1, 1, 1, 1}; // 임의의 배열을 설정해줍니다.
        temp.n = 5;
        temp.k = 2;
        int result2 = temp.findJumpValue();
        assertEquals(4, result2);

    }

    @Test
    void main() {
        greatJump temp = new greatJump();
    }
}