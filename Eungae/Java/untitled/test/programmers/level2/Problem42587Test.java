package programmers.level2;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Problem42587Test {

    @Test
    void solution() {
        Problem42587 temp = new Problem42587();

        assertEquals(5, temp.solution(new int[]{1, 1, 9, 1, 1, 1}, 0));
    }
}